# Phase 5 · Week 37 — Logging with Loki I

[← Back to Phase 5](../phase-5-observability.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Deploy Loki and query logs.

## Topics
- [ ] Loki architecture (distributor/ingester/querier); labels vs content — [Pluralsight · Implementing the Kubernetes Observability Stack](https://www.pluralsight.com/courses/implementing-k8s-observability-stack) — [Pluralsight Lab · Kubernetes Metrics and Logging Stack](https://www.pluralsight.com/labs/aws/kubernetes-metrics-and-logging-stack-installation) — [KodeKloud · Grafana Loki](https://kodekloud.com/courses/grafana-loki) — [Video](https://www.youtube.com/watch?v=_hv4i84Z68s) — [Docs](https://grafana.com/docs/loki/latest/)
- [ ] Deploy Loki + Alloy/Promtail on K8s — [Pluralsight · Implementing the Kubernetes Observability Stack](https://www.pluralsight.com/courses/implementing-k8s-observability-stack) — [Pluralsight Lab · Kubernetes Metrics and Logging Stack](https://www.pluralsight.com/labs/aws/kubernetes-metrics-and-logging-stack-installation) — [KodeKloud · Grafana Loki](https://kodekloud.com/courses/grafana-loki) — [Video](https://www.youtube.com/watch?v=hAlQ1TV_-Vw) — [Docs](https://grafana.com/docs/loki/latest/clients/promtail/)
- [ ] LogQL basics and log pipelines — [Pluralsight · Implementing the Kubernetes Observability Stack](https://www.pluralsight.com/courses/implementing-k8s-observability-stack) — [Pluralsight Lab · Kubernetes Metrics and Logging Stack](https://www.pluralsight.com/labs/aws/kubernetes-metrics-and-logging-stack-installation) — [KodeKloud · Grafana Loki](https://kodekloud.com/courses/grafana-loki) — [Video](https://www.youtube.com/watch?v=57dQwcmqkpQ) — [Docs](https://grafana.com/docs/loki/latest/query/)
- [ ] **[OpenShift]** OpenShift Logging (LokiStack/Vector) vs legacy ClusterLogging — [Pluralsight · Managing Advanced Kubernetes Logging and Tracing](https://www.pluralsight.com/courses/managing-advanced-kubernetes-logging-tracing) — [Pluralsight Lab · Kubernetes Log Collectors](https://www.pluralsight.com/labs/aws/kubernetes-log-collectors-and-sample-application-deployment) — [OpenShift docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18) — [Video](https://www.youtube.com/watch?v=JFlhvMaQ96I) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/logging/index)

## Deliverable
- cluster + app logs queryable in Grafana

## Exit check
- [ ] Query app logs in Grafana via LogQL — [Docs](https://grafana.com/docs/grafana/latest/dashboards/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
