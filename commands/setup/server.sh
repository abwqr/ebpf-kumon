#!/bin/bash

# 1. Port forward Grafana service for Cilium monitoring
echo "Port forwarding Grafana service for Cilium monitoring..."
kubectl -n cilium-monitoring port-forward service/grafana --address 0.0.0.0,:: 3000:3000 > /dev/null 2>&1 &


# Start cilium hubble ui
cilium hubble ui > /dev/null 2>&1 &

# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Port forwarding Grafana service failed."
    exit 1
fi


