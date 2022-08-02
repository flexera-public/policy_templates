# New Service Usage

## What It Does

This policy checks for new services that appear in the bill between the last month and the current run. If any new services are found it will generate and incident. There is an option to include services that have been added but have not generated any cost as of the current run.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Description

- This policy queries optima data for the current month, as well as the last month and does a comparison on `billing center`, `vendor`, `vendor account name`, `region`, and `service` to determine if a new service has been added to the current month's bill.

## Input Parameters

This policy template has the following Input parameters which require value before the policy can be applied.

- *Email addresses* - A list of email addresses to notify
- *Billing Center Name* - List of Billing Center Names to check
- *Include 0 Dollar Items* - Include items that have a `$0.00` run rate at the time of the policy run.

## Actions

Policy actions may include automation to alert or remediate violations found in the Policy Incident. Actions that destroy or terminate a resource generally require approval from the Policy Approver. This policy includes the following actions.

- Sends an email notification

## Supported Clouds

This policy template supports the following clouds:

- AWS
- Azure
- Google

## Costs

This Policy Template does not incur any cloud costs.
