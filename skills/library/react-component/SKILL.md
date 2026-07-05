---
name: react-component
description: Build a clean, accessible, well-typed React component following modern best practices. Use when the user asks to create or refactor a React component.
---

# React Component

Write React components that are readable, reusable, accessible, and correct.

## Principles
- **Function components + hooks.** No class components for new code.
- **Typed props** (TypeScript). Model the real states; make illegal states unrepresentable.
- **Single responsibility.** One component, one job; extract subcomponents when it grows.
- **Controlled vs. uncontrolled** — pick deliberately and document which.
- **Derive, don't sync.** Compute from props/state during render instead of mirroring into extra state.
- **Effects are for side effects**, not for transforming data — most `useEffect` uses are avoidable.
- **Stable keys** in lists (not array index when items reorder).
- **Accessible by default** — semantic elements, labels, focus management, keyboard support.

## Checklist
- Props typed and minimal; sensible defaults.
- No unnecessary state or effects; memoize only where profiling shows a need.
- Handles loading / empty / error states.
- No layout shift; responsive; respects reduced motion.
- Styling matches the project's system (CSS modules / Tailwind / styled — follow existing code).

## Example (shape)
```tsx
type Props = { label: string; onClick: () => void; disabled?: boolean };

export function Button({ label, onClick, disabled = false }: Props) {
  return (
    <button type="button" onClick={onClick} disabled={disabled}>
      {label}
    </button>
  );
}
```

## Guidelines
- Match the surrounding codebase's conventions over any generic style.
- Co-locate tests; test behavior via the accessible role/name, not internals.
