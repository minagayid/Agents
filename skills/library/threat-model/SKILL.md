---
name: threat-model
description: Produce a threat model for a system or feature using STRIDE and data-flow analysis. Use when the user asks to threat-model, assess attack surface, or plan security for a design.
---

# Threat Model

Systematically enumerate how a system could be attacked and what to do about it.

## Steps
1. **Scope & assets.** What are we protecting (data, funds, availability, trust)? Who are the actors?
2. **Draw the data flow.** External entities, processes, data stores, and the flows between them.
   Mark **trust boundaries** (where data crosses privilege levels).
3. **Enumerate threats with STRIDE** per element/flow:
   - **S**poofing · **T**ampering · **R**epudiation · **I**nformation disclosure ·
     **D**enial of service · **E**levation of privilege
4. **Rate** each threat by likelihood × impact; focus on what crosses trust boundaries.
5. **Mitigate.** For each significant threat, name a control (authN, input validation, encryption,
   rate limiting, least privilege, logging) and who owns it.
6. **Track residual risk** you're accepting and why.

## Deliverable
A table: element/flow · STRIDE category · threat · likelihood/impact · mitigation · status.
Plus a short list of the top risks and recommended next actions.

## Guidelines
- Concentrate on trust boundaries — that's where most real vulnerabilities live.
- Prefer eliminating a threat (design change) over detecting it.
- Keep it living: revisit when the design or data flows change.
