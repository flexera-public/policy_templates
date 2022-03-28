# Azure Guest Users Audit

## What it does

This policy pulls a list of all guest users on the Azure account. An incident is raised with the list of affected users if any exist so that said users can be reviewed to ensure that they still need to exist.

## Functional Details

A list of users is obtained via the Azure Graph API with a filter for "userType eq 'Guest'". If this list contains any entries, an incident is raised.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Graph API Endpoint* - Azure Endpoint to access the Graph API

## Prerequesites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_graph`

Required permissions in the provider:

- User.Read.All
- Directory.Read.All

## Supported Clouds

- Microsoft Azure

## Cost

This Policy Template does not incur any cloud costs.
