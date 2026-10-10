# Kubernetes & Platform Engineering Learning Plan — Arjun Besetti

Tailored to the profile: **Principal DevOps & Platform Engineer**, 15+ years,
currently VP–Lead Software Engineer (Observability) at Wells Fargo.
Background: CKA certified (2025) but hands-on Kubernetes work was ~2 years ago;
AWS SAA; strong scripting (Python/Bash); observability exposure (Splunk limited
to log onboarding; Dynatrace Managed cluster management ~2 years ago).

<!-- PROGRESS:START -->
## Progress

**Overall** — **0 / 256** tasks complete (**0%**)

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥

| Phase | Timeline | Tasks | Progress |
| --- | --- | --- | --- |
| 1 — Kubernetes Revision & Re-Fluency | Weeks 1–5 | 0 / 33 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| 2 — Kubernetes Depth & Application Delivery | Weeks 6–14 | 0 / 42 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| 3 — GitOps & CI/CD Depth | Weeks 15–22 | 0 / 34 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| 4 — Infrastructure as Code | Weeks 23–32 | 0 / 40 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| 5 — Observability Platform Ownership | Weeks 33–44 | 0 / 49 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| 6 — Kubernetes Security | Weeks 45–50 | 0 / 24 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| 7 — Platform Engineering: Owner & Leader | Months 10–12+ | 0 / 34 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |

_Auto-generated from checklist state. Run [`scripts/update_progress.py`](scripts/update_progress.py) (or let the `Update progress bars` GitHub Action run it) to refresh._
<!-- PROGRESS:END -->

## Goal

Become a **strong Platform Owner / Technical Leader** who can:
- Personally operate and troubleshoot Kubernetes at depth (refresh the 2-year gap).
- Own and build observability platforms end-to-end (not just onboard logs).
- Drive Infrastructure as Code to an advanced, production standard.
- Lead and grow Platform Engineering teams (platform-as-a-product, golden paths).

**Certifications: not a current target.** Treat CNCF/cloud exams as *optional
checkpoints* later to validate skills — not as the objective. The objective is
demonstrable, hands-on capability and portfolio evidence.

## Starting-Point Gap Analysis (updated)

| Area | Current reality | Priority |
| --- | --- | --- |
| Kubernetes | CKA held, but little hands-on for ~2 yrs | **High — revise** |
| Spinnaker / Jenkins | Basic only, not in-depth | Medium |
| GitOps (ArgoCD) | Little/no exposure | **High** |
| Splunk | Log onboarding only; no cluster build/manage | **High** |
| Dynatrace Managed | Cluster mgmt done ~2 yrs ago | **High — revise** |
| Prometheus / Grafana / Loki / EFK | Limited hands-on | **High** |
| Ansible | Used before; needs revision + tests | **High — revise** |
| Terraform | Basic–intermediate only | **High — level up** |
| AWS EKS / GCP | AWS SAA-level; EKS light | Medium |
| Service mesh (Istio) / Gateways | None | Medium |
| Platform Engineering (as owner/leader) | Practitioner, not owner | **High** |
| Team leadership / platform-as-product | Some mentoring | **High** |

## Phased Plan (~12 months, ~8–10 hrs/week)

### Phase 1 — Kubernetes Revision & Re-Fluency (Weeks 1–5)
*Close the 2-year gap first.*
- Re-run the CKA curriculum as a **refresh**, not first-time study
- Hands-on: `kubectl`, troubleshooting, scheduling, control-plane internals, etcd/backup
- Build/rebuild a multi-node cluster locally (kind/k3d) and on a cloud free tier
- Labs: KodeKloud Kubernetes / CKA course labs + hands-on challenges
- **Project:** automated cluster bootstrap script + runbook you can re-run anytime
- **Exit test:** complete a timed CKA-style lab set cold, without notes

### Phase 2 — Kubernetes Depth & Application Delivery (Weeks 6–14)
- Kubernetes Networking Deep Dive (CNI, Services, Ingress, NetworkPolicy)
- Helm for Beginners + Kustomize (packaging/config at scale)
- Kubernetes Operators (extend the platform)
- Kubernetes Autoscaling; troubleshooting for developers
- **Project:** Helm-umbrella app (API + worker + DB) with Kustomize overlays on your cluster

