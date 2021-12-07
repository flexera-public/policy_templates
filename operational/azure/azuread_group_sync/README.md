# AzureAD Group Sync

## What it does

This policy collects groups and their members from AzureAD and synchronizes them to the Flexera Cloud Management Platform.

## Functional Details

This policy leverages the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/api/overview?toc=./ref/toc.json&view=graph-rest-1.0) to collect groups and their members based on a filter prefix. It then compares them to the groups and members that currently exist in the Flexera CMP and updates the CMP groups to reflect the current membership in AzureAD.

The policy will recurse through all child groups and flatten their membership in the matching parent CMP group.

If users do not exist in the CMP, they are created using the information gathered from AzureAD.

You can elect to automatically remove users from your organization that are no longer members of any groups by setting selecting the `Remove Users?` parameter.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Prefix to filter groups on* - Uses the `startswith()` odata query to filter AzureAD groups based on a prefix
  - Example: `FLEXERA_CMP_`
- *Default Phone Number for New Users* - Use this phone number if the user doesn't have one set in AzureAD.
  - The policy looks for a value in the first item of `businessPhones` attribute of the AzureAD user account.
- *Default Company Name for New Users* - Use this Company Name if the user doesn't have one set in AzureAD
  - The policy looks for a value in the `companyName` attribute of the AzureAD user account.
- *Identity Provider Href* - The Href for the Identity Provider to associate to new users
  - Can be retrieved by copying the link to edit your SSO: `https://us-3.rightscale.com/global/enterprises/<ACCOUNT_ID>/edit_sso?identity_provider_id=<IDP_ID>` and grabbing the IDP ID value at the end, or via the [RightScale Cloud Management API](https://reference.rightscale.com/api1.5/resources/ResourceIdentityProviders.html#index)
  - Example: `/api/identity_providers/<IDP_ID>`
- *Remove Users?* - Remove users from the Organization that are no longer members of a group

## Actions

- Synchronizes group memberships in CMP from AzureAD

## Pre-requisites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to read groups and users in the target tenant.
- A [configured Identity Provider](https://docs.rightscale.com/platform/guides/configuring_sso/) in the Cloud Management Platform.
- [Groups need to be created](https://docs.rightscale.com/gov/getting_started/gov_groups.html), and have [permissions assigned](https://docs.rightscale.com/gov/getting_started/gov_groups.html#roles), for each one that you want to synchronize from AzureAD. This policy will NOT create groups, or assign permissions to them, in the CMP.
- This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. [The information below](#Credential-Configuration) should be consulted when creating the credential.
- The policy must be applied by a user with the `enterprise_manager` role.

### Credential Configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

### Credential #1

Type: `Microsoft Azure Resource Manager`
Tenant Id: [See documentation](https://docs.rightscale.com/policies/users/guides/credential_management.html#azure-resource-manager)
Client Id: [See documentation](https://docs.rightscale.com/policies/users/guides/credential_management.html#azure-resource-manager)
Client Secret: [See documentation](https://docs.rightscale.com/policies/users/guides/credential_management.html#azure-resource-manager)
Resource: `Azure Active Directory`

Required permissions in the provider:

- Tenant > Microsoft Graph > User.Read.All (Application with Admin Consent)
- Tenant > Microsoft Graph > Group.Read.All (Application with Admin Consent)

![Enterprise Application Permissions](enterprise_app_permissions.png)

## Supported Services

- AzureAD

## Cost

This Policy Template does not incur any cloud costs.
