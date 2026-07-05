---
name: pr-description
description: Draft a clear, reviewer-friendly pull request description from a diff or branch. Use when the user asks to open a PR, write a PR description, or summarize changes for review.
---

# PR Description

Write a pull request description that lets a reviewer understand and evaluate the change quickly.

## Steps
1. Look at the actual change: `git diff <base>...HEAD` and the commit messages.
2. If the repo has a PR template (`.github/pull_request_template.md`), mirror its sections.
3. Otherwise use the structure below. Keep it tight — link to detail rather than pasting it.

## Structure
```markdown
## Summary
1–3 sentences: what this PR does and why it exists.

## Changes
- Bullet the notable changes, grouped by area.
- Call out anything non-obvious or intentionally out of scope.

## Testing
How you verified it (commands run, cases covered, screenshots for UI).

## Risk / rollout
Migrations, feature flags, backward-compat notes, or "low risk — additive only".

## Related
Closes #123 · depends on #456
```

## Guidelines
- Lead with *why*, not a restatement of the diff.
- Make the testing section concrete — a reviewer should be able to reproduce it.
- Flag breaking changes and required follow-ups explicitly.
- Keep the title in imperative mood and scoped, matching the primary commit.
