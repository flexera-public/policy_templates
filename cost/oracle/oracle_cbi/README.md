# Oracle Cloud Common Bill Ingestion

## What it does

This Policy Template is used to automatically take Cost Reports from Oracle Cloud (OCI) and send them to Flexera CBI so that Oracle Cloud costs are visible in Flexera One. An incident is raised on every execution of the policy to provide status information to the user.

## Functional Details

- The policy uses the Oracle Cloud Object Storage API to connect to the bucket containing the Cost & Usage Reports and obtain the relevant reports for the specified month (or current month if none is specified.)
- The policy then sends those reports, unmodified, into a Flexera CBI endpoint so that they can be ingested and then visible on the platform.
- The policy does this over the course of multiple runs to avoid hitting memory and other constraints; it is recommended that the default frequency of 15 minutes be used.
- The policy requires that a valid Oracle CBI endpoint exists, a valid Oracle Cloud credential exists in Flexera One, and that Cost & Usage Reporting is enabled in Oracle Cloud.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Period* - The year and month to process bills for in YYYY-MM format. Leave this parameter blank to always do the current month. Example: 2022-09
- *Flexera CBI Endpoint* - The name of the Flexera CBI endpoint to use. Example: cbi-oi-oracle-oraclecloud
- *Oracle Cloud Region* - The region of the Oracle Cloud Object Storage bucket containing the cost and usage reports. Example: us-phoenix-1
- *Oracle Cloud Cost & Usage Bucket* - OCID of the Oracle Cloud Object Storage bucket containing the Cost and Usage reports.
- *Block Size* - The number of files to upload with each execution of the policy. Changing from the default value of 20 is not recommended.
- *Commit Delay (Hours)* - The number of hours to wait between committing bill uploads. This is to avoid overloading the CBI system and to ensure bill ingestion occurs at a predictable cadence. The default value of 12 is recommended.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

This policy also requires a valid Oracle CBI endpoint created using the [Flexera Bill Connect API](https://reference.rightscale.com/optima-bill/#/CBIBillConnects/CBIBillConnects_create), as well as Cost & Usage Reporting to be enabled within the Oracle Cloud environment.

Additionally, the policy requires that the Flexera Bill Upload limit be increased to 125 on your Flexera One organization. Please contact [Flexera Support](https://community.flexera.com/t5/Using-the-Case-Portal/Contact-Flexera-support/ta-p/94684) to have this done.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `oracle`

Required permissions for the Oracle policy:

- define tenancy usage-report as [OCID]
- endorse group [Group] to read objects in tenancy usage-report

[OCID] should be replaced with the OCID shown on the Cost & Usage Reports page in Oracle Cloud's web UI. [Group] should be replaced with a group that the user associated with the Oracle Cloud credential is a member of.

Note: Oracle Cloud credentials cannot be added in Flexera One; the [Flexera Credential Management API](https://reference.rightscale.com/cred-management/#/Credentials/Credentials_create_oracle) must be used to create the credential.

## Supported Clouds

- Oracle Cloud (OCI)

## Cost

This Policy Template does not incur any cloud costs.
