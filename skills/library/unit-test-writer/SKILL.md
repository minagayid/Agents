---
name: unit-test-writer
description: Write focused, meaningful unit tests for a function or module. Use when the user asks to add tests, improve coverage, or write tests for specific code.
---

# Unit Test Writer

Write tests that catch real regressions, not tests that just execute lines.

## Steps
1. Identify the unit under test and its contract (inputs, outputs, side effects, errors).
2. Detect the project's test framework and conventions (look at existing tests first) and match them.
3. Enumerate cases before writing:
   - **Happy path** — typical valid input.
   - **Boundaries** — empty, zero, one, max, negative, very large.
   - **Invalid input** — wrong type, null/None, malformed → expected error.
   - **Side effects** — state changes, calls to collaborators (use fakes/mocks).
4. Write one behavior per test with a descriptive name (`returns_empty_list_when_no_matches`).
5. Follow Arrange–Act–Assert; keep each test independent and deterministic.

## Guidelines
- Assert on behavior and outputs, not implementation details.
- Prefer real objects; mock only at true boundaries (network, clock, filesystem, randomness).
- Make failures readable — assert specific values with clear messages.
- Cover the failure modes, not just coverage percentage.
- Run the suite and confirm the new tests pass (and fail when the code is broken).
