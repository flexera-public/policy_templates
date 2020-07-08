# Azure: Policy Audit

## What it does

This Policy Template accepts an input that defines which Azure Policies are to be audited.

## Functional Details

- The policy leverages the Azure API to check for assigned policies in all subscriptions the service principal has access to.
- Assigned policies are compared against the list of policies provided.
- An email is sent with details on which policies are assigned and not assigned to each subscription.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Policy Names* - A list of Azure Policies. **Case sensitive.**
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Authorization/policyAssignments/read
- Microsoft.Authorization/policyDefinitions/read

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- A list of resources is sent to the email addresses provided.

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
