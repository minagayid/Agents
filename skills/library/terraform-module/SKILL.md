---
name: terraform-module
description: Write clean, reusable Terraform modules and safe infrastructure changes. Use when the user asks to write Terraform/IaC, create a module, or review infrastructure code.
---

# Terraform Module

Author Terraform that is reusable, reviewable, and safe to apply.

## Module structure
```
module/
├── main.tf         # resources
├── variables.tf    # typed inputs with descriptions + validation
├── outputs.tf      # outputs consumers need
├── versions.tf     # required_version + provider version constraints
└── README.md       # purpose, inputs, outputs, example usage
```

## Practices
- **Typed variables** with `description`, sensible `default`s, and `validation` blocks; mark secrets `sensitive = true`.
- **Pin versions** — `required_version` and provider constraints; commit `.terraform.lock.hcl`.
- **Remote state** with locking (e.g. S3 + DynamoDB, GCS, Terraform Cloud); never commit state or secrets.
- **No hard-coded values** — parameterize via variables; keep environments in separate workspaces/dirs.
- **Least privilege** IAM; tag resources; use `for_each` over `count` for stable addressing.
- **Composable** — small modules with clear inputs/outputs; avoid provider config inside reusable modules.

## Workflow (safe change)
1. `terraform fmt` and `terraform validate`.
2. `terraform plan` — **read the plan**; confirm no unexpected destroy/replace.
3. Apply to non-prod first; use `-target` sparingly and only knowingly.
4. Review drift; keep applies small and reversible.

## Guidelines
- Treat `plan` output as the review artifact — a resource being destroyed/recreated is a red flag.
- Prefer data sources and outputs over duplicating values across modules.
