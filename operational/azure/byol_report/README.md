# Azure Bring-Your-Own-License (BYOL) Report

## What It Does

This policy analyzes the stored billing data for Microsoft Azure from 2 days ago to a user-specified number of days back and reports on the number of VMs using the Bring-Your-Own-License (BYOL) feature each day. The report includes daily numbers and percentages as well as the peak total BYOL usage and peak percentage BYOL usage and is emailed to a user-specified list of email addresses.

## Functional Details

- The policy leverages the Flexera Optima API to retrieve amortized costs and metadata for Azure virtual machines on a per-subscription basis. Costs for the most recent 2 days are ignored due to the high likelihood of cost data this recent being incomplete.
- The `Operating System` dimension is used to determine if each virtual machine is using Bring-Your-Own-License (BYOL) or not. The following values for this dimension are considered BYOL: Red Hat BYOS, SUSE BYOS, Windows Server BYOL, Windows Client BYOL
- The total number of virtual machines, the number using BYOL, and the percentage using BYOL are calculated for each day based on the above data.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Look Back Period (Days)* - How far back, in days, to report on Azure virtual machines that utilize Bring-Your-Own-License (BYOL).

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
