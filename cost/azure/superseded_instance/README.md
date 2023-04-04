# Azure Superseded Instances Policy Template

## What it does

The Azure Superseded Instances Policy Template is used to monitor an account a generate a list of superseded instances. This policy supports Azure and AzureCSP. The resulting incident will include an estimated savings based on the list price for the current instance size and the new recommended size.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Usage

This policy used Optima data to get a list of instances used in the month and their possible new types, as well it uses data in [Policies Data](https://github.com/flexera-public/policy_templates/tree/master/data) to determine if an instance type has been superseded.  It will then list all the instances that have been superseded and their types. The `Monthly Estimated Cost` is an estimated cost for the instances with the current configuration, you will save a portion of that by moving to the instance type, the new instance types should be more performant as well. If the **New Instance Type** value in the incident report is "Unavailable", the current instance type does not currently exist in our Instance Type mapping. Please raise an issue for the mapping to be updated with the current instance type.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Billing Center Name* - List of Billing Center Names to check
- *Minimum Savings Threshold* - Specify the minimum monthly savings value required for a recommendation to be issued on a per resource basis. Example: 1.00

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
