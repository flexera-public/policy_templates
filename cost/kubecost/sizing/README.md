# Kubecost Request Right Sizing Recommendations Policy Template

## What it does

Kubecost request sizing recommendations policy template is used to resize instances controlled by Kubecost.

## Prerequisites

This policy uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- *Create a credential for Kubecost* - Create a new credential with basic authentication for use this policy.
- *Username* - username for kubecost host or Ip authentication
- *Password* - password for kubecost host or Ip authentication
- *provider=kubecost*

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- The policy receives recommendations to resize instances managed by Kubecost
- The policy calls Kubecost API endpoint

### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Kubecost Host or IP address* - The host or IP Address where your Kubecost runs
- *Window size* - Number of days used in the calculation of the moving average
  - Default: "2d"
- *The algorithm for the CPU* - The algorithm to be used to calculate CPU recommendations
  - Default: "max"
  - Allowed values: "max", "quantile"
- *CPU quantile* - The desired quantile to base CPU recommendations on
  - Default: 0.75
  - Minimum value: 0.01
  - Maximum value: 1
- *Target CPU Utilization (%)* - Target CPU utilization in percent
  - Default: 80
  - Minimum value: 1
  - Maximum value: 100
- *The algorithm for Memory* - The algorithm to be used to calculate memory recommendations
  - Default: "max"
  - Allowed values: "max", "quantile"
- *Memory quantile* - The desired quantile to base memory recommendations on
  - Default: 0.75
  - Minimum value: 0.01
  - Maximum value: 1
- *Target Memory Utilization (%)* - Target memory utilization in percent
  - Default: 90
  - Minimum value: 1
  - Maximum value: 100

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
