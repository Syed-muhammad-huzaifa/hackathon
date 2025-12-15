# Context7 MCP Usage (Agents SDK)

- Use the Context7 MCP server to fetch the latest OpenAI Agents SDK documentation before implementing or updating the agent pipeline.
- Target library: `/openai/openai-agents-python` (use “tools” or “agents” topics).
- Steps:
  1) Query Context7 MCP for current Agents SDK patterns (tool registration, Runner, model settings).
  2) Align function tools and agent calls to the returned patterns; avoid ad-hoc/hallucinated wiring.
  3) Record any SDK changes here with date and code pointers.

## Changelog

- 2025-12-06: Initialized guidance placeholder; consult Context7 MCP before coding agent calls.
- 2025-12-06: Confirmed Agents SDK 0.6.x patterns via Context7: use `ModelSettings(tool_choice="fetch_context")`, LitellmModel for Gemini (`gemini-2.5-flash`), and parse tool outputs from `RunResult.new_items`. Runner invoked with `run_config` for max_tokens and asyncio timeout guarding.
