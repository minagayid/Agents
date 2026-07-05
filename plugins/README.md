# 🧩 Plugins

Claude Code **plugins** bundle slash commands, agents, skills, hooks, and MCP config into an
installable package. A plugin folder looks like:

```
plugin-name/
├── .claude-plugin/plugin.json   # metadata (required)
├── .mcp.json                    # MCP server config (optional)
├── commands/                    # slash commands (optional)
├── agents/                      # agent definitions (optional)
├── skills/                      # skills (optional)
└── README.md
```

## Install

```bash
/plugin marketplace add anthropics/claude-plugins-official
/plugin install <plugin-name>@claude-plugins-official
# or browse: /plugin > Discover
```

## This repo's plugins — `agents-collection` marketplace

```bash
/plugin marketplace add minagayid/Agents
```

| Plugin | Description |
|--------|-------------|
| [`agent-starter`](agent-starter/README.md) | `/scaffold-agent` command that bootstraps a new agent project from the [SDK starters](../sdk/README.md). |
| [`skills-pack`](skills-pack/README.md) | 10 ready-to-use engineering skills (commits, PRs, review, tests, Docker, REST, README, changelog, SQL, debugging). |

## Official plugins — [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

### Development workflow
| Plugin | Description |
|--------|-------------|
| `feature-dev` | End‑to‑end feature development workflow. |
| `code-review` | Structured code review commands. |
| `pr-review-toolkit` | Tools for reviewing pull requests. |
| `code-simplifier` | Simplify and refactor code. |
| `code-modernization` | Modernize legacy code. |
| `commit-commands` | Helpers for crafting commits. |
| `session-report` | Summarize a working session. |
| `ralph-loop` | Iterative "loop" workflow automation. |

### Building agents, skills & plugins
| Plugin | Description |
|--------|-------------|
| `agent-sdk-dev` | Develop with the Claude Agent SDK. |
| `mcp-server-dev` | Build MCP servers. |
| `mcp-tunnels` | Expose/manage MCP server tunnels. |
| `skill-creator` | Create new Agent Skills. |
| `plugin-dev` | Develop Claude Code plugins. |
| `hookify` | Add and manage hooks. |
| `claude-md-management` | Manage `CLAUDE.md` files. |
| `claude-code-setup` | Set up Claude Code for a project. |
| `example-plugin` | Reference example plugin. |
| `playground` | Experimentation sandbox. |
| `project-artifact` | Generate project artifacts. |

### Language servers (LSP)
`clangd-lsp`, `csharp-lsp`, `gopls-lsp`, `jdtls-lsp`, `kotlin-lsp`, `lua-lsp`, `php-lsp`,
`pyright-lsp`, `ruby-lsp`, `rust-analyzer-lsp`, `swift-lsp`, `typescript-lsp` — language‑server
integrations for diagnostics, navigation, and refactoring.

### Design, security & output styles
| Plugin | Description |
|--------|-------------|
| `frontend-design` | Front‑end design workflows. |
| `security-guidance` | Security best‑practice guidance. |
| `explanatory-output-style` | Verbose, explanatory responses. |
| `learning-output-style` | Teaching‑oriented responses. |
| `math-olympiad` | Olympiad‑level math problem solving. |
| `cwc-makers` | "Claude with Code" maker workflows. |

> Plugin names are immutable once published. External/community plugins live under
> [`external_plugins/`](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins).
