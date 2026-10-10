# Phase 8 — OpenShift: Advanced Cluster Management (Weeks 51–58)

**Why:** OpenShift is the enterprise Kubernetes distribution, and your target is **advanced cluster management** — running and governing a fleet of clusters, not a single one. This phase covers OpenShift day-2 operations at scale and Red Hat Advanced Cluster Management for Kubernetes (RHACM): hub/spoke lifecycle, policy governance, multicluster observability, GitOps delivery and disaster recovery.

**Deliverable:** `projects/openshift-fleet/` — an RHACM hub managing multiple clusters (OpenShift Local/SNO + a cloud cluster) with declarative provisioning, GitOps app delivery, fleet-wide policy governance, multicluster observability and a fleet operations runbook.

**Resources:** KodeKloud *OpenShift 4*; Red Hat *DO280* (OCP Admin II), *DO380* (OCP Admin III: Scaling Deployments), *DO432* (Multicluster Management with RHACM); OpenShift and RHACM documentation. Optional checkpoint: *EX432* (OpenShift Advanced Cluster Management).

---

<!-- PROGRESS:START -->
## Progress

**OpenShift: Advanced Cluster Management** — **0 / 55** tasks complete (**0%**)

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥

| Week / Module | Tasks | Progress |
| --- | --- | --- |
| Week 51 — OpenShift Foundations & Architecture | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 52 — OpenShift Day-2 Operations & Upgrades | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 53 — OpenShift for Developers, Networking & Storage | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 54 — RHACM Foundations: Hub & Managed Clusters | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 55 — Fleet Provisioning & Lifecycle at Scale | 0 / 6 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 56 — Governance & Policy at Scale | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 57 — Multicluster Observability, App Lifecycle & DR | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |
| Week 58 — Advanced Fleet Operations, Scale & Capstone Exit | 0 / 7 | 🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥 0% |

_Auto-generated from ticked checkboxes — see the phase checklists below. Updated by [`scripts/update_progress.py`](../scripts/update_progress.py)._
<!-- PROGRESS:END -->

## Week Pages
- [Week 51 — OpenShift Foundations & Architecture](weeks/phase-8-week-51.md)
- [Week 52 — OpenShift Day-2 Operations & Upgrades](weeks/phase-8-week-52.md)
- [Week 53 — OpenShift for Developers, Networking & Storage](weeks/phase-8-week-53.md)
- [Week 54 — RHACM Foundations: Hub & Managed Clusters](weeks/phase-8-week-54.md)
- [Week 55 — Fleet Provisioning & Lifecycle at Scale](weeks/phase-8-week-55.md)
- [Week 56 — Governance & Policy at Scale](weeks/phase-8-week-56.md)
- [Week 57 — Multicluster Observability, App Lifecycle & DR](weeks/phase-8-week-57.md)
- [Week 58 — Advanced Fleet Operations, Scale & Capstone Exit](weeks/phase-8-week-58.md)

## Week 51 — OpenShift Foundations & Architecture
- [ ] From Kubernetes to OpenShift: OCP architecture, `oc` vs `kubectl`
- [ ] Cluster Version Operator (CVO) & ClusterOperators: the OpenShift operator model
- [ ] Machine Config Operator (MCO): MachineConfig, MachineConfigPool (master/worker)
- [ ] Projects, users, groups, OAuth basics; default Security Context Constraints
- [ ] Stand up a cluster: OpenShift Local (CRC), Single Node OpenShift (SNO), or cloud (ROSA/ARO)
- [ ] Console + `oc` day-1 tour; deploy and expose a sample app
- [ ] **Deliverable:** a running OpenShift cluster (CRC/SNO/cloud) + first app

## Week 52 — OpenShift Day-2 Operations & Upgrades
- [ ] OLM: OperatorHub, `Subscription`, `ClusterServiceVersion`, `InstallPlan`, catalogs
- [ ] Node & compute: MachineSets, scaling, labels/taints, dedicated node pools
- [ ] Upgrades: release channels (stable/fast/EUS), ClusterVersion, upgrade control & pausing
- [ ] Certificates, etcd backup, cluster-operator degradation, `oc adm` day-2 tasks
- [ ] Troubleshooting: `oc get clusteroperators`, `must-gather`, `oc debug node`
- [ ] Disconnected / air-gapped installs & mirrored registries (concepts)
- [ ] **Deliverable:** upgrade path notes + a cluster-operator / must-gather runbook

