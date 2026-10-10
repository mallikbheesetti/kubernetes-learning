# Phase 2 — Kubernetes Depth & Application Delivery (Weeks 6–14)

**Why:** Move from "can run workloads" to "can design, package and deliver
production applications on Kubernetes."

**Deliverable:** `projects/helm-umbrella-app/` — an API + worker + DB app deployed
via a Helm umbrella chart with Kustomize overlays for dev/staging/prod.

**Resources:** KodeKloud *Kubernetes Networking Deep Dive*, *Helm for Beginners*,
*Kustomize*, *Kubernetes Operators*, *Kubernetes Autoscaling*,
*Kubernetes Troubleshooting for Application Developers*.

---

## Week 6 — Networking Deep Dive I
- [ ] CNI fundamentals: plugin model, pod IP allocation, VXLAN vs host-gw
- [ ] Deploy a CNI (Calico or Cilium) on your kind cluster
- [ ] kube-proxy modes (iptables/ipvs); Service implementation detail
- [ ] DNS deep dive: CoreDNS config, custom records, ndots/resolv.conf
- [ ] **Drill:** trace a packet Pod-to-Pod and Pod-to-Service; document it

## Week 7 — Networking Deep Dive II
- [ ] Ingress controllers vs Gateway API (concepts)
- [ ] Advanced NetworkPolicies: egress, namespace selectors, DNS egress
- [ ] Service discovery patterns; headless services for StatefulSets
- [ ] Troubleshoot DNS and connectivity failures
- [ ] **Deliverable:** `labs/networking/` manifests + `NOTES.md`

## Week 8 — Helm I
- [ ] Helm architecture: charts, releases, repositories
- [ ] Create a chart from scratch: templates, values, `.helmignore`, helpers
- [ ] Templating: `_helpers.tpl`, named templates, `with`/`range`/`if`
- [ ] Package, lint, and install/uninstall; `helm template` vs `install`
- [ ] **Deliverable:** a chart for a simple web app

## Week 9 — Helm II
- [ ] Subcharts & dependencies; umbrella charts
- [ ] Chart hooks (pre/post-install/upgrade); tests (`helm test`)
- [ ] Versioning, packaging, signing (cosign/GP)
- [ ] Upgrade/rollback semantics; `--atomic`, `--wait`
- [ ] **Deliverable:** umbrella chart skeleton

## Week 10 — Kustomize
- [ ] Bases and overlays; `kustomization.yaml`
- [ ] Patches (strategic merge, JSON6902), image transformers, generators
- [ ] ConfigMap/Secret generators with hashing
- [ ] Kustomize vs Helm — when to use which
- [ ] **Deliverable:** dev/staging/prod overlays for the app

## Week 11 — Kubernetes Operators I
- [ ] Operator pattern, CRDs, controllers, reconciliation loop
- [ ] Install an existing operator (e.g., cert-manager or a DB operator)
- [ ] Understand CRDs and `kubectl get crd`, status/conditions
- [ ] **Deliverable:** operator installed + CR managed (documented)

## Week 12 — Kubernetes Operators II
- [ ] Build a tiny operator (Kubebuilder or Operator SDK) — Go or scaffold
- [ ] Watch/reconcile logic; status updates; finalizers
- [ ] Package & deploy the operator to your cluster
- [ ] **Deliverable:** `projects/operator-demo/` with a working reconcile

## Week 13 — Autoscaling & Troubleshooting
- [ ] HPA (metrics-server), VPA concepts, cluster autoscaler concepts
- [ ] KEDA event-driven scaling basics
- [ ] Troubleshooting toolkit: k9s, ephemeral containers, `kubectl debug`
- [ ] **Deliverable:** HPA demo + troubleshooting runbook

## Week 14 — Project Integration & Exit
- [ ] Assemble API + worker + DB into one Helm umbrella chart + Kustomize overlays
- [ ] Add probes, resources, HPA, Ingress, Config/Secrets
- [ ] Document architecture + deploy/rollback steps
- [ ] Deploy to dev/staging/prod overlays on your cluster
- [ ] **Deliverable:** `projects/helm-umbrella-app/` fully committed + README

---

## Exit Criteria
- [ ] Can package and ship a multi-service app with Helm + Kustomize
- [ ] Can explain Service/Ingress/DNS packet flows and CNI choices
- [ ] Built and deployed a minimal operator
- [ ] Umbrella chart deploys cleanly across three overlays
