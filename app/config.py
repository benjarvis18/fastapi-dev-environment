from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Default App Name"
    model_config = SettingsConfigDict(env_file=".env")
