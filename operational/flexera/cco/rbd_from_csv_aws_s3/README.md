# Rule-Based Dimensions from CSV - AWS S3

## What It Does

This policy template creates and updates Flexera Rule-Based Dimensions (RBDs) from a CSV file hosted in an AWS S3 bucket. The CSV uses a `||DIVIDER||` column to separate rule-dimension columns (conditions) from RBD-output columns (values). The policy resolves dimension display names to API IDs at runtime, validates CSV data quality, and uses sentinel rules to safely merge generated rules with manually-created or externally-managed rules.

## How It Works

- The policy lists objects in the specified S3 bucket matching the configured prefix and selects the latest file by lexicographic sort (or a specific file if overridden).
- The CSV is parsed using an RFC 4180-compliant parser that handles quoted fields, embedded commas, embedded newlines, and escaped quotes.
- Columns to the left of the `||DIVIDER||` column are treated as rule dimensions (conditions). Columns to the right are treated as RBD outputs (values to assign).
- Rule-dimension column headers can use either the Flexera dimension display name (e.g. `Vendor Account`) or the API ID (e.g. `vendor_account`). The policy resolves display names to IDs at runtime by querying the Flexera Bill Analysis API.
- A validation pass checks for structural errors, data-quality warnings, and informational findings. If any error-level findings exist, RBD creation is skipped entirely.
- For each RBD-output column, the policy generates rules and merges them with any existing rules using sentinel delimiter rules. This preserves rules created by other sources (manual UI rules, other applied policies) while allowing this policy to update its own managed block of rules idempotently.
- The sentinel rules use the applied policy name to identify the managed block. If multiple instances of this policy template are applied, each **must have a distinct applied policy name** to avoid sentinel block collisions.

### CSV Format

```csv
Vendor Account,Cloud Vendor,tag_app_code,||DIVIDER||,rbd_business_unit,rbd_cost_center
123456789012,AWS,APP-001,,Engineering,CC-1234
234567890123,AWS,APP-002,,Marketing,CC-5678
```

- The header row is required.
- The `||DIVIDER||` column is required. Its data cells are ignored.
- Rule-dimension headers can be dimension display names or API IDs.
- RBD-output headers become the RBD ID on the Flexera platform and must follow the `rbd_` naming convention.
- Empty RBD cells produce no rule for that RBD for that row.
- Empty rule-dimension cells exclude that dimension from the rule condition for that row.

## Input Parameters

- *Effective Date* - Year/month you want rules to start applying in YYYY-MM format. Default: `2020-01`.
- *Lowercase Values* - Whether to normalize all RBD output values by converting them to lowercase. Prevents case-collision rejections from the API. Default: `No`.
- *RBD ID Filter* - If non-empty, only process the listed RBD column IDs from the CSV. Useful for splitting large CSVs across multiple applied policies to avoid BSON size limits.
- *RBD Name Overrides* - Optional list of RBD ID to display name mappings in `id=Name` format. Example: `rbd_bu=Business Unit`. When empty, display names are auto-derived from the RBD ID.
- *S3 Bucket Hostname* - The full hostname of the S3 bucket containing the CSV file. Example: `my-bucket.s3.us-west-2.amazonaws.com`.
- *S3 File Prefix* - Only S3 objects whose key starts with this prefix will be considered. Default: `rbd_`.
- *S3 File Override* - If non-empty, forces use of this exact S3 object key instead of automatically selecting the latest file by name.

## Policy Actions

- Raises an incident with CSV validation findings (errors, warnings, informational items)
- Raises an incident with RBD creation/update summary
- Creates or updates Rule-Based Dimensions via the Flexera API
- Applies merged rule sets for each RBD at the specified effective date

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `s3:GetObject`
  - `s3:ListBucket`

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Multiple Applied Policy Instances

If you apply this policy template multiple times (e.g. with different CSV files or different RBD ID Filter values), each applied policy **must have a distinct name**. The policy uses sentinel rules containing the applied policy name to track which rules it manages. If two applied policies share the same name, their sentinel blocks will collide and overwrite each other.

## Supported Clouds

- AWS
- Flexera

## Cost

This policy template does not incur any cloud costs.
