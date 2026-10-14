# Phase 1 · Week 2 — Workloads & Controllers

[← Back to Phase 1](../phase-1-kubernetes-revision.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Remaster every core workload primitive and controller.

## Topics
- [ ] Pods: lifecycle, init containers, sidecars, probes (liveness/readiness/startup) — [Pluralsight · Getting Started with Kubernetes](https://www.pluralsight.com/courses/kubernetes-getting-started-2023) — [Pluralsight Lab · Configure a Multi-container Pod](https://www.pluralsight.com/labs/aws/configure-a-multi-container-pod-with-kubernetes) — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Video](https://www.youtube.com/watch?v=yRiFq1ykBxc) — [Docs](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- [ ] ReplicaSets, Deployments, rolling updates & rollbacks — [Pluralsight · Managing Kubernetes Controllers and Deployments](https://www.pluralsight.com/courses/managing-kubernetes-controllers-deployments) — [Pluralsight Lab · Manage Controllers and Deployments](https://www.pluralsight.com/labs/aws/manage-kubernetes-controllers-and-deployments) — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Video](https://www.youtube.com/watch?v=4k_Zsf-b90Y) — [Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [ ] DaemonSets, StatefulSets (headless services, stable identity) — [Pluralsight · Deploying Stateful Applications in Kubernetes](https://www.pluralsight.com/courses/kubernetes-deploying-stateful-applications) — [Pluralsight Lab · Manage Controllers and Deployments](https://www.pluralsight.com/labs/aws/manage-kubernetes-controllers-and-deployments) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=RGSeeN-o-kQ) — [Video 2](https://www.youtube.com/watch?v=pPQKAR1pA9U) — [Docs](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
- [ ] Jobs & CronJobs; parallel/completion semantics — [Pluralsight · Managing Kubernetes Controllers and Deployments](https://www.pluralsight.com/courses/managing-kubernetes-controllers-deployments) — [Pluralsight Lab · Manage Controllers and Deployments](https://www.pluralsight.com/labs/aws/manage-kubernetes-controllers-and-deployments) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=jWD1B5Ynh_8) — [Docs](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [ ] Resource requests/limits, QoS classes — [Pluralsight · Configuring and Managing Kubernetes Storage and Scheduling](https://www.pluralsight.com/courses/configuring-managing-kubernetes-storage-scheduling) — [Pluralsight Lab · Storage and Scheduling](https://www.pluralsight.com/labs/aws/configure-and-manage-kubernetes-storage-and-scheduling) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=DLVmhu1lFmI) — [Docs](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)

## Deliverable
- Drill notes in labs/workloads/NOTES.md

## Exit check
- [ ] Perform a rolling update and rollback from memory — [Docs](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
