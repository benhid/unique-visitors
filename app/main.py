from contextlib import asynccontextmanager
from typing import Annotated

from databases import Database
from fastapi import BackgroundTasks, Depends, FastAPI, Header, Request, Response, status

from . import __version__
from .dabatase import get_db, hits_add_stmt, hits_agg_stmt, hits_table_stmt
from .security import get_client_id


@asynccontextmanager
async def lifespan(_: FastAPI):
    database = get_db()
    await database.connect()
    await database.execute(hits_table_stmt)
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/", status_code=200)
async def main(database: Database = Depends(get_db)) -> int | None:
    """Get the current site view count. Might take a few seconds to update."""
    return await database.fetch_val(hits_agg_stmt)


async def increment_site_views(client_id: str, database: Database) -> None:
    """Upsert the client ID and increment the site view count if the client ID hasn't been seen before."""
    await database.execute(hits_add_stmt, values={"client_id": client_id})


@app.post("/site_view", status_code=200)
async def site_view(
    request: Request,
    background_tasks: BackgroundTasks,
    database: Database = Depends(get_db),
    user_agent: Annotated[str | None, Header()] = None,
    referer: Annotated[str | None, Header()] = None,
) -> Response:
    """Record a site view."""
    # Some browsers honor the referer header. If it's present, we'll use it
    #  to discard inter-site visits.
    if request.base_url == referer:
        return Response(status_code=status.HTTP_200_OK)

    user_ip = request.client.host
    user_agent = user_agent or ""
    client_id = get_client_id("", user_agent, user_ip)

    # No need to wait for the task to complete.
    background_tasks.add_task(increment_site_views, client_id, database)

    return Response(status_code=status.HTTP_200_OK)


@app.get("/version", status_code=200)
async def version():
    """Get the version of the API."""
    return {"version": __version__}


@app.get("/healthz", status_code=200)
async def health():
    """Health check. Used for liveness probes."""
    return {"status": "OK"}
