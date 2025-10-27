# Azure Superseded Compute Instances

## What It Does

This policy template checks all the virtual machines in an Azure account to determine if the instance type has been superseded. If it has, the virtual machine is recommended for resizing to a more modern instance type. An incident listing all of these superseded virtual machines is emailed to the user.

## How It Works

- The policy leverages the Azure API to retrieve all virtual machines and then checks them against our internal database to see if their instance type has been superseded.
- Flexera Cloud Cost Optimization (CCO) billing data is pulled for these instances to assess the current cost of the instance as well as grab additional metadata about the instance, such as operating system, needed to calculate savings.
- The recommendation provided for Superseded Instances is a Change Instance Type action; changing instance type can be performed in an automated manner or after approval.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the instance type is changed to the recommended instance type.

- The `Estimated Monthly Cost` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the `Estimated Monthly Cost` of individual resources is obtained from Flexera CCO, it will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The `Estimated Monthly Savings` is calculated as the percentage differences between either the ["Azure VM listed price"](https://github.com/flexera-public/policy_templates/blob/master/data/azure/azure_vm_pricing.json) or ["Instance Size Flexibility Ratio"](https://learn.microsoft.com/en-us/azure/virtual-machines/reserved-vm-instance-size-flexibility) between current instance type and the recommended instance type. More specifically:
  - If the "listed price" of both instance types is available, the `Estimated Monthly Savings` is calculated as ("actual cost" * (1 - "list price of recommended instance type" / "list price of current instance type"))
  - If the "listed price" is unavailable but the "Instance Size Flexibility Ratio" is available, the `Estimated Monthly Savings` is calculated as ("actual cost" * (1 - "Instance Size Flexibility Ratio of recommended instance type" - "Instance Size Flexibility Ratio of current instance type"))
  - If neither the "listed price" nor the "Instance Size Flexibility Ratio" is available, the `Estimated Monthly Savings` will be 0.
- If no cost information for the resource type was found in our internal database, the `Estimated Monthly Savings` will also be 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- If the Flexera organization is configured to use a currency other than USD, the savings values will be converted from USD using the exchange rate at the time that the policy executes.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Change Instance Type" action while applying the policy, all the resources that didn't satisfy the policy condition will have their instance type changed.

## Policy Actions

- Sends an email notification
- Change instance type after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`*

  \* Only required for taking action (changing instance type); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
