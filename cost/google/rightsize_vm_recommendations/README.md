# Google Rightsize VM Recommender

## What it does

This Policy finds Rightsize Virtual Machine Recommendations and reports when it finds them. These recommendations are based on the optimal machine type to more efficiently use the instance's resources. 

## Input parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Zones* - Location to check, this is zone names
- *Project ID* - Google Projects to Query. Leave blank to query all projects.
- *Exclusion Tag Key:Value* - Cloud native tag (label) to ignore IP addresses. Format: Key:Value.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Log to CM Audit Entries* - Boolean for whether or not to log any debugging information from actions to CM Audit Entries, this should be left set to No on Flexera EU.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

The recommender API also needs to be [enabled.](https://cloud.google.com/recommender/docs/enabling#gcloud).

Here you can also check what are the permissions required depending on the recommender: [https://cloud.google.com/recommender/docs/recommenders](https://cloud.google.com/recommender/docs/recommenders)

## Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `resourcemanager.projects.get` permission
- The `roles/recommender.computeAdmin` role
- The GCP permission `monitoring.timeSeries.list`
- The GCP permission `compute.instances.list`

This policy also requires the GCP Resource Manager API, GCP Compute Engine API, and GCP Recommender API to be enabled.

## Supported clouds

- Google.

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

## API Quotas

The google api sets quotas on the recommender api, which will generate a `429 RESOURCE_EXHAUSTED`. See [Quotas & Limits](https://cloud.google.com/recommender/quotas)

