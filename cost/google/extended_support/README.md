# Google Cloud Resources Under or Approaching Extended Support

## What It Does

This policy template identifies Google Kubernetes Engine (GKE) clusters and Cloud SQL instances that are currently under extended support or will enter extended support within a configurable number of days. Extended support is a paid tier that allows customers to continue using a software version beyond its standard end-of-life date, incurring additional hourly charges. The policy reports affected resources alongside an estimated monthly extended-support surcharge for each resource.

The policy targets GKE clusters enrolled in the **EXTENDED** release channel (Enterprise tier clusters are excluded, as extended support fees do not apply to them) and Cloud SQL instances running database versions that have entered or are approaching Google's extended support window. Resource data is cross-referenced against a static reference dataset of extended support dates maintained in the Flexera policy catalog.

### Policy Savings Details

The policy includes an estimated monthly extended-support surcharge for each resource. The estimated surcharge represents the incremental cost incurred by remaining on an extended-support version rather than upgrading.

- For **GKE** clusters, the `Estimated Monthly Savings` is calculated as `$0.50/cluster/hr × 730.44` (the average number of hours in a month).
- For **Cloud SQL** dedicated-core instances, the `Estimated Monthly Savings` is calculated as `$0.07/vCPU/hr × vCPU_count × 730.44` (Year 1–2 rate). The vCPU count is derived from the instance tier string (e.g. `db-custom-4-15360` → 4 vCPUs; `db-n1-standard-8` → 8 vCPUs).
- For **Cloud SQL** shared-core instances, the `Estimated Monthly Savings` is calculated as `rate × 730.44` where `db-f1-micro` = `$0.018/hr` and `db-g1-small` = `$0.035/hr` (Year 1–2 rates).
- Rates are maintained in `data/google/google_extended_support_dates.json` using Google's published Year 1–2 extended support pricing. The Year 3 rate doubles. Region-level rate variation is not modeled; a single representative rate is used per engine version.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Estimated Monthly Extended-Support Surcharge`.
- All amounts are reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Minimum Savings Threshold* - Minimum estimated monthly surcharge required to include a resource in the report. Only applies to resources currently under extended support; resources approaching extended support always appear.
- *Days Until Extended Support* - Report resources that will enter extended support within this many days. Set to 0 to only report resources currently under extended support.
- *Allow/Deny Projects* - Whether to allow or deny the projects listed in the *Allow/Deny Projects List* parameter.
- *Allow/Deny Projects List* - A list of allowed or denied Google Cloud project IDs/names. Leave blank to check all projects.
- *Ignore System Projects* - Whether or not to automatically ignore system projects (projects whose ID begins with `sys-`).
- *Ignore Google Apps Script Projects* - Whether or not to automatically ignore Google Apps Script projects (projects whose ID begins with `app-`).
- *Allow/Deny Regions* - Whether to allow or deny the regions listed in the *Allow/Deny Regions List* parameter.
- *Allow/Deny Regions List* - A list of allowed or denied Google region names (e.g. `us-central1`). Leave blank to check all regions.
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

Additionally, this policy template requires that the following APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Kubernetes Engine API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com)
- [Cloud SQL Admin API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
