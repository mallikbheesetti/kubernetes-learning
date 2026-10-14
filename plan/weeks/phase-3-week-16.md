# Phase 3 · Week 16 — GitHub Actions (Modern CI)

[← Back to Phase 3](../phase-3-gitops-cicd.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Build modern CI pipelines.

## Topics
- [ ] Workflow syntax: jobs, steps, matrix, caching, artifacts, secrets — [Pluralsight · Authoring and Maintaining GitHub Actions Workflows](https://www.pluralsight.com/courses/github-actions-authoring-maintaining-workflows) — [Pluralsight Lab · Custom GitHub Actions Runner](https://www.pluralsight.com/labs/aws/setting-up-a-custom-github-actions-runner) — [Video](https://www.youtube.com/watch?v=jtKrINOzQ3A) — [Video 2](https://www.youtube.com/watch?v=E2RRxcq_08E) — [Docs](https://docs.github.com/en/actions)
- [ ] Build + test + container build; push to GHCR — [Pluralsight · Authoring and Maintaining GitHub Actions Workflows](https://www.pluralsight.com/courses/github-actions-authoring-maintaining-workflows) — [Pluralsight Lab · Custom GitHub Actions Runner](https://www.pluralsight.com/labs/aws/setting-up-a-custom-github-actions-runner) — [Video](https://www.youtube.com/watch?v=R8_veQiYBjI) — [Video 2](https://www.youtube.com/watch?v=WjzA9dfk5w4) — [Docs](https://docs.github.com/en/packages)
- [ ] Reusable workflows + composite actions — [Pluralsight · Authoring and Maintaining GitHub Actions Workflows](https://www.pluralsight.com/courses/github-actions-authoring-maintaining-workflows) — [Pluralsight Lab · Custom GitHub Actions Runner](https://www.pluralsight.com/labs/aws/setting-up-a-custom-github-actions-runner) — [Video](https://www.youtube.com/watch?v=zc19mR3O4a4) — [Video 2](https://www.youtube.com/watch?v=lRypYtmbKMs) — [Docs](https://docs.github.com/en/actions)
- [ ] OIDC to cloud (no long-lived keys) — [Pluralsight · CKA: Securing Access with RBAC and Admission Controls](https://www.pluralsight.com/courses/cka-securing-access-with-rbac-and-admission-controls) — [Pluralsight Lab · Kubernetes Security and RBAC for CKA](https://www.pluralsight.com/labs/aws/manage-kubernetes-security-and-rbac-for-cka) — [Video](https://www.youtube.com/watch?v=Io5UFJlEJKc) — [Docs](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-cloud-providers)
- [ ] **[OpenShift]** OpenShift Pipelines (Tekton) + S2I builds as native CI — [Pluralsight · OpenShift Fundamentals and Workload Deployment](https://www.pluralsight.com/courses/openshift-fundamentals-workload-deployment) — [Pluralsight Lab · Deploying an App in OpenShift 4](https://www.pluralsight.com/labs/aws/configuring-and-deploying-an-application-using-git-in-openshift-4) — [Video](https://www.youtube.com/watch?v=pMDiiW1UqLo) — [Video 2](https://www.youtube.com/watch?v=036WYhSlGEs) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/pipelines)

## Deliverable
- .github/workflows/build.yaml for the umbrella app

## Exit check
- [ ] A push builds and pushes a container image via Actions — [Docs](https://docs.github.com/en/actions)

> Mark topics `[x]` as you finish them and commit this page to track progress.
