---
description: Scaffold a new AI agent project from a chosen SDK starter (Claude / OpenAI / Google ADK).
argument-hint: [sdk] [project-name]
---

Scaffold a new AI agent project.

Arguments: `$ARGUMENTS`
- First token (optional): the SDK — one of `claude`, `claude-ts`, `openai`, `adk`. Default `claude`.
- Second token (optional): the project directory name. Default `my-agent`.

Do the following:
1. Resolve the SDK and project name from the arguments (apply the defaults above if missing).
2. Copy the matching starter from this repo's `sdk/` directory into the new project directory:
   - `claude` → `sdk/anthropic/python`
   - `claude-ts` → `sdk/anthropic/typescript`
   - `openai` → `sdk/openai/python`
   - `adk` → `sdk/google-adk/python`
3. Tell the user which environment variable to set (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, or
   `GOOGLE_API_KEY`) and the install/run commands for that starter.
4. Offer to add a domain‑specific tool and/or an MCP server from `mcp/mcp-servers.json`.
5. If the user confirms, install dependencies and run the quickstart to verify it works, then
   report the output.

Follow the `agent-project-scaffold` skill's guidelines: keep the first version minimal and
runnable, never hard‑code API keys, and use the SDK's async entrypoint.
