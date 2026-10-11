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

**Infrastructure as Code** — **0 / 41** tasks complete (**0%**)

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥

| Week / Module | Tasks | Progress |
| --- | --- | --- |
| Week 23 — Terraform Fundamentals | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 24 — Terraform State & Backends | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 25 — Terraform Modules I | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 26 — Terraform Modules II | 0 / 3 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 27 — Testing & CI for IaC | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 28 — Advanced Ecosystem | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 29 — Terraform + EKS (Real Cluster) | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 30 — Ansible Revision I | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 31 — Ansible Revision II + Testing | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 32 — Project Integration & Exit | 0 / 3 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |

_Auto-generated from the linked week pages. Updated by [`scripts/update_progress.py`](../scripts/update_progress.py)._
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

---

## Exit Criteria
- [ ] Can build a VPC + EKS stack from modules and destroy it cleanly
- [ ] IaC has automated tests + CI gates (both Terraform and Ansible)
- [ ] Ansible idempotency + Molecule demonstrated on at least one role
