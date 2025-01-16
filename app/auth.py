from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyCookie, APIKeyHeader, APIKeyQuery

from . import config

API_KEY_NAME = "access_token"
HTTP_403_FORBIDDEN = 403

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
    api_key_cookie: str = Security(api_key_cookie),
    settings: config.Settings = Depends(config.get_settings),
):
    if api_key_query == settings.api_key:
        return api_key_query
    if api_key_header == settings.api_key:
        return api_key_header
    if api_key_cookie == settings.api_key:
        return api_key_cookie
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN,
        detail="Could not validate API key",
    )