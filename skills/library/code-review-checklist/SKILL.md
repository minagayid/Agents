---
name: code-review-checklist
description: Review a code change for correctness, clarity, security, and tests using a structured checklist. Use when the user asks to review code, a diff, or a pull request.
---

# Code Review Checklist

Review a diff methodically and report findings ordered by severity.

## Process
1. Read the change end-to-end first to understand intent before nitpicking.
2. Evaluate against the checklist below.
3. Report as: **Blocking** (must fix), **Non-blocking** (should fix), **Nits** (optional).
   For each finding give `file:line`, the problem, and a concrete suggestion.

## Checklist
**Correctness**
- Does it do what the PR claims? Edge cases, off-by-one, null/empty, error paths?
- Concurrency/race conditions; resource leaks (files, connections, listeners)?

**Security**
- Untrusted input validated/escaped? Injection (SQL/shell/HTML) avoided?
- Secrets not hard-coded or logged? AuthZ checks present on new endpoints?

**Design & clarity**
- Simplest solution that works? Any dead code or needless abstraction?
- Names, structure, and comments match the surrounding code?

**Tests**
- New behavior covered? Failure modes tested, not just the happy path?
- Tests deterministic and independent?

**Ops**
- Backward compatible? Migrations safe? Logging/metrics for new failure modes?

## Guidelines
- Be specific and kind; critique the code, not the author.
- Distinguish facts ("this NPEs when `x` is null") from preferences ("I'd name this `total`").
- Don't rubber-stamp — if you found nothing blocking, say what you checked.
