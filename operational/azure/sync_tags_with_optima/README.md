# Azure Sync Tags with Optima

## What it does

This Policy identifies all Azure tag keys that are not being used as custom dimensions in Flexera Optima.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Exclusion Tag Keys* - list of tag keys that should be excluded from incidents.
- *Minimum Number of Resources* - The minimum number of resources using a specific tag key which should trigger an incident.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Add tags as custom dimensions to Flexera Optima, after an approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- `Reader`

### Optima Permissions

This policy inherits the Flexera Optima permissions of the user that applied the policy.  Users must have the following role(s):

- `enterprise_manager`

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
