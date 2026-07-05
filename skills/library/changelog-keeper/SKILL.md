---
name: changelog-keeper
description: Maintain a CHANGELOG following Keep a Changelog and semantic versioning. Use when the user asks to update the changelog, prepare a release, or summarize changes since the last version.
---

# Changelog Keeper

Maintain a human-readable `CHANGELOG.md` per [Keep a Changelog](https://keepachangelog.com/)
and [SemVer](https://semver.org/).

## Format
```markdown
# Changelog

## [Unreleased]

## [1.4.0] - 2026-07-05
### Added
- New `--json` output flag.
### Changed
- Faster startup by lazy-loading plugins.
### Fixed
- Crash when the config file was empty.
### Deprecated
### Removed
### Security
```

## Rules
- Group entries under **Added / Changed / Deprecated / Removed / Fixed / Security**.
- Write for humans, present tense, one bullet per change; link issues/PRs.
- Keep an `[Unreleased]` section at the top; on release, rename it to the new version + date.
- **SemVer**: breaking → major, backward-compatible feature → minor, fix → patch.
- Derive entries from merged commits/PRs since the last tag (`git log <lastTag>..HEAD`), but
  rewrite them as user-facing notes — don't dump raw commit subjects.

## Guidelines
- Omit noise (internal refactors with no user impact) unless notable.
- Keep newest version at the top; never rewrite released history.
