# Orgs and Clouds Vendor Accounts

## What It Does

This policy generates a list of cross organization Cloud Vendor Accounts connected to Flexera Cloud Cost Optimization based on the bill connection settings for Azure and Google, as well as full list of AWS accounts under the payer account connected for each Flexera Organization.

_Note 1: 'enterprise_manager' user role is required for each organization._

_Note 2: If excluding orgs is needed use only either 'Excluded Organizations' or 'Exclucded organizations IDs' parameter, not both._

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email list* - Email addresses of the recipients you wish to notify
- *Excluded Organizations* - Names of organizations to exclude
- *Excluded Organizations IDs* - Names of organizations to exclude

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `enterprise_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This policy template does not incur any cloud costs.
