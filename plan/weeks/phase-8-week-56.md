# Phase 8 · Week 56 — Governance & Policy at Scale

[← Back to Phase 8](../phase-8-openshift-acm.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Enforce configuration and security policy across the fleet.

## Topics
- [ ] Policy framework: `Policy`, configuration policy controller, inform vs enforce — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16) — [Docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html/governance)
- [ ] Placement & `PlacementDecision`: bind policies to clusters by labels/claims — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16) — [Docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html/governance)
- [ ] Policy Generator (Kustomize-based), policy sets, `OperatorPolicy` — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16) — [Docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html/governance)
- [ ] Prebuilt templates: CIS scan, etcd encryption, IAM, certs, Gatekeeper/OPA, Compliance Operator — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/security_and_compliance/compliance-operator)
- [ ] Governance dashboard, violations, policy test automation (`dryrun`) — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16) — [Docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html/governance)
- [ ] Lab: enforce a fleet-wide security baseline via GitOps — [Red Hat · DO432](https://www.redhat.com/en/services/training/do432-multicluster-management-red-hat-advanced-cluster-management-kubernetes) — [Docs](https://opengitops.dev/)

## Deliverable
- policy suite (informing + enforcing) applied via GitOps

## Exit check
- [ ] A non-compliant cluster is remediated by policy automatically — [Docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html/governance)

> Mark topics `[x]` as you finish them and commit this page to track progress.
