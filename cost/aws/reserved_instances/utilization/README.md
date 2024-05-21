# AWS Reserved Instances Utilization

## What It Does

This policy template generates a report of all AWS Reservations whose utilization is below a user-specified threshold.

This Policy Template leverages the AWS Reserved Instances (RI) report. It will notify only if utilization of an RI falls below the value specified in the `Show Reservations with utilization below this value` field. It will email the user specified in `Email addresses of the recipients you wish to notify`

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - Filter reservations for a specific Billing Center/s by entering Billing Center names
- *Show Reservations with utilization below this value (%)* - Number between 1 and 100
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
