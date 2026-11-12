from fastapi.testclient import TestClient

from routechat import __version__
from routechat.config import Settings
from routechat.main import create_app


def test_health_returns_ok_version_and_env(settings: Settings) -> None:
    client = TestClient(create_app(settings))

    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "version": __version__, "env": "test"}
