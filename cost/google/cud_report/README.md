# Google Committed Use Discount (CUD)

## What it does

This policy identifies all CUDs that exist in a given GCP project and sends a notification. It can optionally send a notification on all CUDs or only those that are active or expired.

## Functional Details

- Uses the GCP API to get a list of all CUDs and sends a notification.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *CUD Status* - Allow the user to choose from "All", "Active" or "Expired"

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `compute.commitments.get` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
