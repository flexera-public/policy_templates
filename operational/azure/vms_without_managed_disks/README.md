# Azure VMs Not Using Managed Disks

## What it does

This policy checks all Azure VMs and reports on any that are not using Managed Disks, which are the latest offering from Azure and are much easier to manage.

## Functional Details

When a VM that is using unmanaged disks is detected, VM location information as well as unmanaged disk information is reported to the specified users.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Exclusion Tag Key* - an Azure-native instance tag to ignore instances that match the disallowed instance type. Only supply the tag key
- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication

## Prerequisites

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

## Required RightScale Roles

- credential_viewer or admin

## Azure Required Permissions

- Microsoft.Compute/virtualMachines/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
