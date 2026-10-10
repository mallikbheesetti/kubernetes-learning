# Phase 8 · Week 56 — Governance & Policy at Scale

[← Back to Phase 8](../phase-8-openshift-acm.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Enforce configuration and security policy across the fleet.

## Topics
- [ ] Policy framework: `Policy`, configuration policy controller, inform vs enforce — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Placement & `PlacementDecision`: bind policies to clusters by labels/claims — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Policy Generator (Kustomize-based), policy sets, `OperatorPolicy` — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Prebuilt templates: CIS scan, etcd encryption, IAM, certs, Gatekeeper/OPA, Compliance Operator — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Governance dashboard, violations, policy test automation (`dryrun`) — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Lab: enforce a fleet-wide security baseline via GitOps — [Red Hat · DO432](https://www.redhat.com/en/services/training/do432-multicluster-management-red-hat-advanced-cluster-management-kubernetes)

## Deliverable
- policy suite (informing + enforcing) applied via GitOps

## Exit check
- [ ] A non-compliant cluster is remediated by policy automatically

> Mark topics `[x]` as you finish them and commit this page to track progress.
