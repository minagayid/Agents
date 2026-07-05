---
name: debugging-methodology
description: Debug a failing program systematically — reproduce, isolate, hypothesize, fix, verify. Use when the user reports a bug, a crash, a failing test, or unexpected behavior.
---

# Debugging Methodology

Find root causes by evidence, not by guessing.

## Loop
1. **Reproduce reliably.** Get the exact steps, inputs, environment, and error/stack trace.
   A bug you can't reproduce, you can't confirm fixed.
2. **Isolate.** Shrink to the smallest failing case. Binary-search the space: comment out halves,
   `git bisect` across commits, or narrow the input until the failure flips.
3. **Read the actual error.** Stack traces and messages usually point near the cause — start there.
4. **Form one hypothesis** about the root cause and make a **prediction** you can test.
5. **Test it.** Add a targeted log/assert/breakpoint, inspect the real state, confirm or reject.
   Change one variable at a time.
6. **Fix the root cause**, not the symptom. Then verify the original repro passes.
7. **Prevent regression.** Add a test that fails without the fix and passes with it.

## Heuristics
- Question assumptions: verify what the code *actually* does vs. what you think it does.
- "It worked before" → check what changed (deps, config, data, recent commits).
- Heisenbugs (timing/order-dependent) → suspect concurrency, shared state, or reliance on
  undefined ordering.
- If truly stuck, explain the problem out loud step by step — the gap often surfaces itself.

## Guidelines
- Keep a short log of what you tried and what you observed; don't re-test the same thing.
- Don't ship a fix you can't explain — understand *why* it works.
