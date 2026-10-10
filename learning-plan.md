# Kubernetes Mastery Learning Plan — Arjun Besetti

Tailored to the profile: **Principal DevOps & Platform Engineer**, 15+ years,
currently VP–Lead Software Engineer (Observability) at Wells Fargo.
Existing: CKA (2025), AWS SAA (2023), Splunk Admin, RHCE; strong on
AWS/GCP, Terraform, Ansible, Jenkins, Docker, Python/Bash, and observability
(Splunk/Dynatrace).

## Goal

Move from **certified Kubernetes administrator** to **cloud-native platform
authority** — deep cluster internals, GitOps, service mesh, security, and
production observability — ideally landing **Kubestronaut** while producing a
public portfolio of hands-on projects.

## Starting-Point Gap Analysis

| Area | Current level | Target |
| --- | --- | --- |
| Kubernetes admin | Certified (CKA) | Expert / CKS + deep internals |
| Kubernetes app dev | Working knowledge | CKAD-level fluency |
| GitOps / ArgoCD | Adjacent (Spinnaker, Jenkins) | Production GitOps ownership |
| Service mesh / ingress | Light (Istio not in resume) | Istio + Gateway API |
| Observability | Expert (Splunk, Dynatrace) | Prometheus/Grafana/OTel + PCA cert |
| Security (K8s) | Foundational | CKS + KCSA + Kyverno/Vault |
| IaC | Strong (Terraform/Ansible) | Terraform Associate + modules/state at scale |
| Platform engineering | Strong (self-service platform lead) | IDP patterns (Backstage, Crossplane, Operators) |
| AI/ML on K8s | None | Kubeflow/KServe/vLLM foundations |

## Certification Roadmap (Kubestronaut track)

1. **CKAD** — next, leverages CKA base (~4–6 weeks)
2. **CKS** — security depth (~6–8 weeks)
3. **KCNA** — cloud-native concepts (fast win, ~2–3 weeks)
4. **KCSA** — security associate (~3–4 weeks)
5. → **Kubestronaut** badge (all 5 CNCF certs)
6. Optional later: **PCA** (Prometheus), **Terraform Associate**, **CNPE** (Platform Engineer)

## Phased Plan (~12 months, ~8–10 hrs/week)

### Phase 1 — Core Kubernetes Mastery & Refresh (Weeks 1–4)
- Kubernetes for the Absolute Beginners (hands-on refresh)
- 12 Factor App; dense `kubectl` practice; k9s
- Deep dive: control plane, etcd, kubelet, scheduling, networking model
- **Project:** local multi-node cluster (kind/k3d) + automated bootstrap script

### Phase 2 — Application Development on K8s, CKAD (Weeks 5–12)
- CKAD prep: multi-container pods, probes, jobs/cronjobs, config, security context
- Helm for Beginners + Kustomize
- Kubernetes Networking Deep Dive (CNI, Services, Ingress)
- **Project:** Helm-umbrella app (API + worker + DB) with Kustomize overlays
- **Milestone:** pass CKAD

### Phase 3 — GitOps, CI/CD & Platform Engineering (Weeks 13–24)
- ArgoCD + GitHub Actions + Jenkins (formalize), CI/CD learning path
- Kubernetes Operators; Package Management with Glasskube
- Platform patterns: namespaces-as-a-service, RBAC, policy-as-code
- **Project:** GitOps repo driving ArgoCD to a cluster; self-service onboarding template
- **Milestone:** production-grade GitOps demo

### Phase 4 — Observability & Monitoring (Weeks 25–32)
- Prometheus Certified Associate (PCA); Grafana Loki; Grafana & Prometheus
- EFK stack; OpenTelemetry instrumentation; SLOs/alerting
- Bridge your Splunk/Dynatrace expertise to open-source stack
- **Project:** full observability stack (Prometheus + Grafana + Loki + OTel) on K8s
- **Milestone:** pass PCA (optional)

### Phase 5 — Kubernetes Security (Weeks 33–42)
- CKS prep: cluster hardening, supply chain, runtime security, network policies
- KCSA; Kyverno policies; HashiCorp Vault
- **Milestone:** pass CKS + KCSA

### Phase 6 — Cloud, IaC & Service Mesh (Weeks 43–48)
- AWS EKS (deep), Terraform Associate + modules/state at scale, Ansible Advanced
- Istio Service Mesh; Gateway API with NGINX; kgateway
- **Project:** EKS cluster provisioned by Terraform module + Istio traffic management
- **Milestone:** KCNA (fast, complete the Kubestronaut set)

### Phase 7 — Specialization (ongoing, months 10–12+)
Pick one or two:
- **Platform Engineering:** Backstage IDP, Crossplane, Operators, CNPE prep
- **AI/ML on K8s:** KubeFlow, KServe, LLM-d, vLLM & GPUs (Kubernetes & Cloud Native AI path)
- **SRE:** Kubernetes Autoscaling, resiliency/DR, chaos engineering

### Capstone (final month)
- Public "platform-in-a-box": EKS + Terraform + ArgoCD + Helm/Kustomize +
  Prometheus/Grafana/Loki + Istio + Kyverno, with CI, docs, and runbooks.
- Publish to GitHub; write up architecture posts.

## Weekly Cadence (suggested, ~10 hrs)
- Mon–Fri: 1 hr theory (course videos) + 30 min hands-on lab
- Sat: 2–3 hr project deep work
- Sun: 1 hr review + flashcards (kubectl, YAML) + notes committed to repo

## KodeKloud Resources
See `resources/kodekloud-courses.md` for the full curated catalog and URLs.

Key learning paths to follow in order:
1. Kubernetes (20 courses) → 2. CKA/CKAD/CKS/KCNA/KCSA → 3. Docker → 4. IaC →
5. CI/CD → 6. HashiCorp → 7. Kubernetes & Cloud Native AI → 8. Kubestronaut.

## Progress Log
Track completion here (date + course + artifact/link):
- [ ] Phase 1 started
- [ ] CKAD passed
- [ ] GitOps project shipped
- [ ] PCA passed
- [ ] CKS passed
- [ ] KCSA passed
- [ ] KCNA passed → **Kubestronaut**
- [ ] Capstone published
