# Azure Advisor Compute Instances Recommendations

## What It Does

This policy template reports Azure virtual machine rightsizing recommendations produced by [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview). Optionally, this report can be emailed and the offending instances can be resized.

**NOTE: This policy template will produce recommendations similar to the [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances) policy template. It is recommended that you avoid using both templates at the same time. Otherwise, redundant recommendations may appear in the Flexera One platform, causing inaccuracies in calculated potential savings.**

## How It Works

The policy utilizes the [Azure Advisor API](https://learn.microsoft.com/en-us/rest/api/advisor/recommendations/list?view=rest-advisor-2023-01-01&tabs=HTTP#category) to get a list of recommendations for Azure virtual machines. The specific recommendations produced by Azure Advisor will depend on how it is configured within the Azure environment. Please consult the [relevant Azure documentation](https://learn.microsoft.com/en-us/azure/advisor/advisor-get-started) for more information on how to do this.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is resized to the recommended size. The `Estimated Monthly Savings` are obtained directly from the [Azure Advisor API](https://learn.microsoft.com/en-us/rest/api/advisor/recommendations/list?view=rest-advisor-2023-01-01&tabs=HTTP#category). If the Flexera organization is configured to use a currency other than the one returned by the [Azure Advisor API](https://learn.microsoft.com/en-us/rest/api/advisor/recommendations/list?view=rest-advisor-2023-01-01&tabs=HTTP#category), the savings values will be converted using the exchange rate at the time that the policy executes.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclude Stopped Virtual Machines* - Whether or not to filter stopped virtual machines from the results. If set to `Yes`, only running virtual machines will be included in the results.
- *Exclude Databricks* - Whether or not to filter virtual machines used for Azure Databricks from the results. If set to `Yes`, virtual machines for Azure Databricks will not be included in the results.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Resize Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be resized.

## Policy Actions

- Sends an email notification
- Resize virtual machines after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Advisor/recommendations/read`
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
