from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_key: str = Field(default="default_key")
    app_name: str = Field(default="My App")
    environment: str = Field(default="local")
    cookie_domain: str = Field(default="localhost")
    model_config = SettingsConfigDict(env_file=".env", secrets_dir="secrets")


@lru_cache
def get_settings() -> Settings:
    return Settings()
