from functools import lru_cache
from typing import Annotated, Union

from fastapi import Depends, FastAPI

from . import config

app = FastAPI()


@lru_cache
def get_settings():
    return config.Settings()


@app.get("/")
def read_root(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {"Hello": "World from " + settings.app_name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
