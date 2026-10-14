# Phase 6 · Week 48 — Runtime Security & Monitoring

[← Back to Phase 6](../phase-6-security.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Detect and audit runtime threats.

## Topics
- [ ] Threat model; runtime detection (Falco) concepts + deploy — [Pluralsight · Monitoring, Logging and Runtime Security for CKS](https://www.pluralsight.com/courses/monitoring-logging-runtime-security-cks-cert) — [Pluralsight Lab · Threat Detection with Falco](https://www.pluralsight.com/labs/aws/threat-detection-in-kubernetes-with-falco) — [Video](https://www.youtube.com/watch?v=C8ephsD1_fM) — [Video 2](https://www.youtube.com/watch?v=058aWCXQ3dE) — [Docs](https://falco.org/docs/)
- [ ] Audit logging (API server audit policy) — [Pluralsight · Kubernetes System Hardening](https://www.pluralsight.com/courses/kubernetes-system-hardening) — [Pluralsight Lab · Configure Audit Logging in Kubernetes](https://www.pluralsight.com/labs/aws/configure-audit-logging-in-kubernetes) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=EnK1P0jYx7A) — [Video 2](https://www.youtube.com/watch?v=raJRLmGb9Is) — [Docs](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)
- [ ] Secrets: encryption at rest; external secrets; Vault integration — [Pluralsight · Getting Started with HashiCorp Vault](https://www.pluralsight.com/courses/getting-started-hashicorp-vault) — [Pluralsight Lab · Write and Test a Vault Policy](https://www.pluralsight.com/labs/aws/write-and-test-a-hashicorp-vault-policy) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=CF6ARIXdA4A) — [Video 2](https://www.youtube.com/watch?v=RQPz4YlmsCs) — [Docs](https://developer.hashicorp.com/vault/docs)
- [ ] **[OpenShift]** OpenShift OAuth/identity providers, Compliance Operator, RHACS — [Pluralsight · Securing an OpenShift Cluster](https://www.pluralsight.com/courses/openshift-cluster-securing) — [Pluralsight Lab · Configure Audit Logging in Kubernetes](https://www.pluralsight.com/labs/aws/configure-audit-logging-in-kubernetes) — [Video](https://www.youtube.com/watch?v=eFxFtUpAT9s) — [Video 2](https://www.youtube.com/watch?v=_eiEjyprKHg) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/security_and_compliance/compliance-operator)

## Deliverable
- Falco rules + audit policy + Vault secrets injection

## Exit check
- [ ] Falco alerts on a simulated runtime event — [Docs](https://falco.org/docs/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
