# Azure Expiring Reserved Instances

## What it does

This Policy Template leverages the [Azure API](https://docs.microsoft.com/en-us/rest/api/reserved-vm-instances/reservationorder/list). It will notify only if expiration is within the time frame specified in `Number of days to prior to expiration date to trigger incident` field. It will email the user specified in Email addresses of the recipients you wish to notify.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Email addresses of the recipients you wish to notify
- *Number of days to prior to expiration date to trigger incident* - Number of days before a RI expires to alert on

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequesites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no
credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure`

Required permissions in the provider:

- Microsoft.Capacity/reservationOrders/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

