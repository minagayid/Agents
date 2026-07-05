---
name: agent-project-scaffold
description: Scaffold a new AI agent project using a chosen SDK (Claude Agent SDK, OpenAI Agents SDK, or Google ADK). Use when the user asks to "start", "bootstrap", or "scaffold" an agent, or to set up a new agent codebase with a tool and an MCP server wired in.
---

# Agent Project Scaffold

A reusable Agent Skill (following the [Agent Skills standard](https://agentskills.io)) that
guides an agent through bootstrapping a new AI‑agent project from a clean, runnable starting point.

## When to use
Trigger when the user wants to create a new agent project and hasn't specified every detail —
e.g. "set up a Claude agent with a weather tool", "scaffold an OpenAI agents project", or
"bootstrap a Google ADK agent".

## Steps
1. **Pick the SDK.** If unstated, ask: Claude Agent SDK (Python/TS), OpenAI Agents SDK (Python),
   or Google ADK (Python). Default to Claude Agent SDK Python.
2. **Copy the starter.** Use the matching folder in this repo's [`sdk/`](../../sdk/README.md)
   directory as the template (`quickstart.py`/`.ts`, plus `requirements.txt`/`package.json`).
3. **Set the env var.** `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or `GOOGLE_API_KEY` respectively.
4. **Add a tool.** Define one function tool relevant to the user's domain, using the SDK's tool
   pattern (`@tool` / `@function_tool` / a plain function passed in `tools=[...]`).
5. **(Optional) Wire an MCP server.** Add an entry from [`mcp/mcp-servers.json`](../../mcp/mcp-servers.json)
   (e.g. `filesystem` or `fetch`) so the agent can reach external tools.
6. **Install & run.** Install deps and run the quickstart to confirm it works end‑to‑end.
7. **Confirm.** Report the run output and the file layout you created.

## Guidelines
- Keep the first version minimal and runnable; add complexity only after it runs.
- Never hard‑code API keys — read them from environment variables.
- Prefer the SDK's async entrypoint (`Runner.run`, `run_async`, `async for … query()`).
- Match the surrounding project's language and conventions if scaffolding inside an existing repo.

## Examples
- "Bootstrap a Claude agent that can read files." → Claude Agent SDK Python + `filesystem` MCP server.
- "Scaffold an OpenAI agent with a calculator tool." → OpenAI Agents SDK + `@function_tool`.
- "Start a Google ADK weather agent." → ADK Python `root_agent` + `adk web`.
