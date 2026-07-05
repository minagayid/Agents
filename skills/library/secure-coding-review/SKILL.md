---
name: secure-coding-review
description: Review code for security vulnerabilities (injection, authz, secrets, crypto, deserialization). Use when the user asks for a security review, to find vulnerabilities, or to harden code.
---

# Secure Coding Review

Find and prioritize security vulnerabilities in a change or codebase. Map findings to the
[OWASP Top 10](https://owasp.org/www-project-top-ten/) where relevant.

## What to check
- **Injection** — SQL/NoSQL/OS-command/LDAP built from unsanitized input. Require parameterized
  queries / safe APIs, never string concatenation.
- **AuthN/AuthZ** — every sensitive endpoint checks identity *and* permission; no missing object-level
  authorization (IDOR); no privilege escalation paths.
- **Secrets** — no hard-coded keys/tokens/passwords; secrets from env/secret manager; not logged.
- **Input validation & output encoding** — validate on the server; encode output for its sink (HTML/JS/SQL/shell).
- **XSS/CSRF** — output escaping; anti-CSRF tokens on state-changing requests.
- **Crypto** — modern algorithms, no MD5/SHA1 for passwords (use bcrypt/argon2), no hand-rolled crypto,
  random from a CSPRNG.
- **Deserialization / SSRF / path traversal** — untrusted data never drives file paths, URLs, or object graphs.
- **Dependencies** — known-vulnerable versions; run an SCA tool.
- **Errors & logging** — no stack traces/secrets leaked to users; security events logged.

## Report format
For each finding: **severity** (Critical/High/Medium/Low), `file:line`, the vulnerability class,
a concrete exploit scenario, and the fix. Lead with the most severe.

## Guidelines
- Prefer proof over suspicion — show the tainted data path from source to sink.
- Recommend the framework's safe primitive rather than a bespoke fix.
- Note defense-in-depth, but don't drown criticals in style nits.
