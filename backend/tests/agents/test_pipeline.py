import asyncio
from typing import Any, Dict

import pytest

from backend.agents import pipeline
from agents.extensions.models.litellm_model import LitellmModel


def test_resolve_model_prefers_litellm(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("GEMINI_API_KEY", "dummy-key")
    monkeypatch.setenv("AGENTS_MODEL", "gemini-2.5-flash")

    model = pipeline._resolve_model()

    assert isinstance(model, LitellmModel)
    assert "gemini" in getattr(model, "model", "")


def test_resolve_model_falls_back_to_string(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setenv("AGENTS_MODEL", "gpt-4o-mini")

    model = pipeline._resolve_model()

    assert model == "gpt-4o-mini"


def test_resolve_model_prefers_string_when_non_gemini(monkeypatch: pytest.MonkeyPatch):
    # Even with a Gemini key, if a non-Gemini model is configured we should not force LiteLLM.
    monkeypatch.setenv("GEMINI_API_KEY", "dummy-key")
    monkeypatch.setenv("AGENTS_MODEL", "gpt-4o-mini")

    model = pipeline._resolve_model()

    assert isinstance(model, str)
    assert model == "gpt-4o-mini"


def test_run_agent_parses_tool_output(monkeypatch: pytest.MonkeyPatch):
    class DummyRaw:
        def __init__(self) -> None:
            self.output = {"contexts": [{"payload": {"ref": "doc-1"}}]}

    class DummyItem:
        type = "tool_call_output_item"
        raw_item = DummyRaw()

    class DummyResult:
        final_output = "hi"
        new_items = [DummyItem()]

    async def fake_run(agent: Any, input: str, context: Dict[str, Any] | None = None) -> DummyResult:  # type: ignore[override]
        return DummyResult()

    monkeypatch.setenv("AGENTS_TIMEOUT", "2")
    monkeypatch.setenv("GEMINI_API_KEY", "dummy-key")
    monkeypatch.setenv("AGENTS_MODEL", "gemini-2.5-flash")
    monkeypatch.setattr(pipeline.Runner, "run", fake_run)

    result = asyncio.run(pipeline.run_agent("hello", selection="foo", page_url="https://example.com"))

    assert result["answer"] == "hi"
    assert result["citations"] == ["doc-1"]
    assert result["selection_used"] is True
    assert result["fallback"] is False
