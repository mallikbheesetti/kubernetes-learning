# Phase 2 · Week 7 — Networking Deep Dive II

[← Back to Phase 2](../phase-2-kubernetes-depth.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Master Ingress/Gateway, advanced policies and service discovery.

## Topics
- [ ] Ingress controllers vs Gateway API (concepts) — [Pluralsight · Managing Ingress Traffic Patterns for Kubernetes Services](https://www.pluralsight.com/courses/managing-ingress-traffic-patterns-kubernetes-services) — [Pluralsight Lab · Expose an App with Services and Ingress](https://www.pluralsight.com/labs/aws/exposing-a-kubernetes-application-with-services-and-ingress) — [KodeKloud · Kubernetes Networking Deep Dive](https://kodekloud.com/courses/kubernetes-networking) — [Video](https://www.youtube.com/watch?v=xaZ87iSvMAI) — [Video 2](https://www.youtube.com/watch?v=GhIrz-V9X6k) — [Docs](https://gateway-api.sigs.k8s.io/)
- [ ] Advanced NetworkPolicies: egress, namespace selectors, DNS egress — [Pluralsight · Configuring and Managing Kubernetes Networking, Services, and Ingress](https://www.pluralsight.com/courses/configuring-managing-kubernetes-networking-services-ingress) — [Pluralsight Lab · Lock Down Inter-Pod Traffic](https://www.pluralsight.com/labs/aws/lock-down-inter-pod-communication-with-networkpolicies) — [KodeKloud · Kubernetes Networking Deep Dive](https://kodekloud.com/courses/kubernetes-networking) — [Video](https://www.youtube.com/watch?v=eVtnevr3Rao) — [Video 2](https://www.youtube.com/watch?v=5TKKG-uKU4o) — [Docs](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [ ] Service discovery patterns; headless services for StatefulSets — [Pluralsight · Monitoring Key Systems with Prometheus Exporters](https://www.pluralsight.com/courses/monitoring-key-systems-prometheus-exporters) — [Pluralsight Lab · Linux Metrics with Prometheus](https://www.pluralsight.com/labs/aws/collecting-linux-server-metrics-with-prometheus) — [KodeKloud · Kubernetes Networking Deep Dive](https://kodekloud.com/courses/kubernetes-networking) — [Video](https://www.youtube.com/watch?v=NOjCunqu3VA) — [Video 2](https://www.youtube.com/watch?v=Vrxr-7rjkvM) — [Docs](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
- [ ] Troubleshoot DNS and connectivity failures — [Pluralsight · Hands-On Kubernetes Troubleshooting](https://www.pluralsight.com/courses/hands-on-kubernetes-troubleshooting) — [Pluralsight Lab · Repairing Failed Pods](https://www.pluralsight.com/labs/aws/repairing-failed-pods-in-kubernetes) — [KodeKloud · K8s Troubleshooting for App Developers](https://kodekloud.com/courses/kubernetes-troubleshooting-for-application-developers) — [Video](https://www.youtube.com/watch?v=920BZXvQpVs) — [Docs](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- [ ] **[OpenShift]** Routes & the default IngressController (`oc expose`, `oc create route`) — [Pluralsight · Implementing Networking in OpenShift](https://www.pluralsight.com/courses/openshift-implementing-networking) — [Pluralsight Lab · Multi-Container Apps in OpenShift](https://www.pluralsight.com/labs/aws/setting-up-multi-container-applications-in-openshift) — [KodeKloud · OpenShift 4](https://kodekloud.com/courses/openshift-4) — [Video](https://www.youtube.com/watch?v=Vo8XmDNCZKE) — [Video 2](https://www.youtube.com/watch?v=HGTCGA0cpUg) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/networking_overview)

## Deliverable
- labs/networking/ advanced manifests + NOTES.md

## Exit check
- [ ] Diagnose and fix an injected DNS/connectivity failure — [Docs](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
