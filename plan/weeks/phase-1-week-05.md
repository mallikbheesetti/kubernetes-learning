# Phase 1 · Week 5 — Internals, Backup & Cold Mock CKA

[← Back to Phase 1](../phase-1-kubernetes-revision.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Refresh cluster internals, etcd backup, and validate with a timed mock.

## Topics
- [ ] Control-plane internals; kubeconfig/authn/authz (RBAC quick pass) — [Pluralsight · CKA: Securing Access with RBAC and Admission Controls](https://www.pluralsight.com/courses/cka-securing-access-with-rbac-and-admission-controls) — [Pluralsight Lab · Kubernetes Security and RBAC for CKA](https://www.pluralsight.com/labs/aws/manage-kubernetes-security-and-rbac-for-cka) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=bhVMSSWJL6s) — [Docs](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
- [ ] etcd: snapshot, restore; certificates overview — [Pluralsight · CKA: Managing Cluster Lifecycle and Upgrades](https://www.pluralsight.com/courses/cka-kubernetes-managing-cluster-lifecycle-upgrades) — [Pluralsight Lab · Cluster Maintenance and Troubleshooting](https://www.pluralsight.com/labs/aws/perform-cluster-maintenance-and-troubleshooting-for-cka) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=R2wuFCYgnm4) — [Docs](https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/)
- [ ] Cluster upgrade concepts (kubeadm) — [Pluralsight · CKA: Managing Cluster Lifecycle and Upgrades](https://www.pluralsight.com/courses/cka-kubernetes-managing-cluster-lifecycle-upgrades) — [Pluralsight Lab · Cluster Maintenance and Troubleshooting](https://www.pluralsight.com/labs/aws/perform-cluster-maintenance-and-troubleshooting-for-cka) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=fB0P0mSgRdg) — [Lab](https://notes.kodekloud.com/docs/Certified-Kubernetes-Administrator-CKA/Cluster-Maintenance/Solution-Cluster-Upgrade-Process/page) — [Docs](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [ ] Nodes: kubelet config, container runtime, static pod manifests — [Pluralsight · Kubernetes Installation and Configuration Fundamentals](https://www.pluralsight.com/courses/kubernetes-installation-configuration-fundamentals) — [Pluralsight Lab · Kubernetes API Server and Pods](https://www.pluralsight.com/labs/aws/manage-the-kubernetes-api-server-and-pods) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=g3M0UVNBnQ4) — [Lab](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) — [Docs](https://kubernetes.io/docs/concepts/overview/components/)
- [ ] Cold timed mock CKA-style set (2 hrs), no notes — [Pluralsight · CKA: Kubernetes Foundations](https://www.pluralsight.com/courses/cka-kubernetes-foundations) — [Pluralsight Lab · CKA Practice Exam](https://www.pluralsight.com/labs/aws/certified-kubernetes-administrator-cka-practice-exam-part-4) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka)

## Deliverable
- projects/k8s-bootstrap/ bootstrap script + RUNBOOK.md

## Exit check
- [ ] Timed mock completed cold at pass-equivalent score

> Mark topics `[x]` as you finish them and commit this page to track progress.
