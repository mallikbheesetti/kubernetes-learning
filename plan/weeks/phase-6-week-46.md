# Phase 6 · Week 46 — Cluster Hardening & Pod Security

[← Back to Phase 6](../phase-6-security.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Harden the cluster and workloads.

## Topics
- [ ] API server/etcd/kubelet hardening flags; CIS benchmark scan (kube-bench) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Docs](https://github.com/aquasecurity/kube-bench)
- [ ] Pod Security Admission (baseline/restricted); securityContext — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Docs](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [ ] seccomp, AppArmor/SELinux, capability dropping, read-only FS — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Docs](https://kubernetes.io/docs/concepts/security/)
- [ ] **[OpenShift]** Security Context Constraints (SCC) & default service accounts — [KodeKloud · OpenShift 4](https://kodekloud.com/courses/openshift-4) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/index)

## Deliverable
- restricted-namespace enforcement demonstration

## Exit check
- [ ] Restricted PSS enforced; hardening flags reviewed — [Docs](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
