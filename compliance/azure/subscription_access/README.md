# Azure Subscription Access

## What it does

This policy checks all users who have Owner or Contributor access to a given Azure subscription and creates an incident whenever that user list changes.

## Functional Details

The policy leverages the Azure RBAC API to get all the users with the given role(s) on the given subscription.
When the list of users that match the criteria changes, an incident is created and the details are reported via email.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Roles to report on* - Can choose to report on Owner, Contributor, or Both

## Actions

- Sends an email notification

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

This policy requires two Microsoft Azure Resource Manager Credentials.  One credential
must be created for the Resource `Resource Management` and one credential must be created for the Resource `Azure Active Directory`

Resource Management Provider tag value to match this policy: `azure_rm`

Azure Active Directory Provider tag value to match this policy: `azure_graph`

Required permissions in the provider:

- Tenant > Microsoft Graph > Directory.Read.all
- Subscription > Reader

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
