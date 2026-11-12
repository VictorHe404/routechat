import pytest

from routechat.config import Settings


@pytest.fixture
def settings() -> Settings:
    """Explicit test settings: never read the developer's real .env."""
    return Settings(
        database_url="postgresql://test:test@localhost:5432/test",  # type: ignore[arg-type]
        app_env="test",
        _env_file=None,  # type: ignore[call-arg]
    )
