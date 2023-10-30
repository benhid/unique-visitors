from typing import Annotated

from fastapi import BackgroundTasks, FastAPI, Header, Request, Response, status

from . import __version__
from .security import get_client_id

app = FastAPI()


@app.get("/", status_code=200)
async def main() -> int | None:
    """Get the current site view count. Might take a few seconds to update."""
    # TODO: Fetch from database.
    pass


async def increment_site_views(client_id: str) -> None:
    # TODO
    pass


@app.post("/site_view", status_code=200)
async def site_view(
    request: Request,
    background_tasks: BackgroundTasks,
    user_agent: Annotated[str | None, Header()] = None,
) -> Response:
    """Record a site view."""
    user_ip = request.client.host
    user_agent = user_agent or ""
    client_id = get_client_id("", user_agent, user_ip)

    # No need to wait for the task to complete.
    background_tasks.add_task(increment_site_views, client_id)

    return Response(status_code=status.HTTP_200_OK)


@app.get("/version", status_code=200)
async def version():
    """Get the version of the API."""
    return {"version": __version__}


@app.get("/healthz", status_code=200)
async def health():
    """Health check. Used for liveness probes."""
    return {"status": "OK"}
