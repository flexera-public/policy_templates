# Rule-Based Dimensions to MSP Child Orgs

## What It Does

This policy template synchronizes selected Rule-Based Dimensions from the current Flexera org to MSP child orgs. It determines which vendor accounts belong to each child org by using historical cost allocations from the `rbd_partner_child_org` dimension, then copies only the matching vendor-account rules into each child org. This template is intended to be paired with a separate solution that manages the parent-org Rule-Based Dimensions.

## How It Works

- The policy template reads the selected Rule-Based Dimensions from the current Flexera org.
- It verifies that the `rbd_partner_child_org` Rule-Based Dimension exists so child-org allocation mapping can be used.
- It enumerates MSP child orgs that are visible to the supplied Flexera credential.
- It builds a historical vendor account-to-child-org allocation map starting at `2020-01`, using aggregated-cost requests in windows of no more than 24 months.
- For each selected parent-org Rule-Based Dimension, it keeps only the vendor-account rules whose vendor account is allocated to a given child org.
- It creates or updates matching Rule-Based Dimensions in each child org while preserving rules outside the policy-managed block.
- It reports missing parent-org Rule-Based Dimensions, child orgs that were skipped before updates could be attempted, and stale policy-managed child-org rules that no longer match the selected parent-org dimensions for currently allocated vendor accounts.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify when any incidents are raised.
- *Rule-Based Dimensions* - A list of parent-org Rule-Based Dimension IDs or exact names to synchronize to MSP child orgs.
- *Effective Date* - The month and year in YYYY-MM format for the Rule-Based Dimension rules to synchronize.

## Policy Actions

- Send an email report
- Read selected Rule-Based Dimensions from the current Flexera org
- Discover vendor account allocations to MSP child orgs
- Create and update matching Rule-Based Dimensions in child orgs
- Preserve child-org rules outside the policy-managed block
- Report parent-org Rule-Based Dimensions that could not be found
- Report child-org synchronization issues when updates are skipped before they are attempted
- Report stale policy-managed child-org rules without removing them automatically

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `observer`
  - `billing_center_viewer`
  - `rule_based_dimensions_manager`
  - `org_owner`*

  \* Child-org synchronization requires a **User Refresh Token** credential associated with a user that has sufficient access in the MSP parent org and each target child org.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

The current implementation requires the `rbd_partner_child_org` Rule-Based Dimension in the current org and uses a historical allocation lookback beginning at `2020-01`.

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This policy template does not incur any cloud costs.
