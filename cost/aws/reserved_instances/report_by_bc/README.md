# Reserved Instances Report by Billing Center

## Deprecated

This policy is no longer being updated.



This Policy Template generates a custom Reserved Instances report.  The Policy will index all Reserved Instances and then report on only the Reserved Instances that exist within an AWS Account that has been allocated to a specific Billing Center. Currently, only top-level Billing Centers are supported.

**Note:** For the most reliable data, target Billing Centers that are configured with account-based Allocation Rules only.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `actor`
  - `observer`
  - `credential_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - enter the Billing Center Name to run the report agains
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
