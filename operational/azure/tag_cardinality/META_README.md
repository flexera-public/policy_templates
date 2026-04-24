# Meta Parent: Azure Tag Cardinality Report

## Why This Meta Parent Is Manually Maintained

Unlike most meta parent policy templates in this catalog, the `azure_tag_cardinality_meta_parent.pt` file is **not auto-generated** by the meta parent policy compiler. It has been excluded from `tools/meta_parent_policy_compiler/default_template_files.yaml` and must be manually maintained.

## Reason

The Azure Tag Cardinality Report child policy produces an incident where each row represents a single tag key with its cardinality (number of unique values) and a comma-separated list of unique values observed in that Azure Subscription.

When a meta parent policy applies child policies to multiple Azure Subscriptions and then consolidates the child incidents into a single combined incident, a naive approach would simply stack all the rows from all child incidents together. This would be incorrect for a cardinality report because:

- The same tag key appears once per child incident (once per subscription)
- Stacking the rows would produce duplicate entries for each tag key — one per subscription
- Each subscription's cardinality figure is only for that subscription, not the combined total

A correct consolidated cardinality report must:

1. Collect the `value_list` field from every child incident row for each `(type, key)` pair
1. Merge all value lists across all subscriptions into a single combined list
1. Deduplicate the merged list to get the true set of unique values across all subscriptions
1. Recalculate cardinality as the count of those unique combined values

This aggregation logic requires a custom JavaScript implementation that cannot be produced by the generic meta parent policy compiler.

## What the Consolidated Incident Shows

The consolidated incident produced by this meta parent contains one row per unique `(type, key)` pair, where:

- **Type**: The resource scope (`Subscription`, `Resource Group`, or `Resource`)
- **Key**: The tag key name
- **Cardinality**: The number of unique values for this tag key across all Azure Subscriptions
- **Unique Values**: A comma-separated list of all unique values observed across all subscriptions
- **Subscription Count**: The number of Azure Subscriptions where this tag key was found

## Maintenance Notes

When updating the child policy (`azure_tag_cardinality.pt`) in a way that changes its incident output format (field names, value format, summary template text), you must also manually update this meta parent policy to reflect those changes. Specifically:

- The `js_ds_tag_report_combined_incidents` script filters child incidents by checking if the summary contains `"Azure Tag Cardinality Report"` — update this string if the child policy's summary template changes
- The `value_list` field is split on `", "` (comma-space) — if the child policy changes its separator, update the split logic here
- The `type` and `key` fields are used as the grouping key — if these field names change in the child policy, update accordingly

Version the meta parent independently using semantic versioning and update the CHANGELOG for each change.
