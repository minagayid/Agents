---
name: technical-writing
description: Write clear technical documentation — guides, references, API docs, tutorials. Use when the user asks to write or improve docs, a how-to, a runbook, or developer-facing content.
---

# Technical Writing

Write documentation people can actually use.

## Know the type (Diátaxis)
- **Tutorial** — learning by doing; hold the reader's hand to a working result.
- **How-to guide** — steps to accomplish a specific goal; assumes some context.
- **Reference** — accurate, exhaustive description (API, config, CLI); structured for lookup.
- **Explanation** — background and "why"; concepts and trade-offs.
Don't mix them in one document.

## Principles
- **Lead with the point.** State what the reader will achieve up front.
- **Task-oriented.** Organize around what the reader wants to do, not how the system is built.
- **Short sentences, active voice, present tense.** Second person ("you").
- **Show, don't just tell.** Copy-pasteable, tested examples beat prose.
- **One concept at a time**; define terms on first use; expand acronyms.
- **Scannable** — descriptive headings, short paragraphs, lists and tables where they help.
- **Say what not to do** and common pitfalls; note prerequisites and assumptions.

## Process
1. Identify the reader and their goal.
2. Outline the path to that goal; cut anything off-path.
3. Draft, then tighten — remove filler, verify every command/example actually works.
4. Add navigation (links, next steps) so readers can go deeper.

## Guidelines
- Accuracy first: wrong docs are worse than none. Verify against the real system.
- Keep it maintainable — link the source of truth instead of duplicating volatile detail.
