# Flexera User Groups from Billing Centers

## What It Does

This policy template automatically creates and manages Flexera IAM User Groups based on the Billing Centers in the organization. For each Billing Center, a corresponding User Group is created and granted a configurable role (`billing_center_viewer` or `billing_center_admin`) scoped to that Billing Center. If a Billing Center is removed or excluded, the corresponding managed User Group is flagged for deletion. The policy template also produces a membership report showing which users belong to each managed group along with adoption metrics.

## How It Works

- The policy template retrieves all Billing Centers and all IAM User Groups in the organization.
- It identifies managed groups by looking for a structured tag in the User Group's `description` field: `Managed by Policy Template: <applied_policy_name> | Billing Center: <billing_center_id>`. This allows multiple instances of the policy template to run simultaneously without conflicting.
- It compares the filtered set of Billing Centers against the set of managed User Groups to determine which groups need to be created or deleted.
- For each managed group with members, the policy template retrieves membership data and enriches it with user login activity to compute adoption statistics (Active, Inactive, Dormant, Never Logged In).
- When the "Create User Groups" action is taken, the policy template creates the User Group via the IAM API and grants the configured role on the corresponding Billing Center.
- When the "Delete User Groups" action is taken, the policy template revokes the access rule and deletes the User Group.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Billing Center Scope* - Whether to create user groups for all Billing Centers, only top-level ones, or only those at a specific level. A specific level can be specified with `L1` through `L9`, `Level 1` through `Level 9`, or `Level1` through `Level9`. Level 1 is equivalent to `Top-Level Billing Centers Only`.
- *Billing Center Names* - Optional list of Billing Center names or IDs to include. If empty, all Billing Centers (per scope setting) are included.
- *Billing Center Names Exclude* - Optional list of Billing Center names or IDs to exclude.
- *Billing Center Role* - The role to grant to the User Group on the Billing Center. Allowed values: `billing_center_viewer`, `billing_center_admin`.
- *User Group Name Prefix* - A prefix to prepend to the Billing Center name when creating the User Group name. Default: `BC:`. Leave empty for no prefix.
- *Billing Center Name Collision Strategy* - How to handle Billing Centers with the same name. `Use Full Path` uses the full hierarchy path (e.g. `North America / Engineering`). `Include BC ID` appends the Billing Center ID. `Allow Collisions` maps identically-named Billing Centers to a single User Group.
- *Automatic Actions* - Actions to automatically take when the policy template finds changes to make. Allowed values: `Create User Groups`, `Delete User Groups`.

## Policy Actions

- Send an email report
- Create User Groups for Billing Centers that do not have a corresponding managed group
- Delete User Groups for Billing Centers that no longer exist or are excluded by filters

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `enterprise_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
