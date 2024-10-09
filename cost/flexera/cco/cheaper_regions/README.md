# Cheaper Regions Policy

## Deprecated

This policy is no longer being updated. Cloud-specific policies now exist for this functionality and should be used instead:

- [AWS Cheaper Regions](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/cheaper_regions/)
- [Azure Cheaper Regions](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/cheaper_regions/)
- [Google Cheaper Regions](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cheaper_regions/)

## What It Does

This Policy Template determines which regions have cheaper alternatives by specifying the expensive region name and the cheaper region name for analysis

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - The list of Billing centers to check against
- *Email Addresses* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_designer`
  - `policy_manager`
  - `policy_publisher`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## How It Works

- This policy uses a hash to determine existing regions and newer compatible cheaper regions. It checks the billing center and reports on cheaper regions.

## Supported Clouds

- Azure Resource Manager
- Azure CSP
- Google
- Amazon

## Cost

This policy template does not incur any cloud costs.
