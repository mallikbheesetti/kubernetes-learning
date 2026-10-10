# Phase 6 — Kubernetes Security (Weeks 45–50)

**Why:** Secure the platform you're building. CKS-level capability (no exam
required) plus policy-as-code and secret management you can own.

**Deliverable:** `projects/hardened-cluster/` — a hardened cluster baseline with
policies, RBAC, Pod Security, network policies, and Vault-backed secrets.

**Resources:** KodeKloud *Certified Kubernetes Security Specialist (CKS)*,
*KCSA*, *Kyverno*, HashiCorp Vault; CIS Benchmark, NSA/CISA K8s hardening guide.

---

## Week 45 — Authentication, Authorization & RBAC
- [ ] AuthN: users/groups, service accounts, OIDC concepts, certificates
- [ ] AuthZ: RBAC (roles/bindings), ABAC, node/webhook
- [ ] Kubeconfig merging; `kubectl auth can-i`; impersonation
- [ ] **Deliverable:** least-privilege RBAC for the umbrella app + platform

## Week 46 — Cluster Hardening & Pod Security
- [ ] API server/etcd/kubelet hardening flags; CIS benchmark scan (kube-bench)
- [ ] Pod Security Admission (baseline/restricted); securityContext
- [ ] seccomp, AppArmor/SELinux, capability dropping, read-only FS
- [ ] **Deliverable:** restricted-namespace enforcement demonstration

## Week 47 — Network Security & Supply Chain
- [ ] NetworkPolicies: default-deny + allow (ingress/egress)
- [ ] Service mesh mTLS concepts (preview Istio); Cilium network policy
- [ ] Supply chain: image scanning (Trivy), SBOM, signing (cosign), admission verify
- [ ] **Deliverable:** signed image + admission verification policy

## Week 48 — Runtime Security & Monitoring
- [ ] Threat model; runtime detection (Falco) concepts + deploy
- [ ] Audit logging (API server audit policy)
- [ ] Secrets: encryption at rest; external secrets; Vault integration
- [ ] **Deliverable:** Falco rules + audit policy + Vault secrets injection

## Week 49 — Policy-as-Code with Kyverno
- [ ] Validate, mutate, generate policies
- [ ] Enforce guardrails: required labels, resource limits, allowed registries
- [ ] Policy reporting / exceptions
- [ ] **Deliverable:** Kyverno policy suite for the platform

## Week 50 — Project Integration & Exit
- [ ] Combine: hardened baseline + RBAC + PSS + NetworkPolicies + Kyverno + Vault
- [ ] Run a kube-bench scan and remediate top findings
- [ ] Document the security baseline as a platform standard
- [ ] **Deliverable:** `projects/hardened-cluster/` + security standard doc

---

## Exit Criteria
- [ ] CIS-style scan passes with documented remediations
- [ ] Pod Security restricted enforced; NetworkPolicies default-deny in place
- [ ] Signed images + admission policy + Kyverno guardrails working
- [ ] Secrets managed via Vault/External Secrets (no plaintext)
