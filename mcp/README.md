# 🔌 MCP Servers

[Model Context Protocol](https://modelcontextprotocol.io) servers expose tools and resources to
any MCP‑compatible client (Claude Code, Claude Desktop, Codex, Google ADK, VS Code, and more).
Browse published servers in the [MCP Registry](https://github.com/modelcontextprotocol/registry).

## Featured

### MCP for Unity — [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp)
Bridge connecting AI assistants (Claude, Codex, VS Code, local LLMs) to the **Unity Editor**.
Offers **47 MCP tool entrypoints**: create scenes/GameObjects, edit & validate C# scripts, manage
assets, run tests, profile, and build projects — all via natural language. MIT licensed.

- **Requirements:** Unity 2021.3 LTS–6.x, Python 3.10+
- **Install:** Package Manager → *Add from git URL*:
  `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`
- Then `Window → MCP for Unity → Configure All Detected Clients`.

## Official reference servers — [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

| Server | Description | Install |
|--------|-------------|---------|
| Everything | Reference/test server exercising prompts, resources, and tools. | `npx @modelcontextprotocol/server-everything` |
| Fetch | Fetch and convert web content for LLM use. | `uvx mcp-server-fetch` |
| Filesystem | Secure file operations with configurable access. | `npx @modelcontextprotocol/server-filesystem <dir>` |
| Git | Read, search, and manipulate git repositories. | `uvx mcp-server-git` |
| Memory | Persistent knowledge‑graph memory. | `npx @modelcontextprotocol/server-memory` |
| Sequential Thinking | Structured, reflective problem‑solving. | `npx @modelcontextprotocol/server-sequential-thinking` |
| Time | Time & timezone conversion utilities. | `uvx mcp-server-time` |

## Other notable servers

| Server | Description | Install |
|--------|-------------|---------|
| [github/github-mcp-server](https://github.com/github/github-mcp-server) | GitHub's official MCP server — repos, PRs, issues, Actions, code search. | see repo |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) | Browser automation via Playwright accessibility tree. | `npx @playwright/mcp` |
| [google/mcp](https://github.com/google/mcp) | Google's core MCP repository. | see repo |
| [google/chrome-enterprise-premium-mcp](https://github.com/google/chrome-enterprise-premium-mcp) | Reference Chrome Enterprise MCP server. | see repo |
| [google/mcp-security](https://github.com/google/mcp-security) | Security‑focused MCP tools & packages. | see repo |
| [google/sam](https://github.com/google/sam) | Sovereign Agent Mesh — MCP, network security, P2P. | see repo |

## Popular integrations

Common third‑party MCP servers (see the [MCP Registry](https://github.com/modelcontextprotocol/registry)
and awesome lists for the full set):

| Server | Description | Install |
|--------|-------------|---------|
| Slack | Post/read messages and manage channels. | `npx @modelcontextprotocol/server-slack` |
| Notion | Query and update Notion pages/databases. | see [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) |
| Sentry | Inspect errors and issues from Sentry. | see [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) |
| Stripe | Interact with the Stripe API. | see [stripe/agent-toolkit](https://github.com/stripe/agent-toolkit) |
| PostgreSQL | Read‑only queries and schema inspection. | `npx @modelcontextprotocol/server-postgres <conn>` |
| SQLite | Query local SQLite databases. | `uvx mcp-server-sqlite --db-path <file>` |
| Puppeteer | Headless browser automation. | `npx @modelcontextprotocol/server-puppeteer` |
| Brave Search | Web search via the Brave API. | see [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server) |

> A ready‑to‑copy config for the most common servers lives in
> [`mcp-servers.json`](mcp-servers.json).

## Curated lists & discovery

- [MCP Registry](https://github.com/modelcontextprotocol/registry) — official published servers
- [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers)
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
- [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)

## Adding an MCP server to Claude Code

```bash
# Example: filesystem server scoped to a directory
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/dir
```
