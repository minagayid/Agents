---
name: accessibility-audit
description: Audit a web UI for accessibility against WCAG (semantics, keyboard, contrast, ARIA, forms). Use when the user asks to check or improve accessibility, a11y, or WCAG compliance.
---

# Accessibility Audit

Evaluate a web UI against [WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/) and fix the gaps.

## What to check
- **Semantics** — real elements (`<button>`, `<nav>`, `<main>`, headings in order) over `<div>` soup.
- **Keyboard** — everything operable without a mouse; visible focus; logical tab order; no traps.
- **Images & media** — meaningful `alt` text; decorative images `alt=""`; captions for video.
- **Color & contrast** — text ≥ 4.5:1 (3:1 for large); never rely on color alone to convey meaning.
- **Forms** — every input has a `<label>`; errors announced and tied to the field; clear instructions.
- **ARIA** — only when native semantics can't express it; correct roles/states; no redundant ARIA.
- **Dynamic content** — live regions announce updates; focus moved sensibly on route/modal changes.
- **Motion & zoom** — respects `prefers-reduced-motion`; usable at 200% zoom / 320px width.

## How
1. Automated pass (axe-core / Lighthouse) to catch the obvious.
2. Manual pass — tab through with the keyboard, check focus and reading order, test with a screen
   reader if possible. Automated tools catch < 50% of issues.
3. Report each issue with WCAG criterion, `selector`/location, impact, and a concrete fix.

## Guidelines
- Prioritize blockers (keyboard traps, unlabeled controls, unreadable contrast) over warnings.
- Fix at the source (semantics) rather than papering over with ARIA.
