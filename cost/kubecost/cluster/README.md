# Kubecost Cluster Sizing Recommendations cust

## What it does

The Kubecost Cluster Sizing Recommendations cust policy utilizes a Kubecost Host API endpoint to provide three different types of recommendations to resize clusters stored in it: single, multi and optimal.

## Functional Details

- The policy receives recommendations to resize clusters managed by Kubecost.
- The policy calls a Kubecost Host API endpoint.

### Input Parameters

- *Email addresses* - A list of email addresses to notify.
- *Kubecost Host or IP address* - The host or IP Address where Kubecost is running.
- *Minimum node count* - Minimum allowed node count in the cluster.
- *Number of days to analyze* - Historical range of time in days to analyze.
- *Target utilization (%)* - Desirable target utilization in percent.
- *Recommendation Type* - Type of existing recommendation in the cluster.
- *Kubecost Credential* - Kubecost Basic Auth credential.

## Cost

This Policy Template does not incur any cloud costs.