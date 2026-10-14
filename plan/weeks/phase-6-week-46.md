# Phase 6 · Week 46 — Cluster Hardening & Pod Security

[← Back to Phase 6](../phase-6-security.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Harden the cluster and workloads.

## Topics
- [ ] API server/etcd/kubelet hardening flags; CIS benchmark scan (kube-bench) — [Pluralsight · Kubernetes System Hardening](https://www.pluralsight.com/courses/kubernetes-system-hardening) — [Pluralsight Lab · Configure Audit Logging in Kubernetes](https://www.pluralsight.com/labs/aws/configure-audit-logging-in-kubernetes) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=yt5KuYjMPvg) — [Video 2](https://www.youtube.com/watch?v=s6nZ_6XSQVQ) — [Docs](https://github.com/aquasecurity/kube-bench)
- [ ] Pod Security Admission (baseline/restricted); securityContext — [Pluralsight · Configuring and Managing Kubernetes Security](https://www.pluralsight.com/courses/configuring-managing-kubernetes-security-2) — [Pluralsight Lab · Pod Security Policy](https://www.pluralsight.com/labs/aws/kubernetes-with-kops-for-podsecuritypolicy-lab) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=bSXi2wF-FKY) — [Docs](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
- [ ] seccomp, AppArmor/SELinux, capability dropping, read-only FS — [Pluralsight · Configuring and Managing Kubernetes Security](https://www.pluralsight.com/courses/configuring-managing-kubernetes-security-2) — [Pluralsight Lab · Pod Security Policy](https://www.pluralsight.com/labs/aws/kubernetes-with-kops-for-podsecuritypolicy-lab) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=OxkMFSKiZYE) — [Video 2](https://www.youtube.com/watch?v=in_P293aXV0) — [Docs](https://kubernetes.io/docs/concepts/security/)
- [ ] **[OpenShift]** Security Context Constraints (SCC) & default service accounts — [Pluralsight · Securing an OpenShift Cluster](https://www.pluralsight.com/courses/openshift-cluster-securing) — [Pluralsight Lab · Getting Acquainted with OpenShift](https://www.pluralsight.com/labs/aws/getting-acquainted-with-openshift) — [KodeKloud · OpenShift 4](https://kodekloud.com/courses/openshift-4) — [Video](https://www.youtube.com/watch?v=VtIxFh6cO0Q) — [Video 2](https://www.youtube.com/watch?v=0sUlF617BOQ) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/authentication_and_authorization/index)

## Deliverable
- restricted-namespace enforcement demonstration

## Exit check
- [ ] Restricted PSS enforced; hardening flags reviewed — [Docs](https://kubernetes.io/docs/concepts/security/pod-security-standards/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
