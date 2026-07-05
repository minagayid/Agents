---
name: readme-generator
description: Generate or improve a project README that helps someone understand, install, and use the project. Use when the user asks to write, scaffold, or improve a README.
---

# README Generator

Write a README that gets a newcomer from zero to running quickly.

## Steps
1. Infer the project from its files: language, entrypoints, manifests (`package.json`,
   `pyproject.toml`, etc.), scripts, and existing docs. Don't invent features.
2. Fill the structure below; drop sections that don't apply.

## Structure
```markdown
# Project Name
One sentence: what it is and who it's for.

## Features
- Key capabilities (3–6 bullets).

## Install
Exact commands, copy-pasteable.

## Usage
The smallest real example that shows value. Then a couple of common variations.

## Configuration
Env vars / config options as a table (name · default · description).

## Development
How to set up locally, run tests, and build.

## Contributing
Link CONTRIBUTING.md or state the basics.

## License
Name + link.
```

## Guidelines
- Put the most important thing first; a reader should grasp the project in 10 seconds.
- Every command must actually work — verify against the repo.
- Prefer a real, runnable example over prose.
- Add badges/screenshots only if they carry information.
