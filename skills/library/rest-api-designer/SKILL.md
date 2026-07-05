---
name: rest-api-designer
description: Design clean, consistent REST API endpoints (resources, methods, status codes, errors, pagination). Use when the user asks to design an API, add endpoints, or review API shape.
---

# REST API Designer

Design HTTP APIs that are predictable and easy to consume.

## Principles
- **Resources are nouns, plural**: `/orders`, `/orders/{id}`, `/orders/{id}/items`.
- **Methods carry the verb**: `GET` (read), `POST` (create), `PUT`/`PATCH` (replace/update), `DELETE`.
- **GET is safe and idempotent**; never mutate on GET.

## Status codes
- `200 OK`, `201 Created` (+ `Location`), `204 No Content`.
- `400` invalid input · `401` unauthenticated · `403` forbidden · `404` not found ·
  `409` conflict · `422` validation · `429` rate limited · `500` server error.

## Conventions
- **Errors**: consistent JSON body, e.g. `{ "error": { "code": "...", "message": "...", "details": [...] } }`.
- **Pagination**: cursor-based preferred (`?limit=&cursor=`), return `next_cursor`.
- **Filtering/sorting**: `?status=open&sort=-created_at`.
- **Versioning**: prefix (`/v1/...`) or header; be explicit and stable.
- **Idempotency**: support an `Idempotency-Key` header for non-idempotent creates.
- Use ISO-8601 timestamps, `snake_case` or `camelCase` consistently, and stable field names.

## Deliverable
Produce an endpoint table (method · path · purpose · request · response · status codes) and,
if useful, an OpenAPI sketch. Call out auth, rate limits, and breaking-change risks.
