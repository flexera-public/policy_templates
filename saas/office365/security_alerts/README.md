# Office 365 Security Alerts

## What it does

This policy will identify Security Alerts that have been raised in Office 365. Policy Managers can minimize the notifications by choosing to only be alerted by certain severity level(s).

## Functional Description

This policy integrates with the Microsoft Graph API to retrieve Office 365 Security Alerts.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure AD Tenant ID* - This value needs to be your Azure tenant ID. To get your tenant ID see [this article](https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id)
- *Alert Severity* - Specify the alert severity levels that should raise an incident
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

- Sends an email notification

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no
credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed: 

Provider tag value to match this policy: `microsoft`

Required permissions in the provider:

- SecurityEvents.Read.All and SecurityEvents.ReadWrite.All in Azure AD
