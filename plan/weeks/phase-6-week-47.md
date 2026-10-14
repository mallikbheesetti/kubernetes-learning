# Phase 6 · Week 47 — Network Security & Supply Chain

[← Back to Phase 6](../phase-6-security.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Lock down traffic and images.

## Topics
- [ ] NetworkPolicies: default-deny + allow (ingress/egress) — [Pluralsight · Configuring and Managing Kubernetes Networking, Services, and Ingress](https://www.pluralsight.com/courses/configuring-managing-kubernetes-networking-services-ingress) — [Pluralsight Lab · Lock Down Inter-Pod Traffic](https://www.pluralsight.com/labs/aws/lock-down-inter-pod-communication-with-networkpolicies) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=eVtnevr3Rao) — [Video 2](https://www.youtube.com/watch?v=Fr-6oDHbobM) — [Docs](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [ ] Service mesh mTLS concepts (preview Istio); Cilium network policy — [Pluralsight · Managing Apps on Kubernetes with Istio](https://www.pluralsight.com/courses/istio-managing-apps-kubernetes) — [Pluralsight Lab · Istio in Kubernetes](https://www.pluralsight.com/labs/aws/istio-in-kubernetes) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=6zDrLvpfCK4) — [Video 2](https://www.youtube.com/watch?v=TxPEpArfjwY) — [Docs](https://docs.cilium.io/en/stable/)
- [ ] Supply chain: image scanning (Trivy), SBOM, signing (cosign), admission verify — [Pluralsight · Container Infrastructure Analysis with Trivy](https://www.pluralsight.com/courses/container-infrastructure-analysis-trivy) — [Pluralsight Lab · Securing Container Runtimes](https://www.pluralsight.com/labs/aws/securing-container-runtimes-for-cks) — [KodeKloud · CKS Course](https://kodekloud.com/courses/certified-kubernetes-security-specialist-cks) — [Video](https://www.youtube.com/watch?v=2cjH6Zkieys) — [Video 2](https://www.youtube.com/watch?v=soTg-b-Uqkw) — [Docs](https://aquasecurity.github.io/trivy/)

## Deliverable
- signed image + admission verification policy

## Exit check
- [ ] Only verified/signed images are admitted — [Docs](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
