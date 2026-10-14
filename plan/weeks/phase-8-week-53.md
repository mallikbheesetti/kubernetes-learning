# Phase 8 · Week 53 — OpenShift for Developers, Networking & Storage

[← Back to Phase 8](../phase-8-openshift-acm.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Master OpenShift-native networking, builds and storage.

## Topics
- [ ] Networking: OVN-Kubernetes, Services, Routes vs Ingress, IngressController, MetalLB — [Pluralsight · Implementing Networking in OpenShift](https://www.pluralsight.com/courses/openshift-implementing-networking) — [Pluralsight Lab · Multi-Container Apps in OpenShift](https://www.pluralsight.com/labs/aws/setting-up-multi-container-applications-in-openshift) — [Red Hat · DO380](https://www.redhat.com/en/services/training/do380-red-hat-openshift-administration-iii-scaling-deployments-in-the-enterprise) — [Video](https://www.youtube.com/watch?v=HGTCGA0cpUg) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/networking_overview)
- [ ] Builds: BuildConfig / S2I, ImageStreams, `oc new-app`, triggers & webhooks — [Pluralsight · OpenShift Fundamentals and Workload Deployment](https://www.pluralsight.com/courses/openshift-fundamentals-workload-deployment) — [Pluralsight Lab · Deploying an App in OpenShift 4](https://www.pluralsight.com/labs/aws/configuring-and-deploying-an-application-using-git-in-openshift-4) — [KodeKloud · OpenShift 4](https://kodekloud.com/courses/openshift-4) — [Video](https://www.youtube.com/watch?v=2PAKw5PHyb4) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/building_applications)
- [ ] Config: ConfigMaps/Secrets, OpenShift Templates, Helm on OpenShift — [Pluralsight · OpenShift Fundamentals and Workload Deployment](https://www.pluralsight.com/courses/openshift-fundamentals-workload-deployment) — [Pluralsight Lab · Deploying an App in OpenShift 4](https://www.pluralsight.com/labs/aws/configuring-and-deploying-an-application-using-git-in-openshift-4) — [KodeKloud · OpenShift 4](https://kodekloud.com/courses/openshift-4) — [Video](https://www.youtube.com/watch?v=Ms-v2x6OyF0) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/building_applications)
- [ ] Storage: CSI, StorageClasses, dynamic provisioning, OpenShift Data Foundation (ODF) — [Pluralsight · Configuring and Managing Kubernetes Storage and Scheduling](https://www.pluralsight.com/courses/configuring-managing-kubernetes-storage-scheduling) — [Pluralsight Lab · Manage Storage in Kubernetes for CKA](https://www.pluralsight.com/labs/aws/manage-storage-in-kubernetes-for-cka) — [OpenShift docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18) — [Video](https://www.youtube.com/watch?v=4zNSCFeaTVk) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/index)
- [ ] Built-in GitOps & Pipelines: OpenShift GitOps (ArgoCD) + OpenShift Pipelines (Tekton) — [Pluralsight · Implementing GitOps for Kubernetes Applications](https://www.pluralsight.com/courses/implementing-gitops-kubernetes-apps) — [Pluralsight Lab · GitOps for Kubernetes Application Deployment](https://www.pluralsight.com/labs/aws/gitops-for-kubernetes-application-deployment) — [Video](https://www.youtube.com/watch?v=pOGMSOotSn0) — [Video 2](https://www.youtube.com/watch?v=aO6tLFqstQk) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/gitops)
- [ ] Service Mesh (Istio) & Serverless (Knative) overview — [Pluralsight · Managing Apps on Kubernetes with Istio](https://www.pluralsight.com/courses/istio-managing-apps-kubernetes) — [Pluralsight Lab · Istio in Kubernetes](https://www.pluralsight.com/labs/aws/istio-in-kubernetes) — [Video](https://www.youtube.com/watch?v=YoGR5zZGG9k) — [Video 2](https://www.youtube.com/watch?v=AR4fqwFLn9I) — [Docs](https://istio.io/latest/docs/)

## Deliverable
- app built via S2I, exposed via Route, config + PVC

## Exit check
- [ ] Build/expose a service and deploy it with OpenShift GitOps — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/gitops)

> Mark topics `[x]` as you finish them and commit this page to track progress.
