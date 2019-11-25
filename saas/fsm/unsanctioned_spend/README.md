# SaaS Manager - Unsanctioned Spend Alert

## What it does

This policy will raise an alert when Flexera SaaS Manager identifies unsanctioned spend on SaaS applications.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve the expense data that has been flagged as unsanctioned. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with expense system connected
- Retrieve a Flexera IAM refresh token for authentication
- The Flexera IAM refresh token must then be stored as a RightScale Credential in the account in which this policy will be applied. The credential must be named `FSM_TOKEN`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of Days Back* - Any unsanctioned expenses discovered during this time period will raise an incident
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

- Sends an email notification

## Required Permissions

- admin or credential_viewer in CMP
- Security Administrator or Administrator in FSM
