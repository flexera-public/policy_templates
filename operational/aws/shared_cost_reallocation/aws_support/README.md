# Shared Cost Reallocation - AWS Support

## What It Does

This policy template reallocates AWS Support costs (`OCBPremiumSupport`, `AWSEnterpriseSupport`, `AWSSupportBusiness`, `AWSSupportEnterprise`) to the AWS Linked Accounts within the AWS Organization.  Costs are allocated to each AWS Linked Account based on the percentage of total that account consumed in the bill period.

To reallocate the costs, the policy template uses Flexera's "Common Bill Ingest" (CBI) capability to negate the original cost allocated to the AWS Master Payer Account with negative cost line items, and write the reallocated portions of costs as new line items.

For example, if you are currently paying $15,000 per month for AWS Enterprise Support, those costs are being charged to your AWS Master Account (example ID `123456789012`).  This policy template would push new line items in, first the negative cost line item for -$15,000 allocated to `123456789012`, and in addition N number of line items that sum up to positive +$15,000.

### Example Scenario

#### Before Reallocation

Let's assume you have three AWS Linked Accounts under your AWS Organization:

- **Master Payer Account** (ID: `123456789012`)
- **Linked Account A** (ID: `234567890123`)
- **Linked Account B** (ID: `345678901234`)
- **Linked Account C** (ID: `456789012345`)

In the current billing setup, the entire AWS Support cost of $15,000 is allocated to the Master Payer Account (`123456789012`).

#### After Reallocation

After applying this policy, the AWS Support costs are reallocated based on the percentage of total consumption by each Linked Account. For example:

- **Linked Account A** consumed 50% of the total usage.
- **Linked Account B** consumed 30% of the total usage.
- **Linked Account C** consumed 20% of the total usage.

The reallocated costs would be:

- **Master Payer Account**: -$15,000 (negative cost line item)
- **Linked Account A**: +$7,500 (50% of $15,000)
- **Linked Account B**: +$4,500 (30% of $15,000)
- **Linked Account C**: +$3,000 (20% of $15,000)

### Positive Business Outcomes

- **Accurate Cost Allocation**: Ensures that each AWS Linked Account is charged accurately based on their actual usage, promoting accountability and cost transparency.
- **Simplified Billing**: Reduces the complexity of internal chargeback and financial reporting by automating the reallocation process.
- **Cost Optimization**: Encourages AWS Linked Accounts to optimize their usage and reduce unnecessary costs, as they are directly accountable for their share of the AWS Support costs.

## Input Parameters

- *Bill Connect ID* - Bill Connect ID to use for reallocating costs. Usually does not need to be changed, will be created if not exists.
- *Billing Period* - Billing Period this applied policy will update. Allowed values: *"Previous Month"*, *"Current Month"*, *"Specific Month"*. If *"Specific Month"* is selected, use the *"Billing Period - Specific Month"* parameter to specify the month in \"YYYY-MM\" format.
- *Billing Period - Specific Month* - If *"Specific Month"* is selected for Billing Period, use this parameter to specify the month in `YYYY-MM` format. Example: 2024-01.  This is intended to be used for backfilling/reprocessing reallocation for previous months.
- *Reallocated Cost Granularity* - Reallocated Cost Granularity configures the granularity for the new line items. Typically "Day" is preferred.  For some extremely large environments, you may need to change this to "Month" to prevent Policy Engine timeouts.

## Policy Actions

- Creates Common Bill Ingest Bill Connect if it does not exists.
- Uploads reallocated cost line items to the Common Bill Ingest Bill Connect.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `org_owner`*

  \* The `org_owner` role is only required if the Bill Connect does not already exist.  If the Bill Connect already exists, the `org_owner` role is not required.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
