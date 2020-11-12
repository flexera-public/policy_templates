# Azure Old Snapshots

## What it does

This Policy finds Azure snapshots older than the specified days and deletes them.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day's cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is N/A. The incident message detail includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.
If the user is missing the minimum required role of `billing_center_viewer` or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as N/A in the incident table.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Snapshot age* - The number of days since the snapshot was created.
- *Exclusion Tags* - list of tags that a snapshot can have to exclude it from the list.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Snapshots" action while applying the policy, all the snapshots that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Compute/snapshots/read
- Microsoft.Compute/snapshots/delete

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
