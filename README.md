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

- ⏱️ **Duration:** 2 hours
- 📝 **Questions:** ~15-20
- 🎯 **Passing Score:** 66%
- 💻 **Format:** Hands-on (Terminal)
- 📚 **Resources:** kubernetes.io access ALLOWED

---

## 📋 Lab List (17 Labs, 100+ Exercises)

### 🟢 Week 1: Core Concepts

- **Lab 01:** [Pod Basics](labs/lab-01-pod-basics.md) - Create and manage Pods
- **Lab 02:** [Multi-Container Pods](labs/lab-02-multi-container-pods.md) - Sidecar, Init containers
- **Lab 03:** [Deployments](labs/lab-03-deployments.md) - Scaling, Rolling updates
- **Lab 04:** [Services](labs/lab-04-services.md) - ClusterIP, NodePort, LoadBalancer

### 🟡 Week 2: Configuration

- **Lab 05:** [ConfigMaps & Secrets](labs/lab-05-configmaps-secrets.md) - External configuration
- **Lab 06:** [Volumes](labs/lab-06-volumes.md) - PV, PVC, Storage
- **Lab 09:** [Resource Limits](labs/lab-09-resource-limits.md) - CPU/Memory management

### 🟠 Week 3: Advanced

- **Lab 07:** [Jobs & CronJobs](labs/lab-07-jobs-cronjobs.md) - Batch processing
- **Lab 08:** [Probes](labs/lab-08-probes.md) - Liveness, Readiness
- **Lab 10:** [Network Policies](labs/lab-10-network-policies.md) - Pod firewall rules
- **Lab 11:** [Security](labs/lab-11-security.md) - SecurityContext, ServiceAccounts

### 🔴 Week 4: Tools

- **Lab 12:** [Ingress](labs/lab-12-ingress.md) - HTTP/HTTPS routing
- **Lab 13:** [Debugging](labs/lab-13-debugging.md) - Troubleshooting pods
- **Lab 14:** [Helm](labs/lab-14-helm.md) - Package management
- **Lab 15:** [Deployment Strategies](labs/lab-15-deployment-strategies.md) - Blue-Green, Canary
- **Lab 16:** [Kustomize](labs/lab-16-kustomize.md) - Configuration overlays
- **Lab 17:** [Dockerfile](labs/lab-17-dockerfile.md) - Container images

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
k create cm myconfig --from-literal=key=value
k create secret generic mysecret --from-literal=pass=123
```

---

## 📊 Repository Stats

- 📚 **Total Labs:** 17
- 📝 **Exercises:** 100+
- 📊 **Diagrams:** 30+
- 📋 **Curriculum Coverage:** 100%

---

## 📚 Additional Resources

- [Kubernetes Docs](https://kubernetes.io/docs/) - Accessible during exam!
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Killer Shell](https://killer.sh/ckad) - Real exam simulator
- [KillerCoda](https://killercoda.com/ckad) - Free scenarios

---

⭐ **If this repo helped you, please give it a star!**

📝 **Contributing:** Pull requests are welcome!
