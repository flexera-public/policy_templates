# Office 365 Security Alerts

## What it does

This policy will identify Security Alerts that have been raised in Office 365. Policy Managers can minimize the notifications by choosing to only be alerted by certain severity level(s).

## Functional Description

This policy integrates with the Microsoft Graph API to retrieve Office 365 Security Alerts. Therefore the following are prerequisites for this policy to execute:

- Office 365 implementation
- Azure Active Directory Application with the appropriate permissions to manage the Office 365 tenant
- The Azure AD Application ID and Secret must then be stored as a RightScale Credential in the account in which this policy will be applied. The credentials must be named `O365_AAD_APPLICATION_ID` and `O365_AAD_APPLICATION_KEY`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure AD Tenant ID* - This value needs to be your Azure tenant ID. To get your tenant ID see [this article](https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id)
- *Alert Severity* - Specify the alert severity levels that should raise an incident
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

- Sends an email notification

## Required Permissions

- admin or credential_viewer in CMP
- SecurityEvents.Read.All and SecurityEvents.ReadWrite.All in Azure AD
