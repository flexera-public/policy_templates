# Oracle Cloud Common Bill Ingestion

## What It Does

This policy template automatically takes Cost Reports from Oracle Cloud (OCI) and sends them to Flexera CBI so that Oracle Cloud costs are visible in Flexera One. An incident is raised on every execution of the policy template to provide status information to the user.

## How It Works

- The policy template uses the Oracle Cloud Object Storage API to connect to the bucket containing the Cost & Usage Reports and obtain the relevant reports for the specified month (or current month if none is specified.)
- The policy template then sends those reports, unmodified, into a Flexera CBI endpoint so that they can be ingested and then visible on the platform.
- The policy template does this over the course of multiple runs to avoid hitting memory and other constraints. **It is recommended that the default frequency of 15 minutes be used; the policy may not function correctly or as expected if a longer frequency is selected.**
- The policy template requires that a valid Oracle CBI endpoint exists, a valid Oracle Cloud credential exists in Flexera One, and that Cost & Usage Reporting is enabled in Oracle Cloud.
- It is recommended that this policy template be applied twice, with Month To Ingest set to Current Month for one instance and with it set to Previous Month for the other. This is to ensure that any changes made to Oracle billing data after the month ends are brought into the Flexera platform.

## Input Parameters

- *Month To Ingest* - Whether to process bills for the current month, previous month, or a specific month.
- *Billing Period* - The year and month to process bills for in YYYY-MM format. Only relevant if Specific Month is selected for the Month To Ingest parameter. Example: 2022-09
- *Flexera CBI Endpoint* - The name of the Flexera CBI endpoint to use. Example: cbi-oi-oracle-oraclecloud
- *Oracle Cloud Region* - The region of the Oracle Cloud Object Storage bucket containing the cost and usage reports. Example: us-phoenix-1
- *Oracle Cloud Cost & Usage Bucket* - Name of the Oracle Cloud Object Storage bucket containing the Cost and Usage reports. In most cases, this will be the same as the tenancy OCID.
- *Oracle Cloud Cost & Usage Namespace* - Namespace that contains the bucket with the Cost and Usage reports. Default value of "bling" should be used unless you're retrieving your cost reports from a custom bucket.
- *Oracle Cloud Cost & Usage Prefix* - The object prefix for Cost and Usage reports. Leave blank to not filter objects by prefix. Should be left at default value of "reports/cost-csv/" unless you're retrieving your cost reports from a custom bucket.
- *Block Size* - The number of files to upload with each execution of the policy template. The default value of 20 is recommended.
- *Commit Delay (Hours)* - The number of hours to wait between committing bill uploads. This is to avoid overloading the CBI system and to ensure bill ingestion occurs at a predictable cadence. The default value of 12 is recommended.

## Policy Actions

- Upload Oracle Cloud bills to Flexera Cloud Cost Optimization (CCO)

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `org_owner`

- [**Oracle Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_3335267112_1121578) (*provider=oracle*) which meets the below requirements:
  - `define tenancy usage-report as <ocid>`
  - `endorse group <group> to read objects in tenancy usage-report`

  Replace `<ocid>` with the OCID of the object storage bucket that stores the Cost & Usage Reports. In most cases, this will be the same as the OCID of the Tenancy itself. Replace `<group>` with a group that the user associated with the Oracle Cloud credential is a member of.

Note: Oracle Cloud credentials cannot be added in Flexera One; the [Flexera Credential Management API](https://reference.rightscale.com/cred-management/#/Credentials/Credentials_create_oracle) must be used to create the credential.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Additional Requirements

This policy also requires a valid Oracle CBI endpoint created using the [Flexera Bill Connect API](https://reference.rightscale.com/optima-bill/#/CBIBillConnects/CBIBillConnects_create), as well as Cost & Usage Reporting to be enabled within the Oracle Cloud environment.

## Supported Clouds

- Oracle Cloud (OCI)

## Cost

This policy template does not incur any cloud costs.
