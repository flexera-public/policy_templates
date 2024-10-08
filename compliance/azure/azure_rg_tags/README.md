# Azure Tag Resources with Resource Group Name

## What It Does

This Policy Template will scan all resources in an Azure Resource Manager Subscription, and will raise an incident if any resources are not properly tagged with their corresponding Resource Group name.  When an incident is raised, the Policy escalation will execute Cloud Workflow to tag the resources with the correct Resource Group name.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Tag Key* - the tag key to scan on resources and to utilize when applying new/updated tags on resources
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Tag Resources" action while applying the policy, all the resources will get tagged  with their corresponding resource group name.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- An email is sent to the Email lists provided of the resources out of compliance
- Tag resources with the name of their Resource Group

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/resources/read
- Microsoft.Resources/subscriptions/providers/read

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure Resource Manager

## Limitations

**Note:** Azure Classic (Azure Service Manager / ASM) resources are not supported by this Policy.

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
