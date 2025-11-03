# Kubecost Cluster Rightsizing Recommendation

## What It Does

This policy template reports a Kubecost cluster rightsizing recommendation generated from the Kubecost API with the user-specified parameters. Optionally, this report can be emailed.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Kubecost Host* - Kubecost Hostname or IP Address of Kubecost Load Balancer to make queries against.
- *Minimum Node Count* - Minimum required node count for recommendations.
- *Lookback Period (Days)* - Number of historical days of usage to analyze when generating recommendations.
- *Target Utilization (%)* - Utilization target to use when generating recommendations.
- *Recommendation Strategy* - Recommendation strategy to use. 'Optimal' will automatically select whichever strategy has the highest potential savings.
- *Allow Shared Core* - Whether to include shared core node types for recommendations.
- *Architecture* - Chipset architecture for recommended nodes (e.g., 'x86' or 'ARM'). Note: 'ARM' is currently supported only on AWS clusters.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

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
