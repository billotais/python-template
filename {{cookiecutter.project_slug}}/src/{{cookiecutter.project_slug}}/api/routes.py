"""API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/items")
async def list_items() -> dict[str, list]:
    """List all items."""
    return {"items": []}


@router.get("/items/{item_id}")
async def get_item(item_id: int) -> dict[str, int | str]:
    """Get a specific item."""
    return {"id": item_id, "name": f"Item {item_id}"}


@router.post("/items")
async def create_item(name: str) -> dict[str, int | str]:
    """Create a new item."""
    return {"id": 1, "name": name}
