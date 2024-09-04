# Azure Advisor Carbon Reduction Recommendations

## What It Does

This policy template reports Azure carbon reduction recommendations produced by [Azure Advisor](https://learn.microsoft.com/en-us/azure/advisor/advisor-overview). Optionally, this report can be emailed.

## How It Works

The policy utilizes the [Azure Advisor API](https://learn.microsoft.com/en-us/rest/api/advisor/recommendations/list?view=rest-advisor-2023-01-01&tabs=HTTP#category) to get a list of cost recommendations and filters them for ones that contain carbon savings. The specific recommendations produced by Azure Advisor will depend on how it is configured within the Azure environment. Please consult the [relevant Azure documentation](https://learn.microsoft.com/en-us/azure/advisor/advisor-get-started) for more information on how to do this.

### Carbon Reduction Details

The policy includes the estimated monthly carbon savings. Savings are measured in kilograms of CO2 (Carbon Dioxide) and are [calculated internally by Microsoft Azure](https://learn.microsoft.com/en-us/azure/carbon-optimization/).

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Advisor/recommendations/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
