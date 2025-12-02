# Oracle Tag Cardinality Report

## What It Does

This policy template is used to generate a tag cardinality (how many unique values each tag key has) report for Oracle Cloud, along with a list of those unique values for each tag key. The report includes cardinality for all tag values for Oracle Cloud Compartments and Resources.

## How It Works

This policy template performs the following actions:

- Connect to the Oracle Cloud Identity API to get a list of Oracle Compartments along with their tags.
- Connect to the Oracle Cloud Query API to get a list of Oracle Resources along with their tags.

The resource's "definedTags" field is used for tag data, and tag keys are presented with their namespace included.

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Oracle Cloud Root Compartment OCID* - The OCID of the Oracle Cloud root compartment.
- *Primary Oracle Cloud Region* - Primary Oracle Cloud region. Example: us-phoenix-1
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Oracle Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_3335267112_1121578) (*provider=oracle*) which meets the below requirements:
  - `Allow group <group> to inspect all-resources in tenancy`

  Replace `<group>` with a group that the user associated with the Oracle Cloud credential is a member of.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Oracle

## Cost

This policy template does not incur any cloud costs.
