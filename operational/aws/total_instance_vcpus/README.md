# AWS Usage Report - Number of Instance vCPUs Used

## What it does

This Policy Template leverages Optima to produce a stacked bar chart showing Total Instance vCPUs for AWS Instance Families used per month for the last 12 months.
This policy allows the user to specify a *Region* to filter results by, and will email the user specified in *Email addresses to notify*.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy supports a single AWS region or the entire Organization.
- This policy produces a stacked-bar chart showing Total Instance vCPUs by Instance Family for the top 8 most used Instance Families. All other Instance Families will be aggregated and displayed as "Other". Values shown in the graph are for the past 12 months.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Region* - Name of the AWS Region to filter by. Example: 'US West (Oregon)'. Leave this blank for 'Organization' scope
- *Email addresses to notify* - A list of email addresses to notify

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
