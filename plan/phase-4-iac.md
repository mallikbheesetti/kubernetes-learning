# Phase 4 — Infrastructure as Code: Terraform + Ansible (Weeks 23–32)

**Why:** Terraform is basic–intermediate (top priority to level up). Ansible was
used before and needs revision + tests to prove retention.

**Deliverables:**
- `projects/tf-modules/` — reusable Terraform modules (VPC + EKS + IAM) with tests.
- `projects/ansible-roles/` — Ansible role collection with Molecule tests + CI.

**Resources:** KodeKloud *Terraform Basics*, *Terraform On Azure*, *Ansible Basics*,
*Ansible Advanced*, HashiCorp learning path; Terraform & Molecule docs.

---

<!-- PROGRESS:START -->
## Progress

**Infrastructure as Code** — **0 / 40** tasks complete (**0%**)

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥

| Week / Module | Tasks | Progress |
| --- | --- | --- |
| Week 23 — Terraform Fundamentals (Refresh + Solidify) | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 24 — Terraform State & Backends | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 25 — Terraform Modules I | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 26 — Terraform Modules II | 0 / 3 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 27 — Testing & CI for IaC | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 28 — Advanced Ecosystem | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 29 — Terraform + EKS (Real Cluster) | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 30 — Ansible Revision I | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 31 — Ansible Revision II + Testing | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 32 — Project Integration & Exit | 0 / 3 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |

_Auto-generated from ticked checkboxes — see the phase checklists below. Updated by [`scripts/update_progress.py`](../scripts/update_progress.py)._
<!-- PROGRESS:END -->

## Week Pages
- [Week 23 — Terraform Fundamentals](weeks/phase-4-week-23.md)
- [Week 24 — Terraform State & Backends](weeks/phase-4-week-24.md)
- [Week 25 — Terraform Modules I](weeks/phase-4-week-25.md)
- [Week 26 — Terraform Modules II](weeks/phase-4-week-26.md)
- [Week 27 — Testing & CI for IaC](weeks/phase-4-week-27.md)
- [Week 28 — Advanced Ecosystem](weeks/phase-4-week-28.md)
- [Week 29 — Terraform + EKS (Real Cluster)](weeks/phase-4-week-29.md)
- [Week 30 — Ansible Revision I](weeks/phase-4-week-30.md)
- [Week 31 — Ansible Revision II + Testing](weeks/phase-4-week-31.md)
- [Week 32 — Project Integration & Exit](weeks/phase-4-week-32.md)

## Week 23 — Terraform Fundamentals (Refresh + Solidify)
- [ ] HCL syntax; providers, resources, data sources, variables, outputs
- [ ] `init/plan/apply/destroy`; dependency graph
- [ ] Local state; `terraform fmt/validate`
- [ ] Rebuild the basic AWS example (S3 + IAM + EC2) from memory
- [ ] **Drill:** write VPC from scratch without copying

## Week 24 — Terraform State & Backends
- [ ] Remote backends (S3 + DynamoDB lock); state locking
- [ ] State operations: `import`, `mv`, `rm`, `taint`, `state pull/push`
- [ ] Workspaces vs directory-per-env
- [ ] Secrets handling; sensitive values; `.tfvars` strategy
- [ ] **Deliverable:** remote backend configured for your modules

## Week 25 — Terraform Modules I
- [ ] Module structure; inputs/outputs; versioning; registry
- [ ] Composition; avoiding duplication; `count` vs `for_each`
- [ ] Build a `vpc` module
- [ ] **Deliverable:** `modules/vpc/`

## Week 26 — Terraform Modules II
- [ ] Build `eks` and `iam` modules; wire them together
- [ ] Providers & aliases; multi-region; provisioners (and why to avoid)
- [ ] **Deliverable:** `modules/eks/`, `modules/iam/`, root composition

## Week 27 — Testing & CI for IaC
- [ ] Test types: static (tflint, checkov/tfsec), integration (Terratest), unit (native `terraform test`)
- [ ] CI pipeline: fmt → validate → plan → policy → apply (manual gate)
- [ ] Policy-as-code: OPA/Conftest or Sentinel basics
- [ ] **Deliverable:** CI workflow for the module library

## Week 28 — Advanced Ecosystem
- [ ] Terragrunt for DRY multi-env (optional but recommended)
- [ ] OpenTofu migration considerations
- [ ] Terraform Cloud/Enterprise vs OSS (state, policy, runs)
- [ ] **Deliverable:** notes + at least one Terragrunt config

## Week 29 — Terraform + EKS (Real Cluster)
- [ ] Provision a real EKS cluster via modules (or localstack/kind where cost is a concern)
- [ ] Node groups, OIDC/IRSA, add-ons (CNI, CSI, CoreDNS)
- [ ] Connect kubectl; deploy the Phase 2 app onto it
- [ ] **Deliverable:** EKS stack up + app deployed (document cost/teardown)

## Week 30 — Ansible Revision I
- [ ] Inventory, modules, playbooks, variables, facts, handlers, templates (Jinja2)
- [ ] Idempotency; `--check`/`--diff`; vault for secrets
- [ ] Re-run 5 lab exercises from memory
- [ ] **Deliverable:** a server-config playbook (e.g., harden + install stack)

## Week 31 — Ansible Revision II + Testing
- [ ] Roles, collections, galaxy; dynamic inventory (AWS)
- [ ] Molecule for role testing; CI for Ansible (ansible-lint, yamllint)
- [ ] Ansible for K8s (`kubernetes.core` collection) — bridge to your Splunk automation work
- [ ] **Deliverable:** role + Molecule test passing

## Week 32 — Project Integration & Exit
- [ ] Finalize module library + tests; Ansible role collection + CI
- [ ] Document usage; add examples; tag a release
- [ ] **Deliverable:** `projects/tf-modules/` and `projects/ansible-roles/` committed

---

## Exit Criteria
- [ ] Can build a VPC + EKS stack from modules and destroy it cleanly
- [ ] IaC has automated tests + CI gates (both Terraform and Ansible)
- [ ] Ansible idempotency + Molecule demonstrated on at least one role
