"""Contains the FastAPI application and its endpoints."""

from typing import Any

from fastapi import FastAPI

from . import auth, config

API_KEY_NAME = "access_token"

SHOW_DOCS_ENVIRONMENT = ("local", "dev")  # explicit list of allowed envs

app_config: dict[str, Any] = {"title": config.get_settings().app_name}

if config.get_settings().environment not in SHOW_DOCS_ENVIRONMENT:
    app_config["openapi_url"] = ""

app = FastAPI(**app_config)


@app.get("/")
def read_root(
    settings: config.SettingsDependency,
    _: auth.AuthDependency,
) -> dict[str, str]:
    """Root endpoint that returns a greeting message."""
    return {"Hello": "World from " + settings.app_name}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, Any]:
    """Endpoint to read an item by its ID."""
    return {"item_id": item_id}
