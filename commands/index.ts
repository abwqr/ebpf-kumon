import * as k8s from "@pulumi/kubernetes";

// Initialize a Kubernetes provider with the default kubeconfig credentials
const provider = new k8s.Provider("provider", {
  kubeconfig: k8s.config.getKubeconfig(),
});

// Deploy Cilium CNI using a Helm Chart
const ciliumRelease = new k8s.helm.v3.Release("cilium", {
  name: "cilium",
  chart: "cilium",
  version: "1.14.5", // Set the desired Cilium chart version here
  namespace: "kube-system",
  repositoryOpts: {
    repo: "https://helm.cilium.io/",
  },
  values: {
    prometheus: {
      enabled: true,
      operator: {
        enabled: true,
      },
    },
    hubble: {
      enabled: true,
      metrics: {
        enableOpenMetrics: true,
        enabled: "dns,drop,tcp,flow,port-distribution,icmp,httpV2:exemplars=true;labelsContext=source_ip,source_namespace,source_workload,destination_ip,destination_namespace,destination_workload,traffic_direction",
      },
      relay: {
        enabled: true,
      },
      ui: {
        enabled: true,
      },
    },
  },
}, { provider });

// Deploy OpenTelemetry Collector using a Helm Chart
const otelCollectorRelease = new k8s.helm.v3.Release("otel-collector", {
  name: "opentelemetry-collector",
  chart: "opentelemetry-collector",
  version: "0.7.0", // Set the desired OpenTelemetry chart version here
  namespace: "opentelemetry",
  repositoryOpts: {
    repo: "https://open-telemetry.github.io/opentelemetry-helm-charts",
  },
  values: {
    // Configure collector to use appropriate receivers, processors, exporters
    // Set your custom configurations here
  },
}, { provider });

// Export the public addresses if relevant
export const ciliumStatus = ciliumRelease.status;
export const otelCollectorStatus = otelCollectorRelease.status;

