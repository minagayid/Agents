# 📦 SDK starter files

Minimal, runnable quickstart files for the major agent SDKs. Copy a folder, install deps,
set the API key env var, and run.

| SDK | Language | Folder | Install | Env var |
|-----|----------|--------|---------|---------|
| Claude Agent SDK | Python | [`anthropic/python`](anthropic/python) | `pip install -r requirements.txt` | `ANTHROPIC_API_KEY` |
| Claude Agent SDK | TypeScript | [`anthropic/typescript`](anthropic/typescript) | `npm install` | `ANTHROPIC_API_KEY` |
| OpenAI Agents SDK | Python | [`openai/python`](openai/python) | `pip install -r requirements.txt` | `OPENAI_API_KEY` |
| OpenAI Agents SDK | TypeScript | [`openai/typescript`](openai/typescript) | `npm install` | `OPENAI_API_KEY` |
| Google ADK | Python | [`google-adk/python`](google-adk/python) | `pip install -r requirements.txt` | `GOOGLE_API_KEY` |
| Google ADK | Go | [`google-adk/go`](google-adk/go) | `go mod tidy` | `GOOGLE_API_KEY` |
| Google ADK | Java | [`google-adk/java`](google-adk/java) | `mvn compile` | `GOOGLE_API_KEY` |

### Framework starters

| Framework | Language | Folder | Install | Env var |
|-----------|----------|--------|---------|---------|
| LangGraph | Python | [`frameworks/langgraph-python`](frameworks/langgraph-python) | `pip install -r requirements.txt` | `ANTHROPIC_API_KEY` |
| CrewAI | Python | [`frameworks/crewai-python`](frameworks/crewai-python) | `pip install -r requirements.txt` | `OPENAI_API_KEY` |

Each `quickstart` shows: a basic query/run, adding a custom tool, and wiring an MCP server
where the SDK supports it. See the per‑folder comments for details.

> These are starter templates, not vendored copies of the SDKs. They pull the real packages
> from PyPI / npm at install time, so they stay current.
