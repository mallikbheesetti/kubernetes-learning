# Phase 5 · Week 33 — Metrics Fundamentals & Prometheus I

[← Back to Phase 5](../phase-5-observability.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Stand up Prometheus and scrape your app.

## Topics
- [ ] Observability 3 pillars; metrics types (counter/gauge/histogram/summary) — [Pluralsight · Full-stack Observability](https://www.pluralsight.com/courses/full-stack-observability) — [Pluralsight Lab · Using Prometheus with Kubernetes](https://www.pluralsight.com/labs/aws/using-prometheus-with-kubernetes) — [KodeKloud · Prometheus (PCA)](https://kodekloud.com/courses/prometheus-certified-associate-pca) — [Video](https://www.youtube.com/watch?v=l9-ExVhVizw) — [Docs](https://prometheus.io/docs/concepts/metric_types/)
- [ ] Prometheus architecture: server, TSDB, retention; pull model — [Pluralsight · Getting Started with Prometheus](https://www.pluralsight.com/courses/getting-started-prometheus) — [Pluralsight Lab · Building a Prometheus Server](https://www.pluralsight.com/labs/aws/building-a-prometheus-server) — [KodeKloud · Prometheus (PCA)](https://kodekloud.com/courses/prometheus-certified-associate-pca) — [Video](https://www.youtube.com/watch?v=h4Sl21AKiDg) — [Docs](https://prometheus.io/docs/)
- [ ] Deploy Prometheus on K8s (kube-prometheus-stack via Helm) — [Pluralsight · Getting Started with Prometheus](https://www.pluralsight.com/courses/getting-started-prometheus) — [Pluralsight Lab · Building a Prometheus Server](https://www.pluralsight.com/labs/aws/building-a-prometheus-server) — [KodeKloud · Prometheus (PCA)](https://kodekloud.com/courses/prometheus-certified-associate-pca) — [Video](https://www.youtube.com/watch?v=QoDqxm7ybLc) — [Docs](https://prometheus-operator.dev/)
- [ ] Exporters & service discovery (kubernetes_sd_configs) — [Pluralsight · Monitoring Key Systems with Prometheus Exporters](https://www.pluralsight.com/courses/monitoring-key-systems-prometheus-exporters) — [Pluralsight Lab · Linux Metrics with Prometheus](https://www.pluralsight.com/labs/aws/collecting-linux-server-metrics-with-prometheus) — [KodeKloud · Prometheus (PCA)](https://kodekloud.com/courses/prometheus-certified-associate-pca) — [Video](https://www.youtube.com/watch?v=mLPg49b33sA) — [Docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- [ ] **[OpenShift]** Built-in monitoring: user-workload monitoring, Thanos, Alertmanager — [Pluralsight · OpenShift Fundamentals and Workload Deployment](https://www.pluralsight.com/courses/openshift-fundamentals-workload-deployment) — [Pluralsight Lab · Kubernetes Metrics and Logging Stack](https://www.pluralsight.com/labs/aws/kubernetes-metrics-and-logging-stack-installation) — [OpenShift docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18) — [Video](https://www.youtube.com/watch?v=lO3A6WOJDic) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/monitoring/index)

## Deliverable
- Prometheus running, scraping your app

## Exit check
- [ ] Prometheus scrapes app + cluster targets — [Docs](https://prometheus.io/docs/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
