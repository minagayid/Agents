# Agents

Collections of **skills**, **tools**, **MCP servers**, and **plugins** for your agents.

A curated catalog of resources you can drop into Claude Code, the Claude Agent SDK,
Google ADK, OpenAI Agents SDK, and any MCP‑compatible client. Each entry links to its
upstream source and includes a short description and, where relevant, install commands.

## Contents

| Category | What's in it | Catalog |
|----------|--------------|---------|
| 🧠 **Skills** | Agent Skills (`SKILL.md` capability modules) from Anthropic, Google, and the open Agent Skills standard | [`skills/`](skills/README.md) |
| 🛠️ **Tools & Frameworks** | Agent SDKs, coding agents, and orchestration frameworks from Anthropic, OpenAI, and Google | [`tools/`](tools/README.md) |
| 🔌 **MCP Servers** | Model Context Protocol servers — Unity, filesystem, git, browser automation, GitHub, and more | [`mcp/`](mcp/README.md) |
| 🧩 **Plugins** | Claude Code plugins — plus this repo's own installable `agent-starter` plugin | [`plugins/`](plugins/README.md) |
| 📦 **SDK starters** | Runnable quickstart files for the Claude, OpenAI, and Google agent SDKs | [`sdk/`](sdk/README.md) |

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
```

## Sources

The primary upstream sources this collection draws from are listed in [`SOURCES.md`](SOURCES.md).

## Contributing

Add a new entry to the relevant catalog file, keeping the table format. Include the upstream
link, a one‑line description, the license, and install instructions where they apply.
