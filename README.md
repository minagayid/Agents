# Agents

Collections of **skills**, **tools**, **MCP servers**, and **plugins** for your agents.

A curated catalog of resources you can drop into Claude Code, the Claude Agent SDK,
Google ADK, OpenAI Agents SDK, and any MCP‑compatible client. Each entry links to its
upstream source and includes a short description and, where relevant, install commands.

## Contents

| Category | What's in it | Catalog |
|----------|--------------|---------|
| 🧠 **Skills** | 25 ready-to-use skills + Anthropic/Google/community catalogs | [`skills/`](skills/README.md) · [ready-to-use](skills/library/README.md) · [catalog](skills/CATALOG.md) |
| 🛠️ **Tools & Frameworks** | Agent SDKs, coding agents, and 30+ orchestration frameworks | [`tools/`](tools/README.md) |
| 🔌 **MCP Servers** | 200+ servers — name directory + 11 per-category lists with install commands | [`mcp/`](mcp/README.md) · [linked lists](mcp/servers/README.md) · [directory](mcp/CATALOG.md) |
| 🧩 **Plugins** | Official catalog + this repo's installable `agent-starter` & `skills-pack` | [`plugins/`](plugins/README.md) |
| 📦 **SDK starters** | Runnable quickstarts: Claude (Py/TS), OpenAI (Py/TS), Google ADK (Py/Go/Java), LangGraph, CrewAI | [`sdk/`](sdk/README.md) |
| 🌐 **Open APIs** | 350+ free & public APIs across 23 topics + a filter CLI — usable in any project | [`apis/`](apis/README.md) |

## Quick reference

**Skills** — a folder with a `SKILL.md` (YAML frontmatter + instructions) that teaches an
agent a repeatable task. Open standard at [agentskills.io](https://agentskills.io).

```bash
# Add a skills marketplace in Claude Code
/plugin marketplace add anthropics/skills

# Or add skills with the Agent Skills CLI
npx skills add anthropics/skills
npx skills add google/skills
```

**Plugins** — bundles of slash commands, agents, skills, hooks, and MCP config for Claude Code.

```bash
/plugin marketplace add anthropics/claude-plugins-official
/plugin install <plugin-name>@claude-plugins-official
```

**MCP servers** — expose tools/resources to any MCP client (Claude Code, Codex, ADK, VS Code…).
Browse the [MCP Registry](https://github.com/modelcontextprotocol/registry) or see [`mcp/`](mcp/README.md).
A ready‑to‑copy config for common servers is in [`mcp/mcp-servers.json`](mcp/mcp-servers.json).

**SDK starters** — copy a folder from [`sdk/`](sdk/README.md), install deps, set the API key, and run.

### This repo is also a plugin marketplace

```bash
/plugin marketplace add minagayid/Agents
/plugin install agent-starter@agents-collection   # scaffold agents from the SDK starters
/plugin install skills-pack@agents-collection      # 10 ready-to-use engineering skills
```

## Sources

The primary upstream sources this collection draws from are listed in [`SOURCES.md`](SOURCES.md).

## Contributing

Add a new entry to the relevant catalog file, keeping the table format. Include the upstream
link, a one‑line description, the license, and install instructions where they apply.
