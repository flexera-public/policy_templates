# Google Rule-Based Dimension From Project Tags

## What It Does

This policy template creates and updates custom Rule-Based Dimensions that surface the specified Google Cloud resource manager tag key short names in the Flexera One platform. Resource manager tags are an organizational governance construct distinct from project labels: they are key-value resources managed at the organization, folder, or project level and can be inherited by resources across the resource hierarchy. This allows costs to be sliced by the values of the tag keys in question. Rules added to these rule-based dimensions manually, or by other policy templates, will not be deleted.

Project tags are retrieved using a single bulk, paginated Cloud Asset Inventory (CAI) API query scoped to the organization, folder, or project specified in the *Cloud Asset Scope* parameter. This avoids per-project API calls entirely. The Cloud Asset Inventory API (`cloudasset.googleapis.com`) must be enabled in the Google Cloud project where the service account credential resides.

NOTE: If applying this policy template multiple times for multiple scopes, please give each applied policy a distinct name. This is to ensure the policy templates do not overwrite each other's work.

NOTE: Unlike labels, resource manager tags use namespaced keys in the format `{parentNamespace}/{keyShortName}`. This policy matches tag keys by their **short name** only (the last path segment). For example, `environment` matches the tag key `myorg.example.com/environment`.

## Input Parameters

This policy template has the following input parameters:

- *Tag Keys* - A list of Google resource manager tag key short names to create custom Rule-Based Dimensions for. Short names are the last path segment of the namespaced key (e.g., `environment` from `myorg.example.com/environment`). Multiple tag keys can be specified for a single dimension by placing a single entry with each tag key separated by a semicolon (;) character. For example, a value of `env;environment;environ` will create one Rule-Based Dimension that checks the short names "env", "environment", and "environ" for values.
- *Dimension Names* - A list of names to give the Rule-Based Dimensions in the Flexera platform. Enter names in the same order as the tag keys in the *Tag Keys* field. Dimension names will be derived from tag keys directly if this list is left empty.
- *Cloud Asset Scope* - The Cloud Asset Inventory scope to search for Google Projects and their resource manager tags. Must be in one of the following formats: `organizations/{id}`, `folders/{id}`, or `projects/{id}`. The Google credential must have the `cloudasset.assets.searchAllResources` permission granted at this scope level.
- *Include Inherited Tags* - Whether to include tags inherited from parent folders and organizations (`Yes`, the default), or only tags directly attached to the Project (`No`). When set to `Yes`, Google's effective tag resolution applies automatically: a tag bound at a closer ancestor overrides the same key bound at a more distant ancestor. When set to `No`, only tags whose binding point is the project itself are considered.
- *Effective Date* - The month and year in YYYY-MM format that you want the rules to apply. This should be left at its default value in most cases to ensure that the rules apply to all costs, including historical costs.
- *Lowercase Values* - Whether or not to normalize all values by converting them to lowercase. Note that, if the same value appears multiple times with different casing, and this option is disabled, the rule-based dimension will be rejected and this policy template will fail.

## Policy Actions

- Create/update rule-based dimensions

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:
  - `resourcemanager.projects.list`
  - `cloudasset.assets.searchAllResources`

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `observer`
  - `rule_based_dimensions_manager`
  - `policy_viewer`

Note: The Cloud Asset Inventory API (`cloudasset.googleapis.com`) must be enabled in the Google Cloud project associated with the service account credential. The `cloudasset.assets.searchAllResources` permission must be granted at the resource scope specified in the *Cloud Asset Scope* parameter.

Note: The `resourcemanager.projects.list` permission must cover at least the same set of Google Projects as the *Cloud Asset Scope* query returns. If this permission is scoped more narrowly than the Cloud Asset Inventory scope, rules for any projects visible to CAI but not to the project list API will be silently omitted from the generated Rule-Based Dimensions.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
