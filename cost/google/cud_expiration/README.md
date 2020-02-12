# Google Expiring Committed Use Discount (CUD)

## What it does

This policy identifies all active CUDs that exist in a given GCP project that will be expiring in a set number of days.

## Functional Details

- Uses the GCP API to get a list of all CUDs and sends a notification.
- Create a service account (if none exist) with `owner` role under Google-cloud platform (IAM & admin -> service accounts). Generate key, a JSON file will get downloaded in which you can find 'client email' and 'private key' which has to be added as credentials in RightScale cloud management Design -> Credentials with name 'GC_SA_CLIENT_EMAIL' and 'GC_SA_PRIVATE_KEY' respectively.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Identify CUDs that are expiring in the given number of days* - Number of days before a CUD expires to alert on

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `compute.commitments.list` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
