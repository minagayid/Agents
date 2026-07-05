# agent-starter (plugin)

Scaffold and run new AI agent projects from the SDK starters in this repo.

## Install

This repository is itself a Claude Code plugin marketplace:

```bash
/plugin marketplace add minagayid/Agents
/plugin install agent-starter@agents-collection
```

## Use

```
/scaffold-agent claude my-agent
/scaffold-agent openai support-bot
/scaffold-agent adk weather-agent
```

The command copies the matching starter from [`sdk/`](../../sdk/README.md), tells you which API
key to set, and offers to add a tool and an MCP server. It bundles the
[`agent-project-scaffold`](../../skills/agent-project-scaffold/SKILL.md) skill.
