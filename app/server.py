from typing import Annotated, Any, Union

from fastapi import Depends, FastAPI

from . import auth, config

API_KEY_NAME = "access_token"

SHOW_DOCS_ENVIRONMENT = ("local", "dev")  # explicit list of allowed envs

app_config: dict[str, Any] = {"title": config.get_settings().app_name}

if config.get_settings().environment not in SHOW_DOCS_ENVIRONMENT:
    app_config["openapi_url"] = ""

app = FastAPI(**app_config)


@app.get("/")
def read_root(
    settings: Annotated[config.Settings, Depends(config.get_settings)],
    api_key: Annotated[str, Depends(auth.get_api_key)],
) -> dict[str, str]:
    return {"Hello": "World from " + settings.app_name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) -> dict[str, Any]:
    return {"item_id": item_id, "q": q}
