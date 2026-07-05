---
name: kubernetes-manifest
description: Write production-ready Kubernetes manifests (Deployment, Service, probes, resources, security). Use when the user asks to write or review K8s YAML, deploy to Kubernetes, or fix a manifest.
---

# Kubernetes Manifest

Write manifests that are safe, observable, and production-ready.

## Essentials for a Deployment
- **Resource requests & limits** on every container (CPU/memory) — required for scheduling and stability.
- **Liveness, readiness, and startup probes** — don't route traffic before ready; restart when wedged.
- **Security context** — `runAsNonRoot`, drop capabilities, `readOnlyRootFilesystem`, no privilege escalation.
- **Config & secrets** via `ConfigMap`/`Secret` (or a secrets manager) — never bake into the image.
- **Labels** (`app.kubernetes.io/*`) and a matching `Service` selector.
- **Rollout strategy** (`RollingUpdate` with sane `maxUnavailable`/`maxSurge`) and replica count.
- **Pod disruption budget** + anti-affinity for HA workloads; `HorizontalPodAutoscaler` if load varies.
- Pin image tags to digests or immutable versions (never `:latest` in prod).

## Skeleton
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: web, labels: { app.kubernetes.io/name: web } }
spec:
  replicas: 3
  selector: { matchLabels: { app.kubernetes.io/name: web } }
  template:
    metadata: { labels: { app.kubernetes.io/name: web } }
    spec:
      securityContext: { runAsNonRoot: true }
      containers:
        - name: web
          image: registry/web:1.4.0
          ports: [{ containerPort: 8080 }]
          resources:
            requests: { cpu: 100m, memory: 128Mi }
            limits:   { cpu: 500m, memory: 256Mi }
          readinessProbe: { httpGet: { path: /healthz, port: 8080 }, initialDelaySeconds: 5 }
          livenessProbe:  { httpGet: { path: /healthz, port: 8080 }, initialDelaySeconds: 10 }
```

## Guidelines
- Validate with `kubectl apply --dry-run=server` / `kubeconform`; lint with `kube-linter`.
- Keep environment differences in overlays (Kustomize) or values (Helm), not copy-pasted YAML.
