from fastapi import FastAPI

from . import __version__

app = FastAPI()


@app.get("/", status_code=200)
async def main() -> int | None:
    """Get the current site view count."""
    pass


@app.post("/site_view", status_code=200)
async def site_view():
    """Record a site view."""
    pass


@app.get("/version", status_code=200)
async def version():
    """Get the version of the API."""
    return {"version": __version__}


@app.get("/healthz", status_code=200)
async def health():
    """Health check. Used for liveness probes."""
    return {"status": "OK"}
