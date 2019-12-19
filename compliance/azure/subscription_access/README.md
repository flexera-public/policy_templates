# Azure Subscription Access

## What it does

This policy checks all users who have Owner or Contributor access to a given Azure subscription and creates an incident whenever that user list changes.

## Functional Details

The policy leverages the Azure RBAC API to get all the users with the given role(s) on the given subscription.
When the list of users that match the criteria changes, an incident is created and the details are reported via email.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Roles to report on* - Can choose to report on Owner, Contributor, or Both

## Actions

- Sends an email notification

## Prerequisites

This policy requires the Azure Resource Manager Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *Azure RM* in the Provider field.  
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Required Permissions

### Required RightScale Roles

- policy_designer
- policy_manager
- policy_publisher
- credential_viewer
- observer

### Azure Required Permissions

- Tenant > Microsoft Graph > Directory.Read.all
- Subscription > Reader

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
