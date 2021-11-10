# Kubecost Cluster Sizing Recommendations

## What it does

This policy will raise an incident if there are any Cluster Sizing Recommendations from the Kubecost API.

## Functional Details

This policy checks the [Kubecost API](https://docs.kubecost.com/apis) for cluster sizing recommendation and report the response.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Kubecost Host* - IP Address of Kubecost LB
- *Email addresses* - Email addresses of the recipients you wish to notify.

## Actions

- Sends an email notification

## Cost

This Policy Template does not incur any cloud costs.
