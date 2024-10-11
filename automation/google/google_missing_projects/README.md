# Google Missing Projects

## What It Does

This policy checks the stored Flexera CCO billing data for Google from 3 days ago to obtain a list of Google Projects that we have billing data for and compares that to the list of Google Projects returned by the Google Cloud Resource Manager API. An incident is raised and email sent containing any projects present in Flexera CCO but not returned by the Google Cloud Resource Manager API, as well as projects returned by the Google Cloud Resource Manager API but not present in Flexera CCO. The user can select which of those two reports they'd like to produce.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Report Selection* - Whether to report Projects missing in the Google Cloud Resource Manager API but present in CCO data, the opposite, or both.
- *Projects Ignore List* - A list of Project IDs/names to never include in the results. Leave blank to not filter results.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
