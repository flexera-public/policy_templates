# Azure Web Apps With Unoptimized Scaling

## What It Does

This Policy finds Azure Web Apps with either no autoscaling or poorly configured autoscaling and reports them. Optionally, it will email these recommendations.

## How It Works

- The `microsoft.web/sites` API endpoint is used to gather a list of all Azure Web Apps.
- The `microsoft.insights/autoscalesettings` API endpoint is used to get a list of all Azure autoscaling configurations.
- The `serverFarmId` from the first list is related to the `targetResourceUri` in the second list to find the autoscaling configurations for these Web Apps. These fields represent the id of Azure App Service Plan that powers the Azure Web App.
- The Azure Web Apps are filtered to just those without an autoscaling configuration, or whose autoscaling configuration does not meet the criteria specified in the policy parameters.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Highest Minimum Capacity* - The highest setting to permit for autoscaling minimum capacity. Web Apps with a Minimum Capacity higher than this will be considered unoptimized. Set to -1 to not consider Minimum Capacity.
- *Lowest CPU Threshold (%)* - The lowest percentage to permit for CPU Threshold before adding more nodes. Web Apps with a CPU Threshold lower than this will be considered unoptimized. Set to -1 to not consider CPU Threshold.
- *Allow/Deny Subscriptions* - Allow or Deny entered Subscriptions to filter results.
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. Leave blank to check all Subscriptions.
- *Allow/Deny Regions* - Allow or Deny entered regions to filter results.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Leave blank to check all Subscriptions.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Web/sites/read`
  - `Microsoft.Insights/autoscalesettings/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
