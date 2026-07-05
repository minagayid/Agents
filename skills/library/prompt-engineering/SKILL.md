---
name: prompt-engineering
description: Design, refine, and debug LLM prompts for reliable, structured outputs. Use when the user asks to write a prompt, improve prompt reliability, reduce hallucination, or get structured output.
---

# Prompt Engineering

Craft prompts that get reliable, well-shaped results from an LLM.

## Structure a prompt
1. **Role / context** — who the model is and the task's purpose.
2. **Task** — a single, specific instruction. Split unrelated tasks.
3. **Inputs** — clearly delimited (XML tags, fenced blocks) and separated from instructions.
4. **Constraints** — length, tone, what to avoid, how to handle unknowns ("say 'unknown' if not stated").
5. **Output format** — exact schema; ask for JSON/keys explicitly when parsing downstream.
6. **Examples** — 1–3 few-shot examples covering the tricky/edge cases (huge reliability lever).

## Techniques
- **Be specific.** Vague prompts get vague answers; state exactly what "good" looks like.
- **Let it think.** For reasoning tasks, allow step-by-step working before the final answer.
- **Ground it.** Provide the source material and instruct "answer only from the context above" to
  cut hallucination; ask for citations/quotes.
- **Structured output.** Give a schema and one example; consider tool/function calling or a
  constrained-decoding library (e.g. Instructor) for guaranteed shapes.
- **Set an escape hatch.** Tell the model what to do when it can't comply, so it doesn't invent.

## Debugging
- Isolate failures: is it comprehension, formatting, or knowledge? Fix the right layer.
- Test on a small labeled set; change one thing at a time; keep a prompt changelog.
- Watch for prompt injection when inputs are untrusted — keep instructions and data separated.

## Guidelines
- Prefer the simplest prompt that works; add structure only where it earns its keep.
- Provider-specific: for Anthropic/Claude specifics, consult the `claude-api` skill.
