#!/bin/bash

# 1. Set the max_user_instances for inotify
echo "Setting max_user_instances for inotify..."
sysctl -w fs.inotify.max_user_instances=1024

# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Unable to set max_user_instances for inotify."
    exit 1
fi

echo "Adding Cilium Helm repository..."
helm repo add cilium https://helm.cilium.io/ &>/dev/null


# 3. Install Cilium using Helm
echo "Installing Cilium..."
helm install cilium cilium/cilium --version 1.14.5 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true \
   --set hubble.enabled=true \
   --set hubble.metrics.enableOpenMetrics=true \
   --set 'hubble.metrics.enabled={dns,drop,tcp,flow,port-distribution,icmp,httpV2:exemplars=true;labelsContext=source_ip\,source_namespace\,source_workload\,destination_ip\,destination_namespace\,destination_workload\,traffic_direction}' \
   --set hubble.relay.enabled=true \
   --set hubble.ui.enabled=true

# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Unable to install Cilium."
    exit 1
fi

# 2. Apply prom-grafana.yaml using kubectl
echo "Applying prom-grafana.yaml..."
kubectl apply -f scripts/prom-grafana.yaml

# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Unable to apply prom-grafana.yaml."
    exit 1
fi

source ./scripts/krew.sh
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
kubectl krew install gadget

# 4. Check Cilium status, wait for completion
echo "Checking Cilium status..."
cilium status --wait

# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Cilium status check failed."
    exit 1
fi


echo "All commands executed successfully."
exit 0

