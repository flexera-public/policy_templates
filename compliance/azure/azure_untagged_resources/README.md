# Azure Untagged Resources

## What it does

Find all Azure resources missing any of the user provided tags with the option to update the resources with the missing tags.
Only the resources that support tags are considered.

## Functional Details

- The policy leverages the AWS API to retrieve a list of all taggable resources in an AWS Account
- Using the 'Tag Keys' parameter, the policy identifies all resources that are missing the tag keys specified by the user.
- The policy outputs resources missing the specified tag keys as well as resources with the specified tag keys but are missing tag values.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked
- *Tags Keys* - List of tag keys e.g., 'Environment' to find resources which are not tagged by the given inputs.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Tagged to the selected resources with given input

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/resources/read
- Microsoft.Resources/subscriptions/providers/read
- Tag Contributor or Contributor [more details](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json)

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
