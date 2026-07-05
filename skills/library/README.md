# Skills library (ready-to-use, offline)

Original, self-contained Agent Skills you can use immediately — no external fetch required. Each
follows the [Agent Skills standard](https://agentskills.io) (`SKILL.md` with YAML frontmatter).

## Engineering & git
| Skill | Use it when you want to… |
|-------|--------------------------|
| [`conventional-commits`](conventional-commits/SKILL.md) | Write commit messages that follow Conventional Commits. |
| [`pr-description`](pr-description/SKILL.md) | Draft a reviewer-friendly PR description from a diff. |
| [`code-review-checklist`](code-review-checklist/SKILL.md) | Review a diff for correctness, security, and tests. |
| [`unit-test-writer`](unit-test-writer/SKILL.md) | Write meaningful unit tests that catch regressions. |
| [`refactoring`](refactoring/SKILL.md) | Refactor safely without changing behavior. |
| [`debugging-methodology`](debugging-methodology/SKILL.md) | Debug failures systematically to root cause. |

## Design & implementation
| Skill | Use it when you want to… |
|-------|--------------------------|
| [`rest-api-designer`](rest-api-designer/SKILL.md) | Design consistent REST endpoints and error shapes. |
| [`react-component`](react-component/SKILL.md) | Build a clean, typed, accessible React component. |
| [`accessibility-audit`](accessibility-audit/SKILL.md) | Audit a web UI against WCAG. |
| [`web-performance`](web-performance/SKILL.md) | Improve Core Web Vitals and load time. |
| [`sql-optimizer`](sql-optimizer/SKILL.md) | Diagnose and speed up slow SQL queries. |

## Security
| Skill | Use it when you want to… |
|-------|--------------------------|
| [`secure-coding-review`](secure-coding-review/SKILL.md) | Find vulnerabilities and map them to OWASP Top 10. |
| [`threat-model`](threat-model/SKILL.md) | Threat-model a system with STRIDE. |
| [`dependency-audit`](dependency-audit/SKILL.md) | Audit dependencies for CVEs and supply-chain risk. |

## Data & AI
| Skill | Use it when you want to… |
|-------|--------------------------|
| [`data-cleaning`](data-cleaning/SKILL.md) | Clean and prep a tabular dataset. |
| [`exploratory-data-analysis`](exploratory-data-analysis/SKILL.md) | Run a structured EDA on a dataset. |
| [`prompt-engineering`](prompt-engineering/SKILL.md) | Design reliable, structured LLM prompts. |

## Cloud & DevOps
| Skill | Use it when you want to… |
|-------|--------------------------|
| [`dockerfile-author`](dockerfile-author/SKILL.md) | Write a small, secure, multi-stage Dockerfile. |
| [`kubernetes-manifest`](kubernetes-manifest/SKILL.md) | Write production-ready Kubernetes YAML. |
| [`terraform-module`](terraform-module/SKILL.md) | Write clean, reusable Terraform modules. |
| [`github-actions-ci`](github-actions-ci/SKILL.md) | Build a fast, secure CI/CD workflow. |

## Docs & process
| Skill | Use it when you want to… |
|-------|--------------------------|
| [`readme-generator`](readme-generator/SKILL.md) | Generate or improve a project README. |
| [`changelog-keeper`](changelog-keeper/SKILL.md) | Maintain a Keep-a-Changelog + SemVer changelog. |
| [`technical-writing`](technical-writing/SKILL.md) | Write clear docs (Diátaxis: tutorial/how-to/reference/explanation). |
| [`incident-postmortem`](incident-postmortem/SKILL.md) | Write a blameless postmortem with action items. |

## Use them

**In Claude Code** — install the bundle from this repo's marketplace:
```bash
/plugin marketplace add minagayid/Agents
/plugin install skills-pack@agents-collection
```

**Anywhere** — copy a skill folder into your agent's skills directory (e.g. `.claude/skills/`,
or wherever your client loads skills from). They're plain `SKILL.md` files, so they work with any
client that supports the Agent Skills standard.
