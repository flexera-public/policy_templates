# Alibaba Cloud Common Bill Ingestion

## What it does

This Policy Template is used to automatically take Cost Reports from Alibaba Cloud and send them to Flexera CBI so that Alibaba Cloud costs are visible in Flexera One. An incident is raised on every execution of the policy to provide status information to the user.

## Functional Details

- The policy uses the pulls cost exports stored in Alibaba OSS storage account to Flexera CBI (Files must be of a daily granularity, ie: an export for each day of the month). For exports that have a granurlarity of monthly see Alibaba_Single_File directory.
- The policy then sends those reports, unmodified, into a Flexera CBI endpoint so that they can be ingested and then visible on the platform.
- The policy pulls each file that represents a day of cost reporting. **It is recommended that the default frequency of daily be used**
- The policy requires that a valid Alibaba CBI endpoint exists, a valid Alibaba Cloud credential exists in Flexera One, and that Exports for daily costs be present.
- It is recommended that this policy be applied twice, with Month To Ingest set to Current Month for one instance and with it set to Previous Month for the other. This is to ensure that any changes made to Aalibaa billing data after the month ends are brought into the Flexera platform.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Month To Ingest* - Whether to process bills for the current month, previous month, or a specific month.
- *Billing Period* - The year and month to process bills for in YYYY-MM format. Only relevant if Specific Month is selected for the Month To Ingest parameter. Example: 2022-09
- *Flexera CBI Endpoint* - The name of the Flexera CBI endpoint to use. Example: cbi-oi-alibaba-alibabacloud
- *Alibaba Cloud Region* - The region of the OSS Storage bucket containing the cost exports. Example: oss-cn-shanghai
- *Alibaba Cloud Account ID* - The account number to ingest costs for.
- *Alibaba Cloud Billing Report Bucket* - Alibaba Cloud Object Storage bucket containing the Billing reports. EX: flexera-billing-data.


## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

There are several steps to take in order to get costs to ingest.
1: Create a Storage using OSS within Alibaba Cloud
2: Create Credentials within Alibaba Cloud
3: Create an Alibaba Cloud CBI Endpoint in Flexera
4: Create Logic for Alibaba Cloud CBI Upload
5: Create an Alibaba Cloud Credential in Flexera One
6: Gather Alibaba Cloud Metadata
7: Apply Flexera Policy

Detailed instructions can be found here: https://flexera.atlassian.net/wiki/spaces/FP/pages/2228814857/Alibaba+Cloud+CBI

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Tag values to match this policy: provider: aws, ui: aws`

## Supported Clouds

- Alibaba cloud

## Cost

This Policy Template does not incur any cloud costs.
