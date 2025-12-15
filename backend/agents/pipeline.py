"""
Agent pipeline using OpenAI Agents SDK with Gemini.
IMPORTANT: Consult Context7 MCP for the latest Agents SDK patterns before modifying this file.
"""
import os
import asyncio
from typing import Any, Dict, List, Optional, Union

from agents import Agent, Runner, function_tool, ModelSettings
from agents.extensions.models.litellm_model import LitellmModel
from backend.retrieval.retriever import retrieve
from backend.agents.prompts import SYSTEM_PROMPT


def build_system_prompt(selection_present: bool = False) -> str:
    base = SYSTEM_PROMPT + "\nAlways call the fetch_context tool to gather context before answering. Use selection first when provided, then page context, then global."
    if selection_present:
        return base + "\nYou have selection context; use it first."
    return base


@function_tool
def fetch_context(query: str, selection: str | None = None, page_url: str | None = None) -> Dict[str, Any]:
    contexts = retrieve(query, selection=selection, page_url=page_url, include_selection_only=bool(selection))
    return {"contexts": contexts}


def _resolve_model() -> Union[str, LitellmModel]:
    """
    Prefer Gemini via LiteLLM wrapper (no OpenAI key requirement). Fallback to direct model string.
    """
    configured = os.getenv("AGENTS_MODEL", "gpt-4o-mini")
    gemini_key = os.getenv("GEMINI_API_KEY")
    use_litellm = os.getenv("AGENTS_USE_LITELLM", "0") == "1"
    configured_lower = configured.lower()

    # Only use LiteLLM when explicitly requested or when a Gemini model is configured.
    if gemini_key and (use_litellm or configured_lower.startswith("gemini")):
        model_name = configured
        # LiteLLM expects provider prefix like gemini/<model>
        if "/" not in model_name:
            model_name = f"gemini/{model_name}"
        return LitellmModel(model=model_name, api_key=gemini_key)
    # Fallback: assume configured model is resolvable by Agents SDK (requires OPENAI_API_KEY)
    return configured


def _build_agent(selection_present: bool = False) -> Agent:
    model = _resolve_model()
    temperature = float(os.getenv("AGENTS_TEMPERATURE", "0.2"))
    return Agent(
        name="DocsChatbot",
        instructions=build_system_prompt(selection_present),
        tools=[fetch_context],
        model=model,
        model_settings=ModelSettings(temperature=temperature, tool_choice="fetch_context"),
    )


async def run_agent(
    prompt: str,
    selection: Optional[str] = None,
    page_url: Optional[str] = None,
    user_profile: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Uses Agents SDK Runner with a fetch_context tool.
    """
    try:
        agent = _build_agent(selection_present=bool(selection))
        timeout = float(os.getenv("AGENTS_TIMEOUT", "45"))
        result = await asyncio.wait_for(
            Runner.run(
                agent,
                input=prompt,
                context={"selection": selection, "page_url": page_url, "user_profile": user_profile}
            ),
            timeout=timeout,
        )
        # Extract tool outputs if any (new SDK uses RunResult.new_items)
        contexts: List[Dict[str, Any]] = []
        for item in getattr(result, "new_items", []):
            if getattr(item, "type", "") == "tool_call_output_item":
                raw = getattr(item, "raw_item", None)
                if isinstance(raw, dict):
                    data = raw.get("output", {}) or {}
                else:
                    data = getattr(raw, "output", {}) or {}
                if isinstance(data, str):
                    import ast

                    try:
                        data = ast.literal_eval(data)
                    except Exception:
                        data = {}
                if isinstance(data, dict) and "contexts" in data:
                    contexts.extend(data["contexts"])
        citations = [ctx.get("payload", {}).get("ref") for ctx in contexts if ctx.get("payload")]
        return {
            "answer": str(result.final_output),
            "citations": [c for c in citations if c],
            "used_context": contexts,
            "fallback": False,
            "selection_used": bool(selection),
        }
    except Exception as exc:
        # Offline/dev fallback so the endpoint still responds.
        return {
            "answer": "Docs chat is not fully configured; returning a placeholder response.",
            "citations": [],
            "used_context": [],
            "fallback": True,
            "selection_used": bool(selection),
            "error": str(exc),
        }
