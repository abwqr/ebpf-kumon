#!/bin/bash

# Create namespace test-biolatency
echo "Creating namespace test-biolatency..."
kubectl create ns test-biolatency

# Run stress with 1 worker that will generate I/O operations
echo "Running stress with 1 worker to generate I/O operations..."
kubectl run --restart=Never --image=polinux/stress stress-io -n test-biolatency -- stress --io 1

# Wait for the stress-io pod to be ready
echo "Waiting for stress-io pod to be ready..."
kubectl wait --timeout=-1s -n test-biolatency --for=condition=ready pod/stress-io

# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Waiting for stress-io pod failed."
    exit 1
fi

echo "stress-io pod is ready and running in namespace test-biolatency."

