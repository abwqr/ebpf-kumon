#!/bin/bash

# Function to cleanup and terminate background processes
cleanup() {
    echo "Cleaning up..."
    pkill -P $$
}

# Trap termination signals to execute cleanup function
trap 'cleanup' SIGTERM SIGINT

# Get list of namespaces and nodes
namespaces=$(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}')
nodes=$(kubectl get nodes -o jsonpath='{.items[*].metadata.name}')

# Execute commands in the background and redirect output to parser
unbuffer kubectl gadget top file -A | python3 parser.py data/top_file.csv K8S.NODE,K8S.NAMESPACE,K8S.POD,K8S.CONTAINER,PID,COMM,READS,WRITES,RBYTES,WBYTES,T,FILE &
unbuffer kubectl gadget top tcp -A | python3 parser.py data/top_tcp.csv K8S.NODE,K8S.NAMESPACE,K8S.POD,K8S.CONTAINER,PID,COMM,IP,SRC,DST,SENT,RECV &
unbuffer kubectl gadget trace fsslower -A | python3 parser.py data/trace_fsslower.csv K8S.NODE,K8S.NAMESPACE,K8S.POD,K8S.CONTAINER,PID,COMM,T,BYTES,OFFSET,LAT,FILE &
unbuffer kubectl gadget trace open -A | python3 parser.py data/trace_open.csv K8S.NODE,K8S.NAMESPACE,K8S.POD,K8S.CONTAINER,PID,COMM,FD,ERR,PATH &
unbuffer kubectl gadget trace signal -A | python3 parser.py data/trace_signal.csv K8S.NODE,K8S.NAMESPACE,K8S.POD,K8S.CONTAINER,PID,COMM,SIGNAL,TPID,RET &
unbuffer kubectl gadget trace tcpconnect -A | python3 parser.py data/trace_tcpconnect.csv K8S.NODE,K8S.NAMESPACE,K8S.POD,K8S.CONTAINER,PID,COMM,IP,SRC,DST

# Wait for all background jobs to finish
wait

