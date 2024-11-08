# Kubecost Container Request Rightsizing Recommendations

## What It Does

This policy template reports Kubecost container request rightsizing recommendations generated from the Kubecost API with the user-specified parameters. Optionally, this report can be emailed.

## How It Works

- The policy requests recommendations for request right-sizing based on parameters provided.
- The [Container Request Right Sizing Recommendation API (V2)](https://docs.kubecost.com/apis/savings-apis/api-request-right-sizing-v2) provides recommendations for container resource requests based on configurable parameters and estimates the savings from implementing those recommendations on a per-container, per-controller level.
- Note that, if the cluster-level resources stay static, you will not realize significant savings until you reduce your cluster resources.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Kubecost Host* - Kubecost Hostname or IP Address of Kubecost Load Balancer to make queries against.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Scope* - Whether to produce recommendations for the entire Kubecost estate or per cluster.
- *Lookback Period (Days)* - Number of historical days of usage to analyze when generating recommendations.
- *CPU Assessment Algorithm* - Whether max or a certain quantile should be used to produce CPU request recommendations.
- *CPU Percentile (%)* - The desired percentile to base CPU request recommendations on.
- *Target CPU Utilization (%)* - CPU utilization target to use when generating recommendations.
- *Memory Assessment Algorithm* - Whether max or a certain quantile should be used to produce Memory request recommendations.
- *Memory Percentile (%)* - The desired percentile to base Memory request recommendations on.
- *Target Memory Utilization (%)* - Memory utilization target to use when generating recommendations.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Kubecost

This Policy Template requires a minimum Kubecost version of 1.100.2 and does not use credentials to access resources in the Kubecost API. If you require authentication for Kubecost access, you can use one of the following options:

- Use a modified, custom version of this policy template to support Basic Auth credentials (Recommended).
- [Enable external access on your pod.](https://docs.kubecost.com/install-and-configure/install/ingress-examples)

## Supported Clouds

- Kubecost

## Cost

This policy template does not incur any cloud costs.
