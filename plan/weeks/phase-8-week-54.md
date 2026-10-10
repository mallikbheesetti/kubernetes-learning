# Phase 8 · Week 54 — RHACM Foundations: Hub & Managed Clusters

[← Back to Phase 8](../phase-8-openshift-acm.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Stand up an RHACM hub and bring clusters under management.

## Topics
- [ ] Multicluster architecture: hub, managed clusters, Klusterlet; MCE vs RHACM — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Install RHACM: MultiClusterEngine + MultiClusterHub; sizing the hub — [Red Hat · DO432](https://www.redhat.com/en/services/training/do432-multicluster-management-red-hat-advanced-cluster-management-kubernetes)
- [ ] Provision/import clusters: `ManagedCluster`, `KlusterletAddonConfig` (console & CLI) — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Cluster sets (`ManagedClusterSet`) & cluster pools; hibernation/resume — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Fleet RBAC & search: `ClusterPermission`, `MulticlusterRoleAssignment`, search add-on — [RHACM docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16)
- [ ] Lab: hub + 2 managed clusters under RHACM — [Red Hat · DO432](https://www.redhat.com/en/services/training/do432-multicluster-management-red-hat-advanced-cluster-management-kubernetes)

## Deliverable
- RHACM hub managing 2+ clusters (documented import)

## Exit check
- [ ] Import a cluster, search it, and grant fleet-scoped RBAC

> Mark topics `[x]` as you finish them and commit this page to track progress.
