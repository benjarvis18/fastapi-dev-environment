"""Contains tests for the FastAPI server."""

from fastapi.testclient import TestClient

from app import config, server

client = TestClient(app=server.app)

FORBIDDEN_STATUS_CODE = 403
OK_STATUS_CODE = 200


def test_read_root_no_token() -> None:
    """Test the root endpoint without an access token."""
    response = client.get("/")
    assert response.status_code == FORBIDDEN_STATUS_CODE


def test_read_root() -> None:
    """Test the root endpoint with an access token."""
    response = client.get("/", params={"access_token": config.get_settings().api_key})
    assert response.status_code == OK_STATUS_CODE
    assert response.json() == {"Hello": "World from " + server.app.title}


def test_read_item_no_token() -> None:
    """Test the read item endpoint without an access token."""
    item_id = 1
    response = client.get(
        f"/items/{item_id}",
    )
    assert response.status_code == FORBIDDEN_STATUS_CODE


def test_read_item() -> None:
    """Test the read item endpoint with an access token."""
    item_id = 1
    response = client.get(
        f"/items/{item_id}",
        params={"access_token": config.get_settings().api_key},
    )
    assert response.status_code == OK_STATUS_CODE
    assert response.json() == {"item_id": item_id}
