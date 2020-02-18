# AzureAD Group Sync

## What it does

This policy collects groups and their members from AzureAD and synchronizes them to the Flexera Cloud Management Platform

## Functional Details

The policy leverages the Azure AD Graph API to collect groups and their members based on a filter prefix. It then compares them to the groups and members that currently exist in the Flexera CMP and updates the CMP groups to reflect the current membership in AzureAD.

## Pre-requisites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to read groups and users in the target tenant.
- A [configured Identity Provider](https://docs.rightscale.com/platform/guides/configuring_sso/) in the Cloud Management Platform.
- [Groups need to be created](https://docs.rightscale.com/gov/getting_started/gov_groups.html), and have permissions assigned, for each one that you want to synchronize from AzureAD. This policy will NOT create groups, or assign permissions to them, in the CMP.

## Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary APIs as detailed in the [Azure Required Permissions](#Azure-Required-Permissions) section.
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Prefix to filter groups on* - Uses the 'startswith()' odata query to filter AzureAD groups based on a prefix
- *Default Phone Number for New Users* - Use this phone number if the user doesn't have one set in AzureAD.
  - The policy looks for a value in the first item of `businessPhones` attribute of the AzureAD user account.
- *Default Company Name for New Users* - Use this Company Name if the user doesn't have one set in AzureAD
  - The policy looks for a value in the `companyName` attribute of the AzureAD user account.
- *Identity Provider Href* - The Href for the Identity Provider to associate to new users
- *Remove Users* - Remove users from the Organization that are no longer members of a group

## Required RightScale Roles

- enterprise_manager

## Azure Required Permissions

- AzureAD Tenant > Azure Active Directory Graph > Directory.Read.All (Application with Admin Consent)

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
