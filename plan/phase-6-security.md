# Phase 6 — Kubernetes Security (Weeks 45–50)

**Why:** Secure the platform you're building. CKS-level capability (no exam
required) plus policy-as-code and secret management you can own.

**Deliverable:** `projects/hardened-cluster/` — a hardened cluster baseline with
policies, RBAC, Pod Security, network policies, and Vault-backed secrets.

**Resources:** KodeKloud *Certified Kubernetes Security Specialist (CKS)*,
*KCSA*, *Kyverno*, HashiCorp Vault; CIS Benchmark, NSA/CISA K8s hardening guide.

**Pluralsight:** [Pluralsight · Kubernetes System Hardening](https://www.pluralsight.com/courses/kubernetes-system-hardening) · [Pluralsight · Configuring and Managing Kubernetes Security](https://www.pluralsight.com/courses/configuring-managing-kubernetes-security-2) · [Pluralsight · Container Infrastructure Analysis with Trivy](https://www.pluralsight.com/courses/container-infrastructure-analysis-trivy) · [Pluralsight · Supply Chain Security for CKS](https://www.pluralsight.com/courses/supply-chain-security-cks-cert) · [Pluralsight · Monitoring, Logging and Runtime Security for CKS](https://www.pluralsight.com/courses/monitoring-logging-runtime-security-cks-cert)

---

<!-- PROGRESS:START -->
## Progress

**Kubernetes Security** — **0 / 26** tasks complete (**0%**)

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥

| Week / Module | Tasks | Progress |
| --- | --- | --- |
| Week 45 — Authentication, Authorization & RBAC | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 46 — Cluster Hardening & Pod Security | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 47 — Network Security & Supply Chain | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 48 — Runtime Security & Monitoring | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 49 — Policy-as-Code with Kyverno | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 50 — Project Integration & Exit | 0 / 4 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |

_Auto-generated from the linked week pages. Updated by [`scripts/update_progress.py`](../scripts/update_progress.py)._
<!-- PROGRESS:END -->

## Week Pages
- [Week 45 — Authentication, Authorization & RBAC](weeks/phase-6-week-45.md)
- [Week 46 — Cluster Hardening & Pod Security](weeks/phase-6-week-46.md)
- [Week 47 — Network Security & Supply Chain](weeks/phase-6-week-47.md)
- [Week 48 — Runtime Security & Monitoring](weeks/phase-6-week-48.md)
- [Week 49 — Policy-as-Code with Kyverno](weeks/phase-6-week-49.md)
- [Week 50 — Project Integration & Exit](weeks/phase-6-week-50.md)

---

## Exit Criteria
- [ ] CIS-style scan passes with documented remediations
- [ ] Pod Security restricted enforced; NetworkPolicies default-deny in place
- [ ] Signed images + admission policy + Kyverno guardrails working
- [ ] Secrets managed via Vault/External Secrets (no plaintext)
