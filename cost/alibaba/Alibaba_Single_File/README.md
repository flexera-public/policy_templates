# Alibaba Cloud Common Bill Ingestion

## What it does

This Policy Template is used to automatically take Cost Reports from Alibaba Cloud and send them to Flexera CBI so that Alibaba Cloud costs are visible in Flexera One. An incident is raised on every execution of the policy to provide status information to the user.

## Functional Details

- The policy uses the pulls cost exports stored in Alibaba OSS storage account to Flexera CBI (Files must be of a monthly granularity, ie: one export file for each month). This export is to be used when pulling exports that were created for historic months that were not previously setup for a daily export. When applying the policy select specific month, and enter the month to be imported. 
Note: For exports that have a granurlarity of daily see Alibaba_Monthly directory.
- The policy sends those reports, unmodified, into a Flexera CBI endpoint so that they can be ingested and then visible on the platform.
- The policy pulls the single file that represents a full month of cost reporting.
- The policy requires that a valid Alibaba CBI endpoint exists, a valid Alibaba Cloud credential exists in Flexera One, and that the historic exports dates exist.
- Once the month has been imported the policy can be terminated as it does not need to be rerun as historic exports are not updated by Alibaba.

## Input Parameters

This policy has the following input parameters required when launching the policy.
- *Billing Period* - The year and month to process bills for in YYYY-MM format. Example: 2022-09
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
