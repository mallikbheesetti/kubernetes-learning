# Phase 4 · Week 27 — Testing & CI for IaC

[← Back to Phase 4](../phase-4-iac.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Add quality gates to infrastructure.

## Topics
- [ ] Test types: static (tflint, checkov/tfsec), integration (Terratest), native terraform test — [Pluralsight · Terraform Deep Dive](https://www.pluralsight.com/courses/terraform-deep-dive-2023) — [Video](https://www.youtube.com/watch?v=oe8tNzkw8cM) — [Video 2](https://www.youtube.com/watch?v=xF-ZNcAZQgg) — [Docs](https://terratest.gruntwork.io/)
- [ ] CI pipeline: fmt -> validate -> plan -> policy -> apply (manual gate) — [Pluralsight · DevOps Foundations: CI/CD](https://www.pluralsight.com/courses/devops-foundations-continuous-integration-continuous-delivery) — [Pluralsight Lab · Fully-Automated CD Pipeline](https://www.pluralsight.com/labs/aws/implementing-fully-automated-deployment-in-a-cd-pipeline) — [KodeKloud · Terraform Basics](https://kodekloud.com/courses/terraform-basics-training-course) — [Video](https://www.youtube.com/watch?v=553liLRXGqY) — [Docs](https://developer.hashicorp.com/terraform/docs)
- [ ] Policy-as-code: OPA/Conftest or Sentinel basics — [Pluralsight · Configuring and Managing Kubernetes Security](https://www.pluralsight.com/courses/configuring-managing-kubernetes-security-2) — [Pluralsight Lab · Gatekeeper Policy-as-Code](https://www.pluralsight.com/labs/azure/enforce-deployment-safeguards-with-azure-policy-and-gatekeeper) — [Video](https://www.youtube.com/watch?v=FDghIoMS9nU) — [Docs](https://developer.hashicorp.com/terraform/cloud-docs/policy-enforcement/sentinel)

## Deliverable
- CI workflow for the module library

## Exit check
- [ ] IaC has automated tests + CI gates

> Mark topics `[x]` as you finish them and commit this page to track progress.
