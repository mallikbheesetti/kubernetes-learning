# Phase 5 · Week 41 — Distributed Tracing & OpenTelemetry

[← Back to Phase 5](../phase-5-observability.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** End-to-end traces.

## Topics
- [ ] Tracing concepts: spans, context propagation, sampling — [Pluralsight · Observability with OpenTelemetry and Grafana](https://www.pluralsight.com/courses/opentelemetry-grafana-observability) — [Pluralsight Lab · Implement OpenTelemetry for Java](https://www.pluralsight.com/labs/codeLabs/guided-implement-opentelemetry-for-java-observability) — [Video](https://www.youtube.com/watch?v=Of_ygNU_Cbw) — [Docs](https://opentelemetry.io/docs/concepts/signals/traces/)
- [ ] OTel Collector (receivers/processors/exporters); OTLP — [Pluralsight · Monitoring Key Systems with Prometheus Exporters](https://www.pluralsight.com/courses/monitoring-key-systems-prometheus-exporters) — [Pluralsight Lab · Linux Metrics with Prometheus](https://www.pluralsight.com/labs/aws/collecting-linux-server-metrics-with-prometheus) — [Video](https://www.youtube.com/watch?v=_CJrFW_yjRo) — [Docs](https://opentelemetry.io/docs/collector/)
- [ ] Export traces to Tempo/Jaeger; correlate with logs/metrics — [Pluralsight · Observability with OpenTelemetry and Grafana](https://www.pluralsight.com/courses/opentelemetry-grafana-observability) — [Pluralsight Lab · Implement OpenTelemetry for Java](https://www.pluralsight.com/labs/codeLabs/guided-implement-opentelemetry-for-java-observability) — [Video](https://www.youtube.com/watch?v=Oa-zqv-EBpw) — [Video 2](https://www.youtube.com/watch?v=ZIN7H00ulQw) — [Docs](https://www.jaegertracing.io/docs/)
- [ ] **[OpenShift]** Distributed Tracing (Tempo/Jaeger) via OpenTelemetry on OCP — [Pluralsight · Observability with OpenTelemetry and Grafana](https://www.pluralsight.com/courses/opentelemetry-grafana-observability) — [Pluralsight Lab · Distributed Tracing with Tempo](https://www.pluralsight.com/labs/aws/kubernetes-distributed-tracing-backend-deployment-with-tempo) — [OpenShift docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18) — [Video](https://www.youtube.com/watch?v=TmC7Ha3Qqk4) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18)

## Deliverable
- end-to-end trace for the app in Tempo/Jaeger

## Exit check
- [ ] A request trace spans multiple services — [Docs](https://opentelemetry.io/docs/concepts/signals/traces/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
