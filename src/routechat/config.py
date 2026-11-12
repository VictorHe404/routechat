"""Application settings, loaded once from environment variables (and .env in dev).

Rule: this is the ONLY module that reads the environment. Everything else receives a Settings.
"""

from functools import lru_cache
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # unrelated vars in .env must not crash startup
    )

    # Required: no default, so a missing value fails at startup, not on first request.
    database_url: SecretStr  # contains the DB password -> never printed or logged

    # Optional, with safe defaults.
    app_env: Literal["dev", "test", "prod"] = "dev"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"


@lru_cache
def get_settings() -> Settings:
    """Read the environment once per process."""
    return Settings()  # type: ignore[call-arg]  # values come from env, not arguments
