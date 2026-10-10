# Phase 5 — Observability Platform Ownership (Weeks 33–44)

**Why:** Move from *consuming* tools to *building and owning* observability
platforms. Splunk is limited to log onboarding (no cluster build/manage) and
Dynatrace Managed needs revision. Build the open-source stack end-to-end.

**Deliverable:** `projects/observability-platform/` — a full metrics + logs + traces
stack on Kubernetes, packaged as a reusable internal product with an onboarding
golden path.

**Resources:** KodeKloud *Prometheus Certified Associate (PCA)*, *Grafana Loki*,
*Grafana & Prometheus*, *EFK Stack*, plus Splunk and Dynatrace Managed docs.

---

## Week Pages
- [Week 33 — Metrics Fundamentals & Prometheus I](weeks/phase-5-week-33.md)
- [Week 34 — Prometheus II: PromQL & Alerts](weeks/phase-5-week-34.md)
- [Week 35 — Grafana & Dashboards](weeks/phase-5-week-35.md)
- [Week 36 — SLOs, Error Budgets & Instrumentation](weeks/phase-5-week-36.md)
- [Week 37 — Logging with Loki I](weeks/phase-5-week-37.md)
- [Week 38 — Logging with Loki II](weeks/phase-5-week-38.md)
- [Week 39 — EFK Stack I](weeks/phase-5-week-39.md)
- [Week 40 — EFK Stack II](weeks/phase-5-week-40.md)
- [Week 41 — Distributed Tracing & OpenTelemetry](weeks/phase-5-week-41.md)
- [Week 42 — Splunk: Beyond Log Onboarding I](weeks/phase-5-week-42.md)
- [Week 43 — Splunk: Beyond Log Onboarding II](weeks/phase-5-week-43.md)
- [Week 44 — Dynatrace Managed Revision + Project Exit](weeks/phase-5-week-44.md)

## Week 33 — Metrics Fundamentals & Prometheus I
- [ ] Observability 3 pillars; metrics types (counter/gauge/histogram/summary)
- [ ] Prometheus architecture: server, TSDB, retention; pull model
- [ ] Deploy Prometheus on K8s (kube-prometheus-stack via Helm)
- [ ] Exporters & service discovery (kubernetes_sd_configs)
- [ ] **Deliverable:** Prometheus running, scraping your app

## Week 34 — Prometheus II: PromQL
- [ ] Selectors, ranges, functions, rates, aggregations, `histogram_quantile`
- [ ] Recording rules & alerting rules
- [ ] Alertmanager: routing, inhibition, silences, receivers
- [ ] **Deliverable:** 5 alert rules + alertmanager routing

## Week 35 — Grafana & Dashboards
- [ ] Grafana data sources, variables, transformations
- [ ] Build dashboards (USE/RED methods) for the umbrella app + cluster
- [ ] Provisioning as code (dashboards + datasources in Git)
- [ ] **Deliverable:** dashboards committed as JSON/provisioning

## Week 36 — SLOs, Error Budgets & Instrumentation
- [ ] SLI/SLO/error budget design; burn-rate alerts
- [ ] Instrument an app (client library or OTel); expose `/metrics`
- [ ] Golden signals (latency, traffic, errors, saturation)
- [ ] **Deliverable:** documented SLOs + burn-rate alert for the app

## Week 37 — Logging with Loki I
- [ ] Loki architecture (distributor/ingester/querier); labels vs content
- [ ] Deploy Loki + Alloy/Promtail on K8s
- [ ] LogQL basics and log pipelines
- [ ] **Deliverable:** cluster + app logs queryable in Grafana

## Week 38 — Loki II
- [ ] Retention, multi-tenancy, object storage backend
- [ ] Metrics-from-logs; correlating logs with traces
- [ ] **Deliverable:** log-based alert + retention policy

## Week 39 — EFK Stack I
- [ ] Elasticsearch architecture & sizing; index lifecycle (ILM)
- [ ] Fluent Bit vs Fluentd; collection pipelines
- [ ] Deploy Elasticsearch + Fluent Bit feeding it
- [ ] **Deliverable:** Elasticsearch cluster + Fluent Bit DaemonSet

## Week 40 — EFK Stack II
- [ ] Kibana: index patterns, dashboards, saved searches
- [ ] Scaling, monitoring, and securing the EFK stack
- [ ] Compare EFK vs Loki (cost, ops, use cases) — write-up
- [ ] **Deliverable:** Kibana dashboards + comparison notes

## Week 41 — Distributed Tracing & OpenTelemetry
- [ ] Tracing concepts: spans, context propagation, sampling
- [ ] OTel Collector (receivers/processors/exporters); OTLP
- [ ] Export traces to Tempo/Jaeger; correlate with logs/metrics
- [ ] **Deliverable:** end-to-end trace for the app in Tempo/Jaeger

## Week 42 — Splunk: Beyond Log Onboarding I
- [ ] Splunk architecture: indexers, search heads, deployment servers, heavy forwarders
- [ ] Indexer clustering & search head clustering concepts
- [ ] Data lifecycle: hot/warm/cold/frozen, retention
- [ ] **Deliverable:** diagrams + notes building a Splunk cluster (map to your work)

## Week 43 — Splunk: Beyond Log Onboarding II
- [ ] Sizing, replication factors, licensing
- [ ] Config management at scale (deployment apps, cluster manager)
- [ ] Relate to your self-service onboarding platform: what a true platform owner controls
- [ ] **Deliverable:** a "Splunk platform ownership" checklist for your role

## Week 44 — Dynatrace Managed Revision + Project Exit
- [ ] Dynatrace Managed architecture: cluster nodes, ActiveGate, oneagent
- [ ] HA setup, upgrades, backups, DR (revise what you did 2 yrs ago)
- [ ] Metrics/entities/tags/dashboards; alerting profiles
- [ ] **Deliverable:** Dynatrace revision notes + open-source platform complete
- [ ] Package `projects/observability-platform/` with README + onboarding golden path

---

## Exit Criteria
- [ ] Open-source observability platform (metrics+logs+traces) deployed and documented
- [ ] Can design SLOs and burn-rate alerting
- [ ] Splunk cluster concepts understood (indexers/SH/DSS/ILM)
- [ ] Dynatrace Managed architecture refreshed with hands-on or detailed notes
