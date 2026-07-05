---
name: conventional-commits
description: Write clear git commit messages following the Conventional Commits spec. Use when the user asks to commit changes, write a commit message, or clean up commit history.
---

# Conventional Commits

Produce commit messages that follow [Conventional Commits](https://www.conventionalcommits.org/).

## Format
```
<type>(<optional scope>): <description>

<optional body>

<optional footer(s)>
```

## Types
- `feat` — a new feature
- `fix` — a bug fix
- `docs` — documentation only
- `style` — formatting, no code change
- `refactor` — code change that neither fixes a bug nor adds a feature
- `perf` — performance improvement
- `test` — adding or fixing tests
- `build` / `ci` — build system or CI changes
- `chore` — tooling, deps, housekeeping

## Rules
1. Subject line ≤ 72 chars, imperative mood ("add", not "added"/"adds"), no trailing period.
2. Use a scope when it clarifies the area, e.g. `feat(auth): ...`.
3. Explain **what and why** in the body (wrap at ~72 cols), not how — the diff shows how.
4. Breaking changes: add `!` after type/scope **and** a `BREAKING CHANGE:` footer.
5. Reference issues in the footer: `Closes #123`.
6. Before writing, inspect the actual diff (`git diff --staged`) so the message matches reality.

## Examples
```
feat(api): add pagination to the /users endpoint

Return 25 users per page with `page` and `per_page` query params.
Keeps large tenants from timing out on the list call.

Closes #482
```
```
fix: prevent crash when config file is missing

Fall back to defaults instead of throwing on first run.
```
