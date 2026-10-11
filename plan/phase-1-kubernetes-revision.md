# Phase 1 — Kubernetes Revision & Re-Fluency (Weeks 1–5)

**Why:** CKA held, but hands-on Kubernetes was ~2 years ago. Rebuild muscle memory
before going deep. Treat this as a *refresh*, not first-time learning.

**Deliverable:** An automated, re-runnable cluster bootstrap (kind/k3d) + runbook in `projects/k8s-bootstrap/`.

**Resources:** KodeKloud *Kubernetes for the Absolute Beginners*, CKA course labs,
`kubectl` docs, Killer Coda / killercoda playgrounds.

---

<!-- PROGRESS:START -->
## Progress

**Kubernetes Revision & Re-Fluency** — **1 / 33** tasks complete (**3%**)

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥

| Week / Module | Tasks | Progress |
| --- | --- | --- |
| Week 1 — Environment + Fundamentals Refresh | 1 / 7 | 🟩🟥🟥🟥🟥🟥🟥🟥🟥🟥 14% |
| Week 2 — Workloads & Controllers | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 3 — Networking, Services & Config | 0 / 6 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 4 — Scheduling, Storage & Troubleshooting | 0 / 6 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 5 — Internals, Backup & Cold Mock CKA | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |

_Auto-generated from ticked checkboxes — see the phase checklists below. Updated by [`scripts/update_progress.py`](../scripts/update_progress.py)._
<!-- PROGRESS:END -->

## Week Pages
- [Week 1 — Environment + Fundamentals Refresh](weeks/phase-1-week-01.md)
- [Week 2 — Workloads & Controllers](weeks/phase-1-week-02.md)
- [Week 3 — Networking, Services & Config](weeks/phase-1-week-03.md)
- [Week 4 — Scheduling, Storage & Troubleshooting](weeks/phase-1-week-04.md)
- [Week 5 — Internals, Backup & Cold Mock CKA](weeks/phase-1-week-05.md)

> Each week page lists its topics with primary **KodeKloud** course links (YouTube search as fallback) plus that week's deliverable and exit check.

## Week 1 — Environment + Fundamentals Refresh
- [x] Install `kubectl`, `kind`, `k3d`, `k9s`, `helm`; set up aliases + shell completion
- [ ] Spin up a local multi-node cluster (1 control-plane + 2 workers) with kind
- [ ] Review cluster architecture: control plane components, kubelet, kube-proxy, CNI
- [ ] Namespaces, contexts, `kubectl config`, `--dry-run=client -o yaml` workflow
- [ ] Declarative vs imperative: create manifests with `kubectl apply -f`
- [ ] **Deliverable:** `projects/k8s-bootstrap/kind-config.yaml` committed
- [ ] Notes: capture 10 most-used `kubectl` commands in `NOTES.md`

## Week 2 — Workloads & Controllers
- [ ] Pods: lifecycle, init containers, sidecars, probes (liveness/readiness/startup)
- [ ] ReplicaSets, Deployments, rolling updates & rollbacks
- [ ] DaemonSets, StatefulSets (headless services, stable identity)
- [ ] Jobs & CronJobs; parallel/completion semantics
- [ ] Resource requests/limits, QoS classes
- [ ] **Drill:** deploy a 3-replica app, perform a rolling update, roll back — from memory
- [ ] Notes: probe types and when to use each

## Week 3 — Networking, Services & Config
- [ ] Cluster networking model; Pod-to-Pod; DNS (CoreDNS)
- [ ] Services: ClusterIP, NodePort, LoadBalancer, headless
- [ ] Ingress basics; Ingress controllers (nginx)
- [ ] ConfigMaps & Secrets (incl. mounting, env, immutable)
- [ ] NetworkPolicy basics (default deny, allow rules)
- [ ] **Drill:** expose an app via Service + Ingress; inject config via ConfigMap/Secret

## Week 4 — Scheduling, Storage & Troubleshooting
- [ ] Scheduling: node selectors, affinity/anti-affinity, taints/tolerations
- [ ] Manual scheduling, cordon/drain, static pods
- [ ] Volumes: emptyDir, hostPath, PV/PVC, StorageClasses; dynamic provisioning
- [ ] StatefulSet + PVC backed by a local storage class
- [ ] Troubleshooting: `describe`, `logs`, `exec`, `events`, ImagePull/Pending/CrashLoop
- [ ] **Drill:** break a deployment 5 ways and fix each (write a runbook)

## Week 5 — Internals, Backup & Cold Mock CKA
- [ ] Control-plane internals; kubeconfig/authn/authz (RBAC quick pass)
- [ ] etcd: snapshot, restore; certificates overview
- [ ] Cluster upgrade concepts (kubeadm)
- [ ] Nodes: kubelet config, container runtime, static pod manifests
- [ ] **Cold timed mock:** complete a CKA-style killer.sh/killercoda set (2 hrs) without notes
- [ ] **Deliverable:** `projects/k8s-bootstrap/` bootstrap script + `RUNBOOK.md`
- [ ] Self-score the mock; log weak areas into Phase 2 backlog

---

## Exit Criteria (do not advance until met)
- [ ] Can bootstrap a cluster and deploy a full app (Deployment+Service+Ingress+Config) from memory in <30 min
- [ ] Timed CKA-style mock completed cold with pass-equivalent score
- [ ] Bootstrap project committed and re-runnable from scratch
