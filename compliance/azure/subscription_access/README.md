# Azure Subscription Access

## What It Does

This policy provides a report of all users with Owner or Contributor access to an Azure Subscription. Optionally, it emails this report.

## How It Works

- The [Azure Resource Manager API](https://learn.microsoft.com/en-us/rest/api/resources/) is used to obtain a list of Azure Subscriptions, Azure Role Definitions, and Azure Role Assignments.
- The [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api) is used to obtain a list of Microsoft users.
- The above datasets are mapped to each other to produce a list of users with Owner or Contributor access per Azure Subscription.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure Resource Manager API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Microsoft Graph Endpoint* - The endpoint to send Microsoft Graph API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Roles* - Whether to report on users that are subscription Owners, Contributors, or both.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Authorization/roleDefinitions/read`
  - `Microsoft.Authorization/roleAssignments/read`

- [**Microsoft Graph Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121576) (*provider=azure_graph*) which has the following permissions:
  - `User.Read.All`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
