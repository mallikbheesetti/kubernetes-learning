# Phase 3 — GitOps & CI/CD Depth (Weeks 15–22)

**Why:** Spinnaker/Jenkins are only basic. GitOps (ArgoCD) is the modern default
and central to platform work. Strengthen pipelines and delivery strategy.

**Deliverable:** `projects/gitops-platform/` — Git repo driving ArgoCD to sync
apps to the cluster (app-of-apps), with a CI pipeline that builds an image.

**Resources:** KodeKloud *ArgoCD/GitOps* content, *Jenkins for Beginners*,
CI/CD learning path, GitHub Actions docs, Argo Rollouts docs,
Spinnaker docs (deepen only if used at work).

---

## Week Pages
- [Week 15 — Git & Branching Discipline](weeks/phase-3-week-15.md)
- [Week 16 — GitHub Actions (Modern CI)](weeks/phase-3-week-16.md)
- [Week 17 — ArgoCD I](weeks/phase-3-week-17.md)
- [Week 18 — ArgoCD II](weeks/phase-3-week-18.md)
- [Week 19 — Jenkins (Deepen from Basic)](weeks/phase-3-week-19.md)
- [Week 20 — Spinnaker (Deepen from Basic)](weeks/phase-3-week-20.md)
- [Week 21 — Progressive Delivery](weeks/phase-3-week-21.md)
- [Week 22 — Project Integration & Exit](weeks/phase-3-week-22.md)

## Week 15 — Git & Branching Discipline
- [ ] Git recovery/advanced: rebase, cherry-pick, reflog, bisect, worktrees
- [ ] Trunk-based development, conventional commits, PR workflow
- [ ] Branch protection, CODEOWNERS, signed commits
- [ ] **Drill:** recover from a "bad merge" scenario using reflog/bisect

## Week 16 — GitHub Actions (Modern CI)
- [ ] Workflow syntax: jobs, steps, matrix, caching, artifacts, secrets
- [ ] Build + test + container build; push to a registry (GHCR)
- [ ] Reusable workflows + composite actions
- [ ] OIDC to cloud (no long-lived keys)
- [ ] **Deliverable:** `.github/workflows/build.yaml` for the umbrella app

## Week 17 — ArgoCD I
- [ ] GitOps principles; ArgoCD architecture (repo-server, controller, redis)
- [ ] Install ArgoCD; connect a Git repo; create an Application
- [ ] Sync policies: auto-sync, prune, self-heal
- [ ] **Deliverable:** ArgoCD installed + one app synced from Git

## Week 18 — ArgoCD II
- [ ] App-of-apps / ApplicationSets for multi-env
- [ ] Sync waves & hooks; health checks; drift detection
- [ ] Projects, RBAC, SSO integration concepts
- [ ] **Deliverable:** app-of-apps managing the umbrella app across overlays

## Week 19 — Jenkins (Deepen from Basic)
- [ ] Jenkins architecture (controller/agents); install on K8s
- [ ] Declarative pipelines, shared libraries, credentials, plugins
- [ ] Jenkins → build/test/deploy; multibranch pipelines
- [ ] **Deliverable:** `Jenkinsfile` re-implementing the CI build

## Week 20 — Spinnaker (Deepen from Basic)
- [ ] Spinnaker concepts: applications, pipelines, stages
- [ ] Deployment strategies: red/black, rolling, canary
- [ ] Managed delivery / declarative pipelines (if applicable to your org)
- [ ] Compare Spinnaker vs ArgoCD/GitOps (write 1-page comparison)
- [ ] **Deliverable:** notes comparing tools + a sample Spinnaker pipeline (local or diagram)

## Week 21 — Progressive Delivery
- [ ] Argo Rollouts: canary & blue/green; analysis templates
- [ ] Feature flags concepts; traffic shifting with a mesh (preview for Phase 6)
- [ ] Automated rollback on metrics failure
- [ ] **Deliverable:** canary rollout demo with automated analysis stub

## Week 22 — Project Integration & Exit
- [ ] Wire CI (Actions) → image → ArgoCD auto-sync → cluster
- [ ] Add rollout strategy + rollback docs
- [ ] Write architecture + onboarding doc for a new service (platform seed)
- [ ] **Deliverable:** `projects/gitops-platform/` complete + README

---

## Exit Criteria
- [ ] A pushed commit flows through CI → image → GitOps sync → running cluster
- [ ] Canary/blue-green rollout with automated rollback demonstrated
- [ ] Can explain ArgoCD vs Jenkins vs Spinnaker trade-offs
