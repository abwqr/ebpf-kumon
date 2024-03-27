#!/bin/bash


echo "Creating service nodeport nginx --tcp=80:80..."
kubectl create service nodeport nginx --tcp=80:80

echo "Creating deployment nginx --image=nginx..."
kubectl create deployment nginx --image=nginx

kubectl wait --timeout=-1s -n test-biolatency --for=condition=ready pod/stress-io

echo "Running myclientpod..."
kubectl run -ti --privileged --image wbitt/network-multitool myclientpod -- bash
curl nginx


# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Waiting for myclientpod pod failed."
    exit 1
fi

echo "myclientpod pod is ready and running"

