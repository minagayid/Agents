---
name: refactoring
description: Refactor code safely to improve structure and readability without changing behavior. Use when the user asks to refactor, clean up, reduce duplication, or pay down tech debt.
---

# Refactoring

Improve internal structure while keeping external behavior identical.

## Golden rule
**Refactoring never changes behavior.** If you're also fixing a bug or adding a feature, do it as a
separate, clearly labeled step — never mix behavior changes into a refactor.

## Process
1. **Establish a safety net.** Ensure tests cover the code; add characterization tests if coverage is thin.
2. **Make small, reversible steps.** One transformation at a time; run tests after each.
3. **Commit frequently** with messages that say what was refactored (and that behavior is unchanged).

## Common moves
- Extract function/method; give it an intention-revealing name.
- Remove duplication (DRY) — but only genuine duplication, not coincidental similarity.
- Replace magic numbers/strings with named constants.
- Simplify conditionals (guard clauses, early returns); flatten nesting.
- Split large functions/classes by responsibility; narrow interfaces.
- Replace comments-that-explain-what with clearer code; keep comments that explain *why*.
- Delete dead code.

## Guidelines
- Match the surrounding style and conventions.
- Don't gold-plate: refactor what you're touching or what's demonstrably painful, not everything.
- Watch for behavior you might accidentally change — error handling, edge cases, side effects, ordering.
- If tests are missing and can't be added cheaply, refactor extra conservatively and verify by hand.
