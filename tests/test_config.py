import pytest
from pydantic import ValidationError

from routechat.config import Settings


def test_missing_database_url_fails_fast(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)

    with pytest.raises(ValidationError, match="database_url"):
        Settings(_env_file=None)  # type: ignore[call-arg]


def test_reads_values_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@db:5432/x")
    monkeypatch.setenv("APP_ENV", "prod")

    s = Settings(_env_file=None)  # type: ignore[call-arg]

    assert s.database_url.get_secret_value() == "postgresql://u:p@db:5432/x"
    assert s.app_env == "prod"


def test_invalid_env_value_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://u:p@db:5432/x")
    monkeypatch.setenv("APP_ENV", "production")  # typo for "prod"

    with pytest.raises(ValidationError, match="app_env"):
        Settings(_env_file=None)  # type: ignore[call-arg]


def test_secret_never_appears_in_repr(settings: Settings) -> None:
    assert "test:test" not in repr(settings)
    assert "test:test" not in str(settings.model_dump())
