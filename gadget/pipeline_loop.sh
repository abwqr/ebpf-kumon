#!/bin/bash

namespaces=$(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}')
nodes=$(kubectl get nodes -o jsonpath='{.items[*].metadata.name}')
while true; do
    for node in $nodes; do
        unbuffer kubectl gadget profile block-io --node $node --timeout 60 | python3 profile_blockio_parser.py data/profile_blockio.csv $node &
        unbuffer kubectl gadget profile tcprtt --node $node --timeout 5 | python3 profile_tcprtt_parser.py data/profile_tcprtt.csv $node &
        sleep 1 
    done
    unbuffer kubectl gadget snapshot process -A | python3 parser.py data/snapshot_process.csv K8S.NODE,K8S.NAMESPACE,K8S.POD,K8S.CONTAINER,COMM,PID,UID,GID
done

