import os
import pytest

PROMPTS = [
    "Summarize the preface highlights",
    "What do weeks 1-2 cover?",
    "Explain ROS 2 nodes and topics",
    "How to build a digital twin in Isaac Sim?",
    "What sensors are recommended?",
    "Describe the autonomous navigation stack",
    "How do vision-language-action models fit in?",
    "How is history stored in chat?",
    "What is the hardware overview?",
    "How to use this book roadmap?",
]

run_eval = os.getenv("RUN_EVAL", "0") == "1"

@pytest.mark.skipif(not run_eval, reason="Set RUN_EVAL=1 to run LLM eval queries")
@pytest.mark.asyncio
async def test_eval_queries_exercise_agent():
    from backend.agents.pipeline import run_agent

    results = []
    for prompt in PROMPTS:
        res = await run_agent(prompt)
        results.append(res)
    # basic assertion: we got a non-empty answer for all prompts
    assert all(r.get("answer") for r in results)
    # ensure most have context
    with_context = sum(1 for r in results if r.get("used_context"))
    assert with_context >= len(results) * 0.8
