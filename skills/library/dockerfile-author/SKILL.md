---
name: dockerfile-author
description: Write a secure, small, well-layered Dockerfile for an application. Use when the user asks to containerize an app, write or optimize a Dockerfile, or fix image size/build issues.
---

# Dockerfile Author

Produce Dockerfiles that are small, cacheable, and secure.

## Steps
1. Identify the language/runtime, build steps, and the runtime entrypoint.
2. Use a **multi-stage build**: compile/install in a build stage, copy only artifacts to a slim runtime stage.
3. Pin a specific minimal base image (e.g. `python:3.12-slim`, `node:22-alpine`, `gcr.io/distroless/*`).
4. Order layers for cache: copy dependency manifests and install **before** copying source.
5. Run as a non-root user; set `WORKDIR`, `EXPOSE`, and a healthcheck where relevant.
6. Add a `.dockerignore` (`.git`, `node_modules`, build caches, secrets).

## Example (Node)
```dockerfile
# --- build ---
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# --- runtime ---
FROM node:22-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev && npm cache clean --force
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

## Guidelines
- Never bake secrets into layers; pass them at runtime or via build secrets.
- Combine related `RUN` steps and clean package caches in the same layer.
- Prefer `COPY` over `ADD`; prefer exec-form `CMD`/`ENTRYPOINT` (`["..."]`).
- Verify with `docker build` and check final size with `docker images`.
