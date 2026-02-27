"""Tests for FastAPI application."""

import pytest
from httpx import ASGITransport, AsyncClient

from {{ cookiecutter.project_slug }}.main import app


@pytest.fixture
async def client() -> AsyncClient:
    """Create async test client."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac


async def test_root(client: AsyncClient) -> None:
    """Test root endpoint."""
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data


async def test_health(client: AsyncClient) -> None:
    """Test health check endpoint."""
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


async def test_list_items(client: AsyncClient) -> None:
    """Test list items endpoint."""
    response = await client.get("/api/v1/items")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert isinstance(data["items"], list)


async def test_get_item(client: AsyncClient) -> None:
    """Test get item endpoint."""
    response = await client.get("/api/v1/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data


async def test_create_item(client: AsyncClient) -> None:
    """Test create item endpoint."""
    response = await client.post("/api/v1/items", json={"name": "TestItem"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "TestItem"
