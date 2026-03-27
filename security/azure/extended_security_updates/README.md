# Azure Resources Under Extended Security Updates

## What It Does

This policy template reports Azure virtual machines running operating systems that are under or past Microsoft's Extended Security Updates (ESU) program. These resources are outdated and running on unsupported software, representing a security risk to the organization. A report is produced containing a list of these resources, and optionally, an email is sent with this report.

> **Note:** Microsoft provides Extended Security Updates at no additional charge for virtual machines hosted in Azure. This policy is therefore categorized as a Security policy rather than a Cost policy — the goal is to identify outdated resources for remediation, not to report costs.

## How It Works

- The policy queries the Azure Compute API to list all virtual machines across the specified subscriptions.
- The OS image reference of each VM (publisher, offer, and SKU) is checked against a known list of end-of-life operating systems and SQL Server versions that are eligible for or past Microsoft's Extended Security Updates program.
- VMs without a standard Azure Marketplace image reference (e.g., created from custom images, managed images, or Shared Image Gallery images) may not be detected and are excluded from results.
- The results are filtered by subscription, region, and tags based on user parameters.

### Detected Operating Systems

The following end-of-life operating system and SQL Server versions are detected by checking the Azure Marketplace image publisher, offer, and SKU of each VM:

| OS / Software Version | End of Life Date | ESU End Date | ESU Status |
| --- | --- | --- | --- |
| Windows Server 2008/R2 | 2020-01-14 | 2023-01-10 | ESU Ended |
| Windows Server 2012/R2 | 2023-10-10 | 2026-10-13 | Under Extended Security Updates |
| Windows 7 | 2020-01-14 | N/A | End of Life - No ESU Available |
| SQL Server 2008/R2 | 2019-07-09 | 2022-07-12 | ESU Ended |
| SQL Server 2012 | 2022-07-12 | 2025-07-08 | Under Extended Security Updates |
| SQL Server 2014 | 2024-07-09 | N/A | End of Life - No ESU Available |

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using Azure China.
- *Allow/Deny Subscriptions* - Whether to treat `Allow/Deny Subscriptions List` parameter as allow or deny list. Has no effect if `Allow/Deny Subscriptions List` is left empty.
- *Allow/Deny Subscriptions List* - A list of allowed or denied subscription IDs/names. Leave blank to check all Azure subscriptions.
- *Allow/Deny Regions* - Whether to treat `Allow/Deny Regions List` parameter as allow or deny list. Has no effect if `Allow/Deny Regions List` is left empty.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Regions can be entered in pretty format, such as `East US`, or in shorthand format, such as `eastus`. Leave blank to check all Azure regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources where the tag key:value pair is not equal to the specified value.
  - `Key=~Value` - Filter all resources where the tag value matches the specified regex string.
  - `Key!~Value` - Filter all resources where the tag value does not match the specified regex string.
- *Exclusion Tags: Any / All* - Whether to filter resources containing any of the specified tags or only those that contain all of them.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to `0` to not show an incident table at all, and `100000` to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.Compute/virtualMachines/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
