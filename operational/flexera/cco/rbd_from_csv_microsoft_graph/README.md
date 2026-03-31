# Rule-Based Dimensions from CSV - Microsoft Graph

## What It Does

This policy template creates and updates Flexera Rule-Based Dimensions (RBDs) from a CSV file hosted in OneDrive or SharePoint via the Microsoft Graph API. The CSV uses a `||DIVIDER||` column to separate rule-dimension columns (conditions) from RBD-output columns (values). The policy resolves dimension display names to API IDs at runtime, validates CSV data quality, and uses sentinel rules to safely merge generated rules with manually-created or externally-managed rules.

## How It Works

- **OneDrive mode:** If a Drive ID is provided directly, the policy uses it to list and download files. No SharePoint resolution is performed.
- **SharePoint mode:** If no Drive ID is provided, the policy resolves the specified SharePoint site hostname and site path to a site ID, looks up the document library by name, and uses the resulting drive ID.
- The policy lists files in the specified folder matching the configured prefix and selects the latest file by lexicographic sort (or a specific file if overridden).
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

### Policy Settings

- *Effective Date* - Year/month you want rules to start applying in YYYY-MM format. Default: `2020-01`.
- *Lowercase Values* - Whether to normalize all RBD output values by converting them to lowercase. Prevents case-collision rejections from the API. Default: `No`.
- *RBD ID Filter* - If non-empty, only process the listed RBD column IDs from the CSV. Useful for splitting large CSVs across multiple applied policies to avoid BSON size limits.
- *RBD Name Overrides* - Optional list of RBD ID to display name mappings in `id=Name` format. Example: `rbd_bu=Business Unit`. When empty, display names are auto-derived from the RBD ID.

### Microsoft Graph Settings

- *Drive ID* - The ID of the OneDrive or SharePoint drive containing the CSV file. If provided, SharePoint site/library settings are ignored. Leave empty to use SharePoint site resolution instead.
- *Folder Path* - Path to the folder containing the CSV file, relative to the drive root. Leave empty to use the root folder. Example: `Reports/RBD`.
- *File Name Prefix* - Only files whose name starts with this prefix will be considered. Default: `rbd_`.
- *File Name Override* - If non-empty, forces use of the file with this exact name instead of automatically selecting the latest file by name.

### SharePoint Settings (Optional)

These settings are only used when Drive ID is left empty.

- *SharePoint Site Hostname* - The hostname of the SharePoint site. Example: `contoso.sharepoint.com`.
- *Site Path* - The server-relative path to the SharePoint site. Example: `sites/Finance` or `teams/CostMgmt`.
- *Document Library Name* - The name of the SharePoint document library. Default: `Documents`.

## Policy Actions

- Raises an incident with CSV validation findings (errors, warnings, informational items)
- Raises an incident with RBD creation/update summary
- Creates or updates Rule-Based Dimensions via the Flexera API
- Applies merged rule sets for each RBD at the specified effective date

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Microsoft Graph Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) (*provider=azure_graph*) which has the following Microsoft Graph API permissions:
  - `Files.Read.All` (Application permission) — required for all modes
  - `Sites.Read.All` (Application permission) — required only for SharePoint mode

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### OneDrive Mode — Finding Your Drive ID

To find your OneDrive drive ID, you can use the Microsoft Graph Explorer:

1. Go to [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
1. Sign in with your Microsoft account
1. Run the query: `GET https://graph.microsoft.com/v1.0/me/drive`
1. The `id` field in the response is your drive ID

For a specific user's drive (with application permissions):
`GET https://graph.microsoft.com/v1.0/users/{user-id}/drive`

### SharePoint Mode — Finding Your Site Path

The site path is the portion of the SharePoint URL after the hostname. For example:

- URL: `https://contoso.sharepoint.com/sites/Finance` → Hostname: `contoso.sharepoint.com`, Site Path: `sites/Finance`
- URL: `https://contoso.sharepoint.com/teams/CostMgmt` → Hostname: `contoso.sharepoint.com`, Site Path: `teams/CostMgmt`

### Multiple Applied Policy Instances

If you apply this policy template multiple times (e.g. with different CSV files or different RBD ID Filter values), each applied policy **must have a distinct name**. The policy uses sentinel rules containing the applied policy name to track which rules it manages. If two applied policies share the same name, their sentinel blocks will collide and overwrite each other.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
