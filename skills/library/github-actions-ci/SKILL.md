---
name: github-actions-ci
description: Write or improve a GitHub Actions CI/CD workflow (build, test, lint, cache, secure secrets). Use when the user asks to set up CI, write a GitHub Actions workflow, or fix a failing pipeline.
---

# GitHub Actions CI

Build reliable, fast, secure GitHub Actions workflows.

## A solid CI workflow
```yaml
name: CI
on:
  push: { branches: [main] }
  pull_request:
permissions:
  contents: read           # least privilege by default
concurrency:               # cancel superseded runs on the same ref
  group: ci-${{ github.ref }}
  cancel-in-progress: true
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run lint
      - run: npm test
```

## Practices
- **Pin actions** to a version (or SHA for third-party) and set minimal `permissions`.
- **Cache** dependencies (built into `setup-*` actions) to cut run time.
- **Matrix** across versions/OSes when it matters; keep the fast checks as required gates.
- **Secrets** via `secrets.*` — never echo them; restrict who can run on `pull_request_target`.
- **Fail fast, report clearly**; upload artifacts/logs on failure.
- Separate **CI** (test on PR) from **CD** (deploy on tag/release) with environment protection rules.
- Add `concurrency` to avoid wasted duplicate runs.

## Guidelines
- Keep the critical path under a few minutes; parallelize independent jobs.
- Treat workflow files as code — review changes; beware supply-chain risk from untrusted actions.
- Reproduce failures locally where possible before pushing "fix CI" commits.
