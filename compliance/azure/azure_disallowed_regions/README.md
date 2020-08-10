# Azure: Disallowed Regions

## What it does

This Policy Template accepts an input that defines which Azure regions are allowed by your compliance policies. Any Azure resource that exists outside of your approved regions will be raised in an Incident. Incidents will escalate to an email notification and will trigger an approval workflow prior to executing Cloud Workflow to delete the resources. If the instance is not able to terminate it will be logged to the CM audit entries.

## Functional Details

- The policy leverages the Azure API to check all resources that exist in a disallowed region.
- When resource in disallowed region is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to terminate resources after manual approval if needed.
- After approving the terminate action, all the resources may not get deleted due to the dependency.
- So, if you find any error about dependency of the resources, those resources will get deleted in next schedule or you can re-execute the policy.
- If there is any error about supported api-version for any of the resource then you need to manually delete the particular resource.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Approved Azure Region(s)* - list of approved Azure regions
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/resources/read
- Microsoft.Resources/subscriptions/resources/delete

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- An email is sent to the Email lists provided of the resources out of compliance.
- Delete any resource that are in regions not in the Approved Regions list.

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