## Week 53 — OpenShift for Developers, Networking & Storage
- [ ] Networking: OVN-Kubernetes, Services, Routes vs Ingress, IngressController, MetalLB
- [ ] Builds: BuildConfig / S2I, ImageStreams, `oc new-app`, triggers & webhooks
- [ ] Config: ConfigMaps/Secrets, OpenShift Templates, Helm on OpenShift
- [ ] Storage: CSI, StorageClasses, dynamic provisioning, OpenShift Data Foundation (ODF)
- [ ] Built-in GitOps & Pipelines: OpenShift GitOps (ArgoCD) + OpenShift Pipelines (Tekton)
- [ ] Service Mesh (Istio) & Serverless (Knative) overview
- [ ] **Deliverable:** app built via S2I, exposed via Route, config + PVC

## Week 54 — RHACM Foundations: Hub & Managed Clusters
- [ ] Multicluster architecture: hub, managed clusters, Klusterlet; MCE vs RHACM
- [ ] Install RHACM: MultiClusterEngine + MultiClusterHub; sizing the hub
- [ ] Provision/import clusters: `ManagedCluster`, `KlusterletAddonConfig` (console & CLI)
- [ ] Cluster sets (`ManagedClusterSet`) & cluster pools; hibernation/resume
- [ ] Fleet RBAC & search: `ClusterPermission`, `MulticlusterRoleAssignment`, search add-on
- [ ] Lab: hub + 2 managed clusters under RHACM
- [ ] **Deliverable:** RHACM hub managing 2+ clusters (documented import)

## Week 55 — Fleet Provisioning & Lifecycle at Scale
- [ ] Declarative provisioning: Hive (`ClusterDeployment`) for OpenShift clusters
- [ ] Assisted Installer & Single Node OpenShift for edge; zero-touch provisioning (ZTP)
- [ ] Hosted Control Planes (HyperShift): hosted clusters on a management cluster
- [ ] Cloud lifecycle at scale: ROSA / ARO / OSD create-upgrade-destroy via RHACM
- [ ] GitOps-driven cluster lifecycle: `ClusterInstance` via ApplicationSet
- [ ] **Deliverable:** a declaratively provisioned cluster (Hive/HCP/Assisted)

## Week 56 — Governance & Policy at Scale
- [ ] Policy framework: `Policy`, configuration policy controller, inform vs enforce
- [ ] Placement & `PlacementDecision`: bind policies to clusters by labels/claims
- [ ] Policy Generator (Kustomize-based), policy sets, `OperatorPolicy`
- [ ] Prebuilt templates: CIS scan, etcd encryption, IAM, certs, Gatekeeper/OPA, Compliance Operator
- [ ] Governance dashboard, violations, policy test automation (`dryrun`)
- [ ] Lab: enforce a fleet-wide security baseline via GitOps
- [ ] **Deliverable:** policy suite (informing + enforcing) applied via GitOps

## Week 57 — Multicluster Observability, App Lifecycle & DR
- [ ] RHACM observability (Thanos) on the hub; multicluster dashboards & alert forwarding
- [ ] Multicluster app delivery: Subscription / ApplicationSet / ArgoCD add-on, placement
- [ ] Submariner: cross-cluster networking & service discovery; Globalnet
- [ ] Backup & DR: OADP (Velero), ODF Regional-DR (async) & Metro-DR (sync)
- [ ] OpenShift Virtualization across the fleet: snapshots, cross-cluster live migration
- [ ] Lab: deliver the app to all clusters + fleet dashboard + DR drill
- [ ] **Deliverable:** fleet observability + DR drill evidence

## Week 58 — Advanced Fleet Operations, Scale & Capstone Exit
- [ ] Global Hub: managed cluster migration, hub upgrade without disruption
- [ ] Scale, capacity & cost: one hub to thousands of clusters; right-sizing recommendations
- [ ] Fleet security hardening: RHACS, compliance, policy-as-code integration
- [ ] Disconnected / edge fleet operations across low-bandwidth sites
- [ ] Optional checkpoint: EX432 (OpenShift Advanced Cluster Management) style mock
- [ ] Capstone: document fleet architecture + runbook in `projects/openshift-fleet/`
- [ ] **Deliverable:** projects/openshift-fleet/ + fleet operations runbook

---

## Exit Criteria
- [ ] Run an RHACM hub managing 2+ clusters with declarative provisioning
- [ ] Fleet-wide governance policy enforced (inform + enforce) via GitOps
- [ ] Multicluster observability dashboard + app delivered to all clusters
- [ ] Backup/restore (OADP) + a DR drill demonstrated
- [ ] Fleet architecture + operations runbook committed in `projects/openshift-fleet/`

