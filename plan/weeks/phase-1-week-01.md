# Phase 1 · Week 1 — Environment + Fundamentals Refresh

[← Back to Phase 1](../phase-1-kubernetes-revision.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Set up your tooling and refresh core Kubernetes architecture.

## Topics
- [ ] Install kubectl, kind, k3d, k9s, helm; aliases + shell completion — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Docs](https://kubernetes.io/docs/tasks/tools/)
- [ ] Spin up a local multi-node cluster (1 control-plane + 2 workers) with kind — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Docs](https://kind.sigs.k8s.io/docs/)
- [ ] Review cluster architecture: control plane components, kubelet, kube-proxy, CNI — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Docs](https://kubernetes.io/docs/concepts/overview/components/)
- [ ] Namespaces, contexts, kubectl config, --dry-run=client -o yaml workflow — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Docs](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
- [ ] Declarative vs imperative: create manifests with kubectl apply — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Docs](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)

## Deliverable
- projects/k8s-bootstrap/kind-config.yaml committed

## Exit check
- [ ] Local multi-node cluster is up and you can deploy a Pod

> Mark topics `[x]` as you finish them and commit this page to track progress.
