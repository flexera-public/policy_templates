# Google Cloud SQL Idle Instance Recommender

## What it does

This Policy finds Idle Cloud SQL Instance Recommendations and reports when it finds them. You can then delete the idle volumes

### How it works

This policy uses the GCP recommender `google.cloudsql.instance.IdleRecommender`, which analyzes the usage metrics of primary instances that are **older than 30 days**. For each instance, the recommender considers the values of certain [metrics](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-cloudsql) within an observation period spanning the last 30 days. The recommender **does not** analyze read replicas.

If the activity level within the observation period is below a certain threshold, the recommender estimates that the instance is idle. Recommendations are generated every 24 hours for shutting down such instances.

It is important that the policy GCP credentials have at least one of the following roles:

- `recommender.cloudsqlViewer`
- `cloudsql.viewer`

You also need to [enable the Recommender API](https://console.cloud.google.com/flows/enableapi?apiid=recommender.googleapis.com)

Check the following official GCP docs for more:

- [Identify idle Cloud SQL instances](https://cloud.google.com/sql/docs/sqlserver/recommender-sql-idle)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify.
- *Regions* - Regions to query. Leave blank to query all available regions.
- *Project IDs* - Google Projects to query. Leave blank to query all projects.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

The recommender API also needs to be [enabled.](https://cloud.google.com/recommender/docs/enabling#gcloud).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required APIs to have enabled in the provider:

- Resource Manager API
- Cloud SQL Admin API
- Recommender API

Required permissions in the provider:

- resourcemanager.projects.get
- cloudsql.instances.list
- recommender.cloudsqlIdleInstanceRecommendations.list

Required roles in the provider:

- Cloud SQL Recommender Viewer

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

### API Quotas

The google api sets quotas on the recommender api, which will generate a `429 RESOURCE_EXHAUSTED`. See [Quotas & Limits](https://cloud.google.com/recommender/quotas)
