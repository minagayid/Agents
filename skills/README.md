# 🧠 Skills

Agent Skills are folders containing a `SKILL.md` (YAML frontmatter + instructions) plus optional
scripts and resources that teach an agent to perform a specialized task in a repeatable way.
They use progressive disclosure: the agent sees skill names first and loads full instructions
only when relevant. Open standard: [agentskills.io](https://agentskills.io).

```yaml
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name
Instructions the agent follows when this skill is active.
```

## The Agent Skills standard

| Skill / Repo | Description | Install |
|--------------|-------------|---------|
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | The open, portable **Agent Skills** format — spec, docs, and reference material. Cross‑product compatible (Apache‑2.0 / CC‑BY‑4.0). | See [agentskills.io](https://agentskills.io) |

## Anthropic skills — [anthropics/skills](https://github.com/anthropics/skills)

Install all via `/plugin marketplace add anthropics/skills` (Claude Code) or
`npx skills add anthropics/skills`.

### Creative & design
| Skill | Description |
|-------|-------------|
| `algorithmic-art` | Generate algorithmic / generative art. |
| `canvas-design` | Design work on a visual canvas. |
| `frontend-design` | Produce polished front‑end UI designs. |
| `theme-factory` | Build cohesive visual themes and palettes. |
| `brand-guidelines` | Apply brand voice, colors, and style rules. |
| `slack-gif-creator` | Create animated GIFs for Slack. |

### Documents
| Skill | Description |
|-------|-------------|
| `docx` | Read/create/edit Word documents. |
| `pdf` | Read/create/manipulate PDFs. |
| `pptx` | Build and edit PowerPoint decks. |
| `xlsx` | Read/create/edit Excel spreadsheets. |
| `doc-coauthoring` | Collaboratively author long‑form documents. |

### Development & technical
| Skill | Description |
|-------|-------------|
| `mcp-builder` | Scaffold and build MCP servers. |
| `web-artifacts-builder` | Build self‑contained web artifacts. |
| `webapp-testing` | Test web applications end‑to‑end. |
| `claude-api` | Reference/help for the Claude API & Anthropic SDK. |
| `skill-creator` | Create new Agent Skills. |

### Enterprise & communication
| Skill | Description |
|-------|-------------|
| `internal-comms` | Draft internal company communications. |

## Google skills — [google/skills](https://github.com/google/skills)

Agent Skills for Google products/technologies. Install with `npx skills add google/skills`
(selectable modules).

| Group | Skills |
|-------|--------|
| Agent Platform & APIs | Gemini API, Managed Agents API, Skill Registry API |
| Databases & data | AlloyDB Basics, BigQuery Basics, BigQuery AI & ML, BigQuery BigFrames, Bigtable Basics, Cloud SQL Basics |
| Compute & infra | Cloud Run Basics, GKE (17 modules: cluster creation, security, networking, observability, scaling, cost), Workload Manager Basics |
| Well‑Architected Framework | Security, reliability, cost optimization, operational excellence, performance, sustainability |
| Advertising & marketing | Google Ads API, Data Manager API, Mobile Ads, Interactive Media Ads |
| Recipes | Cloud onboarding, authentication, network observability |

## Full library

For large community collections (1,000+ skills), discovery directories, and a map of common
skill domains, see **[`CATALOG.md`](CATALOG.md)**.

## Creating your own

Use the `skill-creator` skill (Anthropic) or the `skill-creator` plugin, and follow the spec in
[agentskills/agentskills](https://github.com/agentskills/agentskills). A `template/` is provided
in [anthropics/skills](https://github.com/anthropics/skills/tree/main/template).
