# Skills library (ready-to-use, offline)

Original, self-contained Agent Skills you can use immediately — no external fetch required. Each
follows the [Agent Skills standard](https://agentskills.io) (`SKILL.md` with YAML frontmatter).

| Skill | Use it when you want to… |
|-------|--------------------------|
| [`conventional-commits`](conventional-commits/SKILL.md) | Write commit messages that follow Conventional Commits. |
| [`pr-description`](pr-description/SKILL.md) | Draft a reviewer-friendly PR description from a diff. |
| [`code-review-checklist`](code-review-checklist/SKILL.md) | Review a diff for correctness, security, and tests. |
| [`unit-test-writer`](unit-test-writer/SKILL.md) | Write meaningful unit tests that catch regressions. |
| [`dockerfile-author`](dockerfile-author/SKILL.md) | Write a small, secure, multi-stage Dockerfile. |
| [`rest-api-designer`](rest-api-designer/SKILL.md) | Design consistent REST endpoints and error shapes. |
| [`readme-generator`](readme-generator/SKILL.md) | Generate or improve a project README. |
| [`changelog-keeper`](changelog-keeper/SKILL.md) | Maintain a Keep-a-Changelog + SemVer changelog. |
| [`sql-optimizer`](sql-optimizer/SKILL.md) | Diagnose and speed up slow SQL queries. |
| [`debugging-methodology`](debugging-methodology/SKILL.md) | Debug failures systematically to root cause. |

## Use them

**In Claude Code** — install the bundle from this repo's marketplace:
```bash
/plugin marketplace add minagayid/Agents
/plugin install skills-pack@agents-collection
```

**Anywhere** — copy a skill folder into your agent's skills directory (e.g. `.claude/skills/`,
or wherever your client loads skills from). They're plain `SKILL.md` files, so they work with any
client that supports the Agent Skills standard.
