# Azure Subscription Access

## What it does

This policy checks all users who have Owner or Contributor access to a given Azure subscription and creates an incident whenever that user list changes.

## Functional Details

The policy leverages the Azure RBAC API to get all the users with the given role(s) on the given subscription.
When the list of users that match the criteria changes, an incident is created and the details are reported via email. 

## Pre-requisites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`

## Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Roles to report on* - Can choose to report on Owner, Contributor, or Both
- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication

## Required RightScale Roles

- credential_viewer

## Azure Required Permissions

- Tenant > Microsoft Graph > Directory.Read.all
- Subscription > Reader

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
