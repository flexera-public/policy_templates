# Kubecost Cluster Rightsizing Recommendations

## What it does

The Kubecost Cluster Sizing Recommendations policy utilizes a Kubecost API to provide cluster rightsizing recommendations.

## Prerequisites

Minimum Kubecost version to apply this policy: 1.100.2.\
This policy does not use credentials to access resources in a Kubecost API.\
If you setup authentication for Kubecost access, you can use one of the following options:

- Enable external access on your pod following this [example](https://docs.kubecost.com/install-and-configure/install/ingress-examples).
- Update the policy to support Basic Auth credentials.

## Functional Details

The policy retrieves Kubecost recommendations for rightsizing of Kubernetes clusters.

### Input Parameters

- *Email addresses* - A list of email addresses to notify.
- *Kubecost Host or IP address* - The host or IP Address where Kubecost is running.
- *Minimum node count* - Minimum allowed node count in the cluster.
- *Number of days to analyze* - Historical range of time in days to analyze.
- *Target utilization (%)* - Desirable target utilization in percent.
- *Recommendation Strategy* - Recommendation strategy to apply.
  - Single: Provides cluster rightsizing recommendation for a uniform node type.
  - Multi: Provides cluster rightsizing recommendation allowing different node types.
  - Optimal: Provide cluster rightsizing recommendation with most savings, could be single or multi.

## Cost

This Policy Template does not incur any cloud costs.
