"""FastAPI application entry point.

Run with:  uvicorn routechat.main:create_app --factory
(No module-level `app`: importing this module must not require environment variables.)
"""

from fastapi import FastAPI

from routechat import __version__
from routechat.config import Settings, get_settings


def create_app(settings: Settings | None = None) -> FastAPI:
    """Build the app. Tests pass their own Settings; production reads the environment."""
    settings = settings or get_settings()
    app = FastAPI(title="RouteChat", version=__version__)
    app.state.settings = settings

    @app.get("/health", tags=["ops"])
    def health() -> dict[str, str]:
        """Liveness probe: the process is up. Does not touch the DB (that is /ready, #5)."""
        return {"status": "ok", "version": __version__, "env": settings.app_env}

    return app
