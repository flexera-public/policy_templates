# Azure Web Apps With Unoptimized Scaling

## What It Does

This Policy finds Azure Web Apps with either no autoscaling or poorly configured autoscaling and reports them. Optionally, it will email these recommendations.

## How It Works

- The `microsoft.web/sites` API endpoint is used to gather a list of all Azure Web Apps.
- The `microsoft.insights/autoscalesettings` API endpoint is used to get a list of all Azure autoscaling configurations.
- The `serverFarmId` from the first list is related to the `targetResourceUri` in the second list to find the autoscaling configurations for these Web Apps. These fields represent the id of Azure App Service Plan that powers the Azure Web App.
- The Azure Web Apps are filtered to just those without an autoscaling configuration, or whose autoscaling configuration does not meet the criteria specified in the policy parameters.
  - If no autoscaling configuration is found with the Azure Web App's `serverFarmId`, it is assumed that the Azure Web App does not have autoscaling enabled at all.
  - Each profile in the autoscaling configuration is checked individually. The Azure Web App is considered unoptimized if *any* of the profiles does not meet the criteria specified in the policy parameters.
  - Profiles that do not check the `CpuPercentage` metric and whose `metricTrigger` is not either *greater than* or *greater than or equal to* are ignored.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Highest Minimum Capacity* - The highest setting to permit for autoscaling minimum capacity. Web Apps with a Minimum Capacity higher than this will be considered unoptimized. Set to -1 to not consider Minimum Capacity.
- *Lowest CPU Threshold (%)* - The lowest percentage to permit for CPU Threshold before adding more nodes. Web Apps with a CPU Threshold lower than this will be considered unoptimized. Set to -1 to not consider CPU Threshold.
- *Allow/Deny Subscriptions* - Allow or Deny entered Subscriptions to filter results.
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. Leave blank to check all Subscriptions.
- *Allow/Deny Regions* - Allow or Deny entered regions to filter results.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Leave blank to check all Subscriptions.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.Web/sites/read`
  - `Microsoft.Insights/autoscalesettings/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for meta-policy self-termination; not required if not using the meta parent of this policy template.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
