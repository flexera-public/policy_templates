# Azure Network Security Groups With Inbound SSH Open

## What It Does

This policy template reports any Azure Network Security Groups that have SSH (TCP port 22) open to the internet. Optionally, it emails this report.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Allow/Deny Subscriptions* - Allow or Deny entered Subscriptions to filter results.
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. Leave blank to check all Subscriptions.
- *Allow/Deny Regions* - Allow or Deny entered regions to filter results.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Leave blank to check all Subscriptions.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Network/networkSecurityGroups/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
