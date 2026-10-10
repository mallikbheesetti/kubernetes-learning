# Phase 7 — Platform Engineering: Owner & Leader (Months 10–12 and ongoing)

**Why:** Your explicit goal — become a strong **Platform Owner / Leader** who can
manage Platform teams. This phase is organized as **modules**, not weeks, because
it's continuous and partly non-technical.

**Deliverables:**
- `projects/platform-reference/` — "platform-in-a-box" reference architecture.
- `docs/platform-charter.md` — vision, operating model, team topology, roadmap format.

---

<!-- PROGRESS:START -->
## Progress

**Platform Engineering: Owner & Leader** — **0 / 34** tasks complete (**0%**)

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥

| Week / Module | Tasks | Progress |
| --- | --- | --- |
| Track A — Platform as a Product (Technical Strategy) | 0 / 6 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Track B — Internal Developer Platform (Tooling) | 0 / 6 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Track C — Reliability & Operations (SRE) | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Track D — Governance, Security & FinOps | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Track E — Leadership & Team Management | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Capstone — Platform-in-a-Box | 0 / 5 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |

_Auto-generated from ticked checkboxes — see the phase checklists below. Updated by [`scripts/update_progress.py`](../scripts/update_progress.py)._
<!-- PROGRESS:END -->

## Module Pages
- [Module A — Platform as a Product](weeks/phase-7-module-a-platform-as-a-product.md)
- [Module B — Internal Developer Platform (Tooling)](weeks/phase-7-module-b-idp-tooling.md)
- [Module C — Reliability & Operations (SRE)](weeks/phase-7-module-c-reliability-sre.md)
- [Module D — Governance, Security & FinOps](weeks/phase-7-module-d-governance-finops.md)
- [Module E — Leadership & Team Management](weeks/phase-7-module-e-leadership.md)
- [Capstone — Platform-in-a-Box](weeks/phase-7-capstone.md)

## Track A — Platform as a Product (Technical Strategy)
- [ ] Define what a platform is: product, not project; internal customers
- [ ] Golden paths / paved roads; self-service vs ticketing
- [ ] Platform team topology (Team Topologies: platform, stream-aligned, enabling)
- [ ] Measuring platform success (adoption, time-to-onboard, DORA, dev NPS)
- [ ] Build vs buy; standardization vs flexibility tensions
- [ ] **Deliverable:** `docs/platform-charter.md` § vision + success metrics

## Track B — Internal Developer Platform (Tooling)
- [ ] Developer portal concepts (Backstage: catalog, templates, plugins)
- [ ] Scaffolder templates = golden path in code
- [ ] Infrastructure self-service: Crossplane vs Terraform operators
- [ ] Kubernetes-native packaging: Operators, Glasskube
- [ ] Environment provisioners (vcluster, namespaces-as-a-service)
- [ ] **Deliverable:** a minimal Backstage or equivalent template + doc

## Track C — Reliability & Operations (SRE)
- [ ] SLOs/error budgets as platform commitments (link Phase 5)
- [ ] Incident management, on-call, postmortems, blameless culture
- [ ] Chaos engineering (Chaos Mesh / Litmus) — resiliency validation
- [ ] Capacity, cost, and DR/failover ownership
- [ ] **Deliverable:** platform SLO + resiliency test runbook

## Track D — Governance, Security & FinOps
- [ ] Guardrails vs gates (policy-as-code, link Phase 6)
- [ ] Multi-tenancy models (logical/physical isolation)
- [ ] FinOps: cost allocation, showback/chargeback, rightsizing
- [ ] Compliance mapping (SOC2/PCI-ish controls) to platform standards
- [ ] **Deliverable:** governance + FinOps section in the charter

## Track E — Leadership & Team Management
- [ ] Hiring platform engineers (skills matrix, interview design)
- [ ] Mentoring, growth plans, and building a bench
- [ ] Running a platform org: rituals, roadmap, stakeholder alignment
- [ ] Influencing without authority; communicating with execs and app teams
- [ ] Managing migration/adoption change (inner source, champions)
- [ ] **Reading:** *Team Topologies*, *Accelerate* (DORA), *The Phoenix Project*,
  Google SRE book, *Platform Engineering* (human + tech)
- [ ] **Deliverable:** team operating model + hiring/interview kit + 90-day plan

---

## Capstone — Platform-in-a-Box
- [ ] Assemble end-to-end reference architecture:
  `EKS + Terraform (Phase 4) + ArgoCD (Phase 3) + Helm/Kustomize (Phase 2)
  + observability (Phase 5) + security baseline (Phase 6)`
- [ ] Add a golden-path template: "new service in 30 minutes"
- [ ] Write architecture decision records (ADRs) for key choices
- [ ] Produce a leadership deck: platform vision, roadmap, team model, KPIs
- [ ] **Deliverable:** `projects/platform-reference/` + `docs/platform-charter.md`
  + leadership deck

---

## Exit Criteria
- [ ] Articulate a platform vision + measurable success metrics
- [ ] Demonstrated a golden path from code → running service with guardrails
- [ ] Have a written team operating model, hiring kit, and 90-day plan
- [ ] Can represent platform value to both app teams and executives
