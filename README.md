# 🎯 CKAD Practice Labs

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![K3s](https://img.shields.io/badge/K3s-FFC61C?style=for-the-badge&logo=k3s&logoColor=black)
![CKAD](https://img.shields.io/badge/CKAD-Exam%20Ready-success?style=for-the-badge)
![Labs](https://img.shields.io/badge/Labs-17-blue?style=for-the-badge)
![Exercises](https://img.shields.io/badge/Exercises-100+-orange?style=for-the-badge)

Hands-on lab exercises to prepare for the **Certified Kubernetes Application Developer (CKAD)** exam.

> 🖥️ These labs are optimized for **k3s** environment.

---

## 🆕 New to Kubernetes?

Start with the basics: **[Kubernetes Learning Guide](docs/00-intro.md)**

---

## 📊 CKAD Exam Info

| Property | Value |
|----------|-------|
| ⏱️ Duration | 2 hours |
| 📝 Questions | ~15-20 |
| 🎯 Passing Score | 66% |
| 💻 Format | Hands-on (Terminal) |
| 📚 Resources | kubernetes.io access ALLOWED |

---

## 📋 Lab List (17 Labs, 100+ Exercises)

### Week 1: Core Concepts
| # | Lab | Topic |
|---|-----|-------|
| 01 | [Pod Basics](labs/lab-01-pod-basics.md) | Pod |
| 02 | [Multi-Container](labs/lab-02-multi-container-pods.md) | Sidecar, Init |
| 03 | [Deployments](labs/lab-03-deployments.md) | Scaling, Updates |
| 04 | [Services](labs/lab-04-services.md) | ClusterIP, NodePort |

### Week 2: Configuration
| # | Lab | Topic |
|---|-----|-------|
| 05 | [ConfigMaps & Secrets](labs/lab-05-configmaps-secrets.md) | Config |
| 06 | [Volumes](labs/lab-06-volumes.md) | PV/PVC |
| 09 | [Resource Limits](labs/lab-09-resource-limits.md) | CPU/Memory |

### Week 3: Advanced
| # | Lab | Topic |
|---|-----|-------|
| 07 | [Jobs & CronJobs](labs/lab-07-jobs-cronjobs.md) | Batch |
| 08 | [Probes](labs/lab-08-probes.md) | Health Checks |
| 10 | [Network Policies](labs/lab-10-network-policies.md) | Firewall |
| 11 | [Security](labs/lab-11-security.md) | SecurityContext |

### Week 4: Tools
| # | Lab | Topic |
|---|-----|-------|
| 12 | [Ingress](labs/lab-12-ingress.md) | HTTP Routing |
| 13 | [Debugging](labs/lab-13-debugging.md) | Troubleshooting |
| 14 | [Helm](labs/lab-14-helm.md) | Charts |
| 15 | [Deployment Strategies](labs/lab-15-deployment-strategies.md) | Blue-Green |
| 16 | [Kustomize](labs/lab-16-kustomize.md) | Overlays |
| 17 | [Dockerfile](labs/lab-17-dockerfile.md) | Containers |

---

## 🎯 Exam Day Cheatsheet

```bash
# Aliases
alias k=kubectl
export do="--dry-run=client -o yaml"
export now="--force --grace-period=0"

# Quick commands
k run nginx --image=nginx $do > pod.yaml
k create deploy web --image=nginx --replicas=3
k expose deploy web --port=80
```

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| 📚 Total Labs | 17 |
| 📝 Exercises | 100+ |
| 📊 Mermaid Diagrams | 30+ |
| 📋 Curriculum Coverage | 100% |

---

⭐ **If this repo helped you, please give it a star!**

📝 **Contributing:** Pull requests are welcome!
