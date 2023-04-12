# Kubecost Cluster Sizing Recommendations cust

## What it does

The Kubecost Cluster Sizing Recommendations cust policy utilizes a Kubecost Host API endpoint to provide three different types of recommendations to resize clusters stored in it: single, multi and optimal.

## Prerequisites

This policy uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to access resources in a Kubecost Host API. In order to apply this policy you must have a Kubecost Basic Auth Credential registered in the system with the information below:

- *Username* - Username for Kubecost Host or Ip authentication
- *Password* - Password for Kubecost Host or Ip authentication

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

## Cost

This Policy Template does not incur any cloud costs.
