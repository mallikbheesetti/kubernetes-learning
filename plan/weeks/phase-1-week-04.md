# Phase 1 · Week 4 — Scheduling, Storage & Troubleshooting

[← Back to Phase 1](../phase-1-kubernetes-revision.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Control placement, persist data, and debug failures confidently.

## Topics
- [ ] Scheduling: node selectors, affinity/anti-affinity, taints/tolerations — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=MPx5EID8nkY) — [Video 2](https://www.youtube.com/watch?v=vaW2pwSXdb4) — [Lab](https://kubernetes-tutorial.schoolofdevops.com/advanced_pod_scheduling/) — [Docs](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [ ] Manual scheduling, cordon/drain, static pods — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=6eGf7_VSbrQ) — [Video 2](https://www.youtube.com/watch?v=jfRxw5-Gdq8) — [Docs](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
- [ ] Volumes: emptyDir, hostPath, PV/PVC, StorageClasses; dynamic provisioning — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=0swOh5C3OVM) — [Docs](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [ ] StatefulSet + PVC backed by a local storage class — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=pPQKAR1pA9U) — [Lab](https://runbook.academy/courses/kubernetes/labs/kubernetes-lab-19-statefulset/) — [Docs](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [ ] Troubleshooting: describe, logs, exec, events, ImagePull/Pending/CrashLoop — [KodeKloud · K8s Troubleshooting for App Developers](https://kodekloud.com/courses/kubernetes-troubleshooting-for-application-developers) — [Video](https://www.youtube.com/watch?v=uIYIreo2Pu4) — [Docs](https://kubernetes.io/docs/tasks/debug/debug-application/)

## Deliverable
- labs/troubleshooting/RUNBOOK.md (5 broken deployments fixed)

## Exit check
- [ ] Break a deployment 5 ways and fix each — [Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
