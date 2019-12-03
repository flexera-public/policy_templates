# SaaS Manager - Renewal Reminder

## What it does

This policy will create an incident when Flexera SaaS Manager identifies applications whose contract expiration date is approaching.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve SaaS Applications and will generate reminders for applications whose renewals are approaching. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation
- Retrieve a Flexera IAM refresh token for authentication
- The Flexera IAM refresh token must then be stored as a RightScale Credential in the account in which this policy will be applied. The credential must be named `FSM_TOKEN`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Upcoming Number of Days* - If an application renewal is due in the upcoming time period, raise an incident
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

- Sends an email notification

## Required Permissions

- admin or credential_viewer in CMP
- Administrator, Application Administrator, or Viewer in FSM
