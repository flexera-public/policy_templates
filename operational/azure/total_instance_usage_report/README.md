# Azure Usage Report - Instance Time Used

## What It Does

This Policy Template leverages Flexera CCO APIs to produce a stacked bar chart showing Total Instance Time for Azure Virtual Machine Families used per month for the last 12 months. The user can specify which unit of time and which instance spec to use to normalize time against; for example, a chart can be produced for total instance vCPU hours. The data feeding this chart can be filtered by Azure region or Flexera Billing Center if desired. Optionally, the result can be emailed.

## How It Works

- This policy supports a single Azure region or the entire Organization.
- This policy produces a stacked-bar chart showing Total Instance Units by Virtual Machine Family for the top 8 most used Virtual Machine Families. All other Virtual Machine Families will be aggregated and displayed as "Other". Values shown in the graph are for the past 12 months.
- The unit used for normalizing instance usage depends on the value of the `Instance Unit` parameter.
- The unit used for time depends on the value of the `Time Unit` parameter.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Months Back* - How many months to go back in the chart/incident.
- *Instance Unit* - Instance (Virtual Machine) unit to normalize usage against. Supported units:
  - `Normalized Instance Count` - Normalize the data against each [Instance Size Flexibility (ISF) Ratio](https://learn.microsoft.com/en-us/azure/virtual-machines/reserved-vm-instance-size-flexibility) of each Virtual Machine instance.
  - `vCPUs` - Normalize the data against each vCPU of each Virtual Machine instance.
  - `Memory (GiB)` - Normalize the data against each GiB of total memory of each Virtual Machine instance.
- *Time Unit* - Unit of time to use for results. The `Instance Unit` will be normalized to this time unit. Units are calculated as follows:
  - `Hours` - 1 hour.
  - `Days` - 24 hours.
  - `Weeks` - 168 hours e.g. 7 days * 24 hours.
  - `Months` - 730 hours e.g. 365 days / 12 months * 24 hours.
  - `Years` - 8760 hours e.g. 365 days * 24 hours.
- *Allow/Deny Regions* - Whether to treat `Allow/Deny Regions List` parameter as allow or deny list. Has no effect if `Allow/Deny Regions List` is left empty.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Example: `US East`. Leave blank to check all regions.
- *Allow/Deny Billing Centers* - Whether to treat `Allow/Deny Billing Center List` parameter as allow or deny list. Has no effect if `Allow/Deny Billing Center List` is left empty.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to check all Billing Centers.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
