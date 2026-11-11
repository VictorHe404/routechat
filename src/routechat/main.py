"""FastAPI application entry point."""

from fastapi import FastAPI

from routechat import __version__


def create_app() -> FastAPI:
    """Build the app. A factory keeps tests isolated and lets config be injected later."""
    app = FastAPI(title="RouteChat", version=__version__)

    @app.get("/health", tags=["ops"])
    def health() -> dict[str, str]:
        """Liveness probe: the process is up. Does not touch the DB (that is /ready, #5)."""
        return {"status": "ok", "version": __version__}

    return app


app = create_app()
