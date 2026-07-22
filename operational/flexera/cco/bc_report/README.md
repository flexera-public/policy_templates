# Flexera Billing Center Report

## What It Does

This policy template reports on all Billing Centers within the Flexera organization. It retrieves the full Billing Center hierarchy, resolves each Billing Center's parent (if any), and generates an incident listing every Billing Center along with its description, creation/update timestamps, and parent Billing Center. "Unallocated" Billing Centers are excluded from the report. From the incident, a user can optionally rename a Billing Center, update its description, or delete it.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

- Sends an email listing all Billing Centers found in the Flexera organization
- Rename a Billing Center after approval
- Update a Billing Center's description after approval
- Delete a Billing Center after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `billing_center_admin`*

  \* Only required for taking action (renaming a Billing Center, updating a Billing Center's description, or deleting a Billing Center); the policy will still function in a read-only reporting capacity without this role.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- N/A. This policy template reports on Flexera Billing Centers only and does not interact with any cloud provider.

## Cost

This policy template does not incur any additional costs. It only makes lightweight, read-only calls to the Flexera Billing Center API.
