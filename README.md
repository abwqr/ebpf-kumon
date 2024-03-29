
---

# eBPF Kumon

This repository contains the eBPF (Extended Berkeley Packet Filter) Kumon project.

## Clone the Repository

```bash
git clone https://github.com/abwqr/ebpf-kumon.git
```

## Setup Instructions

### 1. Setup ELK Stack with Docker

Navigate to the `docker-elk` directory and run the following commands:

```bash
cd docker-elk
docker-compose up setup
docker-compose up
```

### 2. Setup Filebeat

Navigate to the `filebeat` directory in the project folder and run the following command. The current image is amd64 compatible.

```bash
cd ../filebeat
docker-compose up
```

### 3. Install Required Packages

Navigate to the `commands/setup` directory and run the `install.sh` script to install all the required packages.

```bash
cd ../../commands/setup
bash install.sh
```

## Prerequisites

Make sure you have the following installed:

- [Kubernetes](https://kubernetes.io/)
- [Helm](https://helm.sh/)
- [Kind](https://kind.sigs.k8s.io/)

**Note:** Kind is used to create multiple nodes on the same machine.

## References

- [Cilium Kubernetes Installation](https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/)
- [Inspektor Gadget](https://www.inspektor-gadget.io/)
- [Kubernetes Documentation](https://kubernetes.io/)
- [Elastic Stack](https://www.elastic.co/elastic-stack)
- [eBPF](https://ebpf.io/)

---
