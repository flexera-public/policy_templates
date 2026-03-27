# ITAM Overused Licenses

## What It Does

This policy template uses the ITAM Inventories API to look up software licenses and raise an incident if more than the specified percentage of available licenses are in use. The incident provides a detailed list of the affected licenses.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - A list of email address(es) to notify
- *Percentage of License Usage* - The percentage of available licenses in use to consider a license overused
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `fnms_user`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any additional cloud costs.
