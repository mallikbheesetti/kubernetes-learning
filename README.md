# kubernetes-learning

Learning journal and study plan for mastering Kubernetes and its closely
connected technologies (containers, GitOps, IaC, observability, security,
platform engineering, and AI/ML on Kubernetes).

## Contents

- [`learning-plan.md`](learning-plan.md) — phased 12-month plan (summary)
- [`plan/00-overview.md`](plan/00-overview.md) — detailed week-by-week checklists (index)
  - [Phase 1 — Kubernetes revision](plan/phase-1-kubernetes-revision.md) (weeks 1–5)
  - [Phase 2 — Kubernetes depth & delivery](plan/phase-2-kubernetes-depth.md) (weeks 6–14)
  - [Phase 3 — GitOps & CI/CD](plan/phase-3-gitops-cicd.md) (weeks 15–22)
  - [Phase 4 — Infrastructure as Code](plan/phase-4-iac.md) (weeks 23–32)
  - [Phase 5 — Observability ownership](plan/phase-5-observability.md) (weeks 33–44)
  - [Phase 6 — Kubernetes security](plan/phase-6-security.md) (weeks 45–50)
  - [Phase 7 — Platform engineering leadership](plan/phase-7-platform-leadership.md) (ongoing)
  - [Phase 8 — OpenShift: advanced cluster management](plan/phase-8-openshift-acm.md) (weeks 51–58)
- [`plan/weeks/`](plan/weeks/00-index.md) — one page per week with per-topic course links + exit checks
- [`resources/kodekloud-courses.md`](resources/kodekloud-courses.md) — curated KodeKloud course catalog
- [`resources/pluralsight-courses.md`](resources/pluralsight-courses.md) — curated Pluralsight course + hands-on lab catalog

## Progress

Track progress by ticking the checkboxes in the phase files above, then commit.
Green/red progress bars in [`learning-plan.md`](learning-plan.md) (per phase) and
each phase file (per week) are recomputed from that checkbox state by
`scripts/update_progress.py` — run automatically by the
[`Update progress bars`](.github/workflows/update-progress.yml) workflow on push,
or locally with `python3 scripts/update_progress.py`.

## Docs links

Every checklist item in the week pages links to the official docs for the
technology it covers (alongside the KodeKloud/YouTube video link). The mapping
(`scripts/docs-links.json`) is applied by `scripts/add_docs_links.py`; re-run it
after editing week pages to keep links consistent (`python3 scripts/add_docs_links.py`).
Items without a specific tool — exams, leadership topics, deliverables — are left
intentionally unlinked.

## Pluralsight links

Week-page topics also link to the most relevant Pluralsight course (and, where one
exists, a hands-on lab). The mapping (`scripts/pluralsight-links.json`) is applied
by `scripts/add_pluralsight_links.py`; re-run it after editing the mapping
(`python3 scripts/add_pluralsight_links.py`). The resulting course/lab set is
catalogued in [`resources/pluralsight-courses.md`](resources/pluralsight-courses.md).
