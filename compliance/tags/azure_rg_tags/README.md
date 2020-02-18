# Azure: Tag Resources with Resource Group Name

## What it does

This Policy Template will scan all resources in an Azure Resource Manager Subscription, and will raise an incident if any resources are not properly tagged with their corresponding Resource Group name.  When an incident is raised, the Policy escalation will execute Cloud Workflow to tag the resources with the correct Resource Group name.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Tag Key* - the tag key to scan on resources and to utilize when applying new/updated tags on resources  
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- An email is sent to the Email lists provided of the resources out of compliance
- Tag resources with the name of their Resource Group

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/resources/read
- Microsoft.Resources/subscriptions/providers/read

## Supported Clouds

- Azure Resource Manager

## Limitations

**Note:** Azure Classic (Azure Service Manager / ASM) resources are not supported by this Policy.

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
