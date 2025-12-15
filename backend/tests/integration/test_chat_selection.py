import pytest
from httpx import AsyncClient
from backend.app.main import app


@pytest.mark.asyncio
async def test_chat_selection_placeholder():
  async with AsyncClient(app=app, base_url="http://test") as client:
    resp = await client.post(
        "/chat/selection",
        json={"message": "Explain", "selected_text": "foo"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("selection_used") is True
