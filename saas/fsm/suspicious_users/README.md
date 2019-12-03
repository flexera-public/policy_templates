# SaaS Manager - Suspicious Users

## What it does

This policy will create an incident when Flexera SaaS Manager identifies suspicious users logging into SaaS applications.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve suspicious activities. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with HR roster connected
- Retrieve a Flexera IAM refresh token for authentication
- The Flexera IAM refresh token must then be stored as a RightScale Credential in the account in which this policy will be applied. The credential must be named `FSM_TOKEN`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

- Sends an email notification

## Required Permissions

- admin or credential_viewer in CMP
- Administrator, Application Administrator, Viewer, or Security Administrator in FSM
