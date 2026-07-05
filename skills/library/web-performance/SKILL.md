---
name: web-performance
description: Diagnose and improve web front-end performance (Core Web Vitals, bundle size, rendering). Use when the user asks to speed up a site, fix slow load, or improve Lighthouse/Core Web Vitals.
---

# Web Performance

Make pages load and respond fast, guided by [Core Web Vitals](https://web.dev/vitals/).

## Measure first
- Lighthouse / PageSpeed Insights and real-user metrics (field data > lab).
- Targets: **LCP** < 2.5s · **INP** < 200ms · **CLS** < 0.1.
- Use the browser Performance panel and the network waterfall to find the actual bottleneck.

## Common fixes
**Loading**
- Ship less JS: code-split, tree-shake, drop unused deps; analyze the bundle.
- Defer/async non-critical scripts; inline critical CSS, lazy-load the rest.
- Optimize images: right dimensions, modern formats (AVIF/WebP), `loading="lazy"`, `srcset`.
- Preconnect/preload key origins and fonts; use `font-display: swap`.
- Cache aggressively (immutable hashed assets, CDN, HTTP caching).

**Rendering / interactivity**
- Reduce main-thread work; break up long tasks; avoid unnecessary re-renders.
- Reserve space for images/embeds to prevent layout shift (fixed dimensions).
- Virtualize long lists; debounce expensive handlers.

**Server**
- Faster TTFB (edge/SSR caching, streaming), compression (brotli/gzip), HTTP/2+.

## Guidelines
- Fix the biggest contributor to the worst metric first, then re-measure.
- Set a performance budget so wins don't regress.
- Report before/after numbers, not just the changes made.
