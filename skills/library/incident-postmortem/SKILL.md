---
name: incident-postmortem
description: Write a blameless incident postmortem with timeline, root cause, and action items. Use when the user asks to document an incident, write a postmortem/RCA, or run a retro on an outage.
---

# Incident Postmortem

Turn an incident into durable learning — blameless, factual, action-oriented.

## Structure
```markdown
# Postmortem: <short title>
- Date / duration / severity
- Author(s), status (draft/final)

## Summary
2–4 sentences: what happened, user impact, and how it was resolved.

## Impact
Who/what was affected, for how long, magnitude (requests, users, revenue, SLO burn).

## Timeline (UTC)
Detection → investigation → mitigation → resolution, with timestamps.
Note when and how it was detected, and time-to-detect / time-to-mitigate.

## Root cause
The technical and contributing causes. Use "5 whys" — go past the trigger to the
conditions that let it happen and stay hidden.

## What went well / what didn't
Honest, blameless.

## Action items
| Action | Owner | Priority | Due | Tracking |
Prevention, detection, and response improvements — each concrete and assigned.

## Lessons learned
```

## Principles
- **Blameless.** Focus on systems and conditions, not individuals. People act reasonably given
  the information they had.
- **Facts over narrative.** Timeline from logs/alerts, not memory.
- **Root cause, not trigger.** Ask why the safeguards didn't catch it.
- **Actionable follow-ups.** Owned, prioritized, tracked to completion — the point of the exercise.

## Guidelines
- Write while memory is fresh; circulate for review.
- Prefer systemic fixes (guardrails, automation, better alerts) over "be more careful."
