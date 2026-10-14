# Phase 4 · Week 24 — Terraform State & Backends

[← Back to Phase 4](../phase-4-iac.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Manage state safely.

## Topics
- [ ] Remote backends (S3 + DynamoDB lock); state locking — [Pluralsight · Terraform - Getting Started](https://www.pluralsight.com/courses/terraform-getting-started-2023) — [Pluralsight Lab · Infrastructure on AWS with Terraform](https://www.pluralsight.com/labs/aws/build-and-manage-infrastructure-on-aws-with-terraform) — [KodeKloud · Terraform Basics](https://kodekloud.com/courses/terraform-basics-training-course) — [Video](https://www.youtube.com/watch?v=o04xfWEouKM) — [Docs](https://developer.hashicorp.com/terraform/language/settings/backends/s3)
- [ ] State operations: import, mv, rm, taint, state pull/push — [Pluralsight · Advanced Implementation and State Operations](https://www.pluralsight.com/courses/advanced-implementation-and-state-operations) — [Pluralsight Lab · Remote Terraform State](https://www.pluralsight.com/labs/aws/enable-team-collaboration-by-moving-terraform-state-to-a-remote-backend) — [KodeKloud · Terraform Basics](https://kodekloud.com/courses/terraform-basics-training-course) — [Video](https://www.youtube.com/watch?v=6tcR4TxVRTM) — [Docs](https://developer.hashicorp.com/terraform/language/state/import)
- [ ] Workspaces vs directory-per-env — [Pluralsight · Terraform - Getting Started](https://www.pluralsight.com/courses/terraform-getting-started-2023) — [Pluralsight Lab · Infrastructure on AWS with Terraform](https://www.pluralsight.com/labs/aws/build-and-manage-infrastructure-on-aws-with-terraform) — [KodeKloud · Terraform Basics](https://kodekloud.com/courses/terraform-basics-training-course) — [Video](https://www.youtube.com/watch?v=W_wW_NNgxf4) — [Docs](https://developer.hashicorp.com/terraform/language/state/workspaces)
- [ ] Secrets handling; sensitive values; .tfvars strategy — [Pluralsight · Configuring and Managing Kubernetes Security](https://www.pluralsight.com/courses/configuring-managing-kubernetes-security-2) — [Pluralsight Lab · Kubernetes API Server and Pods](https://www.pluralsight.com/labs/aws/manage-the-kubernetes-api-server-and-pods) — [KodeKloud · Terraform Basics](https://kodekloud.com/courses/terraform-basics-training-course) — [Video](https://www.youtube.com/watch?v=3N0tGKwvBdA) — [Docs](https://developer.hashicorp.com/terraform/language/values/variables)

## Deliverable
- remote backend configured for your modules

## Exit check
- [ ] State locked remotely; import an existing resource — [Docs](https://developer.hashicorp.com/terraform/language/state/import)

> Mark topics `[x]` as you finish them and commit this page to track progress.