### Phase 3 — GitOps & CI/CD Depth (Weeks 15–22)
- **ArgoCD** (priority) — declarative delivery, sync waves, app-of-apps
- GitHub Actions (modern pipelines); strengthen **Jenkins** from basic → practical
- **Spinnaker**: deepen from basic — pipelines, deployment strategies (only if used in your org)
- CI/CD learning path
- **Project:** GitOps repo driving ArgoCD to a cluster; progressive delivery demo

### Phase 4 — Infrastructure as Code: Go Deep (Weeks 23–32)
*Terraform basic→advanced is a top priority.*
- Terraform: modules, remote state/backends, workspaces, providers, testing
  (Terratest), OpenTofu/Terragrunt, CI for IaC, policy-as-code (Sentinel/OPA)
- Terraform On Azure (given enterprise mix); Terraform + EKS
- **Ansible revision + tests**: idempotency, roles, collections, Molecule testing,
  AWX; re-run lab scenarios to prove retention
- **Project:** reusable Terraform module library (VPC + EKS + IAM) with tests,
  plus an Ansible role collection with CI
- **Optional checkpoint:** Terraform Associate when ready

### Phase 5 — Observability Platform Ownership (Weeks 33–44)
*Move from consuming tools to building/owning them.*
- **Prometheus + Grafana**: deploy and operate the stack on K8s; PromQL; alerting
- **Grafana Loki** and **EFK** (Elasticsearch/Fluent Bit/Kibana) — build the clusters
- OpenTelemetry instrumentation; SLOs/error budgets
- **Splunk**: go beyond onboarding — indexers, search heads, deployment servers,
  clustering, sizing, lifecycle (align with your self-service platform work)
- **Dynatrace Managed revision**: cluster architecture, ActiveGate, HA, upgrades, DR
- **Project:** full open-source observability platform (metrics+logs+traces) on
  Kubernetes, documented as an internal product with onboarding golden path

### Phase 6 — Kubernetes Security (Weeks 45–50)
- CKS-level skills (no exam required): cluster hardening, RBAC, Pod Security,
  supply-chain, runtime security, seccomp/AppArmor
- Kyverno policy-as-code; HashiCorp Vault for secrets
- **Project:** hardened cluster baseline with policies + secret management

### Phase 7 — Platform Engineering: Owner & Leader (Months 10–12 and ongoing)
*The dimension that matters most for your next role.*
- **Platform-as-a-Product**: internal developer platform (IDP), golden paths,
  self-service, paved roads, developer experience, adoption metrics
- Tooling: Backstage, Crossplane, Operators, Glasskube, multi-tenancy, GitOps at scale
- Reliability & SRE: SLOs, incident management, chaos engineering, DR/failover
- Governance: standards, cost/FinOps, security guardrails across teams
- **Leadership**: defining platform vision/roadmap, stakeholder alignment,
  building and managing platform teams, hiring, mentoring, running a platform org
- **Reading/learning**: Team Topologies, Platform Engineering (humans+tech),
  Accelerate/DORA metrics, SRE book
- **Capstone:** documented "platform-in-a-box" reference architecture
  (EKS + Terraform + ArgoCD + Helm/Kustomize + observability + policies)
  and a platform team operating model / charter you could present to leadership

## Suggested Weekly Cadence (~10 hrs)
- Mon–Fri: 1 hr theory/course + 30 min hands-on lab
- Sat: 2–3 hr project deep work
- Sun: 1 hr review + notes committed to this repo; fortnightly Ansible/Terraform recall drills

## KodeKloud Resources
See `resources/kodekloud-courses.md` for the full curated catalog and URLs.
Suggested order: Kubernetes → Docker → CI/CD → IaC → Observability →
Kubernetes security → Platform Engineering → (optionally) AI/ML on K8s.

## Progress Log
Track completion here (date + activity + artifact/link):
- [ ] Phase 1: Kubernetes revision complete; cold CKA-style lab passed
- [ ] Phase 2: delivery project shipped (Helm + Kustomize)
- [ ] Phase 3: ArgoCD GitOps project shipped
- [ ] Phase 4: Terraform module library + Ansible role collection with tests
- [ ] Phase 5: open-source observability platform built; Splunk/Dynatrace revised
- [ ] Phase 6: hardened cluster baseline with policies + Vault
- [ ] Phase 7: platform reference architecture + team operating model written
