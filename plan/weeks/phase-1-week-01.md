# Phase 1 · Week 1 — Environment + Fundamentals Refresh

[← Back to Phase 1](../phase-1-kubernetes-revision.md) | [Weeks index](00-index.md) | [Overview](../00-overview.md)

**Goal:** Set up your tooling and refresh core Kubernetes architecture.

## Topics
- [ ] Install kubectl, kind, k3d, k9s, helm; aliases + shell completion — [Pluralsight · Packaging Applications with Helm for Kubernetes](https://www.pluralsight.com/courses/kubernetes-packaging-applications-helm) — [Pluralsight Lab · Package Applications with Helm](https://www.pluralsight.com/labs/aws/package-applications-with-helm-for-kubernetes) — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Video](https://www.youtube.com/watch?v=SeQevrW176A) — [Video 2](https://www.youtube.com/watch?v=AMUQzyPvO04) — [Docs](https://kubernetes.io/docs/tasks/tools/)
- [ ] Spin up a local multi-node cluster (1 control-plane + 2 workers) with kind — [Pluralsight · Kubernetes Installation and Configuration Fundamentals](https://www.pluralsight.com/courses/kubernetes-installation-configuration-fundamentals) — [Pluralsight Lab · Code Your Infrastructure with Kubernetes](https://www.pluralsight.com/labs/aws/devops-containerization-and-orchestration-code-your-infrastructure-with-kubernetes) — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Video](https://www.youtube.com/watch?v=RORhczcOrWs) — [Lab](https://kind.sigs.k8s.io/docs/user/quick-start) — [Docs](https://kind.sigs.k8s.io/docs/)
- [ ] Review cluster architecture: control plane components, kubelet, kube-proxy, CNI — [Pluralsight · CKA: Network Policies and Traffic Management](https://www.pluralsight.com/courses/cka-kubernetes-network-policies-traffic-management) — [Pluralsight Lab · Configure Networking, Services and Ingress](https://www.pluralsight.com/labs/aws/configure-kubernetes-networking-services-and-ingress) — [KodeKloud · CKA Course](https://kodekloud.com/courses/certified-kubernetes-administrator-cka) — [Video](https://www.youtube.com/watch?v=umXEmn3cMWY) — [Docs](https://kubernetes.io/docs/concepts/overview/components/)
- [ ] Namespaces, contexts, kubectl config, --dry-run=client -o yaml workflow — [Pluralsight · Welcome to Kubectl for Kubernetes](https://www.pluralsight.com/courses/kubernetes-welcome-to-kubectl) — [Pluralsight Lab · Managing Kubernetes with Kubectl](https://www.pluralsight.com/labs/aws/managing-kubernetes-with-kubectl) — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Video](https://www.youtube.com/watch?v=K3jNo4z5Jx8) — [Docs](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
- [ ] Declarative vs imperative: create manifests with kubectl apply — [Pluralsight · Welcome to Kubectl for Kubernetes](https://www.pluralsight.com/courses/kubernetes-welcome-to-kubectl) — [Pluralsight Lab · Managing Kubernetes with Kubectl](https://www.pluralsight.com/labs/aws/managing-kubernetes-with-kubectl) — [KodeKloud · Kubernetes for Beginners](https://kodekloud.com/courses/kubernetes-for-the-absolute-beginners-hands-on-tutorial) — [Video](https://www.youtube.com/watch?v=shqiLgbzIJY) — [Docs](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)

## Deliverable
- projects/k8s-bootstrap/kind-config.yaml committed

## Exit check
- [ ] Local multi-node cluster is up and you can deploy a Pod

> Mark topics `[x]` as you finish them and commit this page to track progress.
