from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Optional

from backend.agents.pipeline import run_agent


router = APIRouter(prefix="/chat", tags=["chat"])


class QueryRequest(BaseModel):
    message: str
    page_url: Optional[str] = None
    user_preferences: Optional[dict] = None


class SelectionRequest(BaseModel):
    message: str
    selected_text: str
    page_url: Optional[str] = None


@router.post("/query")
async def chat_query(payload: QueryRequest):
    if not payload.message.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty message")
    if len(payload.message) > 4000:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message too long")
    result = await run_agent(
        prompt=payload.message,
        page_url=payload.page_url,
        user_profile=payload.user_preferences,
    )
    return result


@router.post("/selection")
async def chat_selection(payload: SelectionRequest):
    if not payload.selected_text.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty selection")
    if len(payload.message) > 4000 or len(payload.selected_text) > 6000:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payload too long")
    result = await run_agent(
        prompt=payload.message,
        selection=payload.selected_text,
        page_url=payload.page_url,
    )
    return result
