from fastapi.testclient import TestClient

from routechat import __version__
from routechat.main import create_app


def test_health_returns_ok_and_version() -> None:
    client = TestClient(create_app())

    resp = client.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "version": __version__}
