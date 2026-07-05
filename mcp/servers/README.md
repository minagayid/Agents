# MCP servers — by category (fully linked)

Per-domain lists with **repo links and install commands**. For the broad name-only overview see
[`../CATALOG.md`](../CATALOG.md); for a ready-to-copy client config see
[`../mcp-servers.json`](../mcp-servers.json).

| Category | File |
|----------|------|
| 🔎 Search & web research | [`search-and-web.md`](search-and-web.md) |
| 🌐 Browser automation | [`browser-automation.md`](browser-automation.md) |
| 🗄️ Databases & data | [`databases.md`](databases.md) |
| ☁️ Cloud & DevOps | [`cloud-and-devops.md`](cloud-and-devops.md) |
| 🧰 Developer tools | [`developer-tools.md`](developer-tools.md) |
| 💬 Productivity & communication | [`productivity-and-communication.md`](productivity-and-communication.md) |
| 🎨 AI, data & media | [`ai-data-and-media.md`](ai-data-and-media.md) |
| 💳 Finance, payments & crypto | [`finance-and-crypto.md`](finance-and-crypto.md) |

## Notes

- `npx -y <pkg>` and `uvx <pkg>` run servers without a global install. `uvx` needs
  [uv](https://github.com/astral-sh/uv); `npx` needs Node.
- **Archived** reference servers still work but live in
  [modelcontextprotocol/servers-archived](https://github.com/modelcontextprotocol/servers-archived).
- **Remote** servers are hosted — add them by URL instead of a command.
- Always review a server's source and the permissions/secrets it requests before connecting it.
- Package names occasionally change; if a command fails, check the linked repo's README.
