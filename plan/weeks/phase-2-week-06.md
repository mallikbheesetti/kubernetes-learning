# Phase 2 · Week 6 — Networking Deep Dive I

[← Back to Phase 2](../phase-2-kubernetes-depth.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Go under the hood of CNI, kube-proxy and DNS.

## Topics
- [ ] CNI fundamentals: plugin model, pod IP allocation, VXLAN vs host-gw — [KodeKloud · Kubernetes Networking Deep Dive](https://kodekloud.com/courses/kubernetes-networking) — [Docs](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [ ] Deploy a CNI (Calico or Cilium) on your kind cluster — [KodeKloud · Kubernetes Networking Deep Dive](https://kodekloud.com/courses/kubernetes-networking) — [Docs](https://docs.tigera.io/calico/latest)
- [ ] kube-proxy modes (iptables/ipvs); Service implementation detail — [KodeKloud · Kubernetes Networking Deep Dive](https://kodekloud.com/courses/kubernetes-networking) — [Docs](https://kubernetes.io/docs/reference/networking/virtual-ips)
- [ ] DNS deep dive: CoreDNS config, custom records, ndots/resolv.conf — [KodeKloud · Kubernetes Networking Deep Dive](https://kodekloud.com/courses/kubernetes-networking) — [Docs](https://coredns.io/manual/toc/)

## Deliverable
- labs/networking/ + packet-flow notes

## Exit check
- [ ] Trace a packet Pod-to-Pod and Pod-to-Service and document it — [Docs](https://kubernetes.io/docs/concepts/cluster-administration/networking/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
