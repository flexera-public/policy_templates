# Kubecost Request Sizing Recommendations Policy Template

## What it does

The Kubecost Request Sizing Recommendations Policy Template is used to get recommendations for resizing instances controlled with Kubecost

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- The policy receives recommendations to resize instances managed by Kubecost
- The policy calls Kubecost API endpoint

### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Kubecost host* - The host or IP Address where your Kubecost runs
- *Window size* - Number of days used in the calculation of the moving average
  - Default: "2d"
- *The algorithm for the CPU* - The algorithm to be used to calculate CPU recommendations
  - Default: "max"
- *CPU quantile* - The desired quantile to base CPU recommendations on
  - Default: 0.75
- *Target CPU Utilization (%)* - Target CPU utilization in percent
  - DEfault: 80
- *The algorithm for Memory* - The algorithm to be used to calculate memory recommendations
  - Default: "max"
- *Memory quantile* - The desired quantile to base memory recommendations on
  - Default: 0.75
- *Target Memory Utilization (%)* - Target memory utilization in percent
  - Default: 90

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
