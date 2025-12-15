import pytest
from httpx import AsyncClient
from backend.app.main import app


@pytest.mark.asyncio
async def test_chat_query_placeholder(monkeypatch):
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post(
            "/chat/query",
            json={"message": "Hello"},
        )
        assert resp.status_code == 200
        data = resp.json()
        assert "answer" in data
