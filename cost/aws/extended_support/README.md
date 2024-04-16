# AWS Resources Under Extended Support

## What It Does

This policy checks the billing data stored in the Flexera CCO platform for AWS resources that are under extended support. These resources are outdated and AWS charges an extended support fee for continued use. A report is produced containing a list of these resources, and optionally, an email is sent with this report.

## How It Works

- The policy pulls resource-level billing data from the Flexera CCO platform from 3 days ago. This data is filtered to just those resources with a `Usage Type` that contains the string `ExtendedSupport`. Data from 3 days ago is used to ensure that we have available, processed billing data to search through.
- The above is filtered by account or region based on user parameters.
- Finally, the data is normalized by combining costs for individual resources listed multiple times and extrapolating an estimated monthly cost from one day of billing data.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Billing Center List* - List of Billing Center names or IDs you want to report on. Leave blank to report on resources in all Billing Centers.
- *Allow/Deny AWS Accounts* - Whether to treat `Allow/Deny AWS Accounts List` parameter as allow or deny list. Has no effect if `Allow/Deny AWS Accounts List` is left empty.
- *Allow/Deny AWS Accounts List* - A list of allowed or denied AWS Account IDs/names. Leave blank to check all AWS Accounts.
- *Allow/Deny Regions* - Whether to treat `Allow/Deny Regions List` parameter as allow or deny list. Has no effect if `Allow/Deny Regions List` is left empty.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Regions can be entered in pretty format, such as `US East (Ohio)`, or in shorthand format, such as `us-east-2`. Leave blank to check all AWS regions.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
