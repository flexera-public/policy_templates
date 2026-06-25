# Google Cloud Resources Under or Approaching Extended Support

## What It Does

This policy template identifies Google Kubernetes Engine (GKE) clusters and Cloud SQL instances that are currently under extended support or will enter extended support within a configurable number of days. Extended support is a paid tier that allows customers to continue using a software version beyond its standard end-of-life date, incurring additional hourly charges. The policy reports affected resources alongside an estimated monthly extended-support surcharge for each resource.

The policy targets GKE clusters enrolled in the **EXTENDED** release channel (Enterprise tier clusters are excluded, as extended support fees do not apply to them) and Cloud SQL instances running database versions that have entered or are approaching Google's extended support window. Resource data is cross-referenced against a static reference dataset of extended support dates maintained in the Flexera policy catalog.

### Policy Savings Details

The policy includes an estimated monthly extended-support surcharge for each resource. The estimated surcharge represents the incremental cost incurred by remaining on an extended-support version rather than upgrading.

- For **GKE** clusters, the `Estimated Monthly Savings` is calculated as `flat_per_cluster_hour_rate × 730.44` (the average number of hours in a month), using the rate stored in the reference data file.
- For **Cloud SQL** dedicated-core instances, the `Estimated Monthly Savings` is calculated as `per_vCPU_hour_rate × vCPU_count × 730.44`. The vCPU count is derived from the instance tier string (e.g. `db-custom-4-15360` → 4 vCPUs; `db-n1-standard-8` → 8 vCPUs).
- For **Cloud SQL** shared-core instances (`db-f1-micro`, `db-g1-small`), the `Estimated Monthly Savings` is calculated as `per_instance_hour_rate × 730.44`, using the `shared_core_hourly_rate` from the reference data.
- Rates are maintained in `data/google/gcp_extended_support_dates.json` and approximate Google's published extended support pricing. Region-level rate variation is not modeled; a single representative rate is used per engine version.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Estimated Monthly Extended-Support Surcharge`.
- All amounts are reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Project ID* - Leave blank; this is for automated use with Meta Policies. See the [README for Meta Policies](https://github.com/flexera-public/policy_templates/blob/master/README_META_POLICIES.md) for more details.
- *Minimum Savings Threshold* - Minimum estimated monthly surcharge required to include a resource in the report. Only applies to resources currently under extended support; resources approaching extended support always appear.
- *Days Until Extended Support* - Report resources that will enter extended support within this many days. Set to 0 to only report resources currently under extended support.
- *Allow/Deny Projects* - Whether to allow or deny the projects listed in the *Allow/Deny Projects List* parameter.
- *Allow/Deny Projects List* - A list of allowed or denied Google Cloud project IDs/names. Leave blank to check all projects.
- *Allow/Deny Regions* - Whether to allow or deny the regions listed in the *Allow/Deny Regions List* parameter.
- *Allow/Deny Regions List* - A list of allowed or denied GCP region names (e.g. `us-central1`). Leave blank to check all regions.
- *Exclusion Labels* - Cloud native labels to ignore resources. Enter the Key name to filter resources with a specific Key regardless of Value, or `Key==Value` to filter a specific pair. Regex operators `=~` and `!~` are also supported.
- *Exclusion Labels: Any / All* - Whether to filter resources containing any of the specified labels or only those that contain all of them.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:
  - `container.clusters.list`
  - `resourcemanager.projects.get`
  - `cloudsql.instances.list`

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `observer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
