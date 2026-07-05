---
name: dependency-audit
description: Audit project dependencies for known vulnerabilities, outdated versions, and license/supply-chain risk. Use when the user asks to audit dependencies, check for CVEs, or update packages safely.
---

# Dependency Audit

Assess and reduce risk from third-party dependencies.

## Steps
1. **Inventory.** Identify manifests and lockfiles (`package-lock.json`, `pnpm-lock.yaml`,
   `poetry.lock`, `requirements.txt`, `go.sum`, `Cargo.lock`, `pom.xml`).
2. **Scan for known vulns** with the native tooling:
   - npm/pnpm/yarn → `npm audit` / `pnpm audit`
   - Python → `pip-audit`
   - Go → `govulncheck ./...`
   - Rust → `cargo audit`
   - Multi-eco → OSV-Scanner, Trivy, or GitHub Dependabot alerts
3. **Triage** each finding: is the vulnerable code path actually reachable? Severity + exploitability,
   not just CVSS.
4. **Remediate** highest risk first: bump to a patched version; if none exists, pin/override, apply a
   workaround, or replace the dependency.
5. **Check hygiene:** unmaintained/abandoned packages, typosquats, license incompatibilities,
   and needless transitive bloat.
6. **Verify** the app still builds and tests pass after upgrades.

## Guidelines
- Prefer the smallest safe bump; read the changelog for breaking changes.
- Commit lockfile changes; keep upgrades reviewable (don't mix with feature work).
- Automate going forward (Dependabot/Renovate) so this doesn't rot.
- Report: package · current → fixed version · severity · reachable? · action taken.
