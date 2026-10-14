# Phase 2 · Week 8 — Helm I

[← Back to Phase 2](../phase-2-kubernetes-depth.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Author Helm charts from scratch.

## Topics
- [ ] Helm architecture: charts, releases, repositories — [Pluralsight · Packaging Applications with Helm for Kubernetes](https://www.pluralsight.com/courses/kubernetes-packaging-applications-helm) — [Pluralsight Lab · Package Applications with Helm](https://www.pluralsight.com/labs/aws/package-applications-with-helm-for-kubernetes) — [KodeKloud · Helm for Beginners](https://kodekloud.com/courses/helm-for-beginners) — [Video](https://www.youtube.com/watch?v=kJscDZfHXrQ) — [Video 2](https://www.youtube.com/watch?v=-ykwb1d0DXU) — [Docs](https://helm.sh/docs/)
- [ ] Create a chart: templates, values, .helmignore, helpers — [Pluralsight · Packaging Applications with Helm for Kubernetes](https://www.pluralsight.com/courses/kubernetes-packaging-applications-helm) — [Pluralsight Lab · Package Applications with Helm](https://www.pluralsight.com/labs/aws/package-applications-with-helm-for-kubernetes) — [KodeKloud · Helm for Beginners](https://kodekloud.com/courses/helm-for-beginners) — [Video](https://www.youtube.com/watch?v=jUYNS90nq8U) — [Docs](https://helm.sh/docs/)
- [ ] Templating: _helpers.tpl, named templates, with/range/if — [Pluralsight · Packaging Applications with Helm for Kubernetes](https://www.pluralsight.com/courses/kubernetes-packaging-applications-helm) — [Pluralsight Lab · Package Applications with Helm](https://www.pluralsight.com/labs/aws/package-applications-with-helm-for-kubernetes) — [KodeKloud · Helm for Beginners](https://kodekloud.com/courses/helm-for-beginners) — [Video](https://www.youtube.com/watch?v=fm_s70i_ws0) — [Video 2](https://www.youtube.com/watch?v=LNGSNaSjPCE) — [Docs](https://helm.sh/docs/)
- [ ] Package, lint, install/uninstall; helm template vs install — [Pluralsight · Packaging Applications with Helm for Kubernetes](https://www.pluralsight.com/courses/kubernetes-packaging-applications-helm) — [Pluralsight Lab · Package Applications with Helm](https://www.pluralsight.com/labs/aws/package-applications-with-helm-for-kubernetes) — [KodeKloud · Helm for Beginners](https://kodekloud.com/courses/helm-for-beginners) — [Video](https://www.youtube.com/watch?v=gg-GuHs8Nsk) — [Video 2](https://www.youtube.com/watch?v=cA8bF9sS6RQ) — [Docs](https://helm.sh/docs/)
- [ ] **[OpenShift]** Packaging on OCP: ImageStreams, BuildConfig/S2I, `oc new-app`, Templates — [Pluralsight · OpenShift Fundamentals and Workload Deployment](https://www.pluralsight.com/courses/openshift-fundamentals-workload-deployment) — [Pluralsight Lab · Deploying an App in OpenShift 4](https://www.pluralsight.com/labs/aws/configuring-and-deploying-an-application-using-git-in-openshift-4) — [KodeKloud · OpenShift 4](https://kodekloud.com/courses/openshift-4) — [Video](https://www.youtube.com/watch?v=4_PUu1tHKiI) — [Video 2](https://www.youtube.com/watch?v=x9QF_6oK_aU) — [Docs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/building_applications)

## Deliverable
- a chart for a simple web app

## Exit check
- [ ] Author and install a working chart without copying — [Docs](https://helm.sh/docs/)

> Mark topics `[x]` as you finish them and commit this page to track progress.
