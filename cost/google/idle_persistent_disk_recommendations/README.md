# Google Idle Persistent Disk Recommender

## What it does

This Policy finds Idle Persistent Disk Recommendations and reports when it finds them. You can then delete the idle volumes

### How it works

This policy uses the GCP recommender `google.compute.disk.IdleResourceRecommender`, which checks if a resource has not been attached to a VM or other resource for 15 days, the recommender classifies that resource as idle.

Idle resource recommendations begin 15 days after resource creation, and they are updated once every 24 hours.

It is important that the policy GCP credentials have at least one of the following roles:

- `recommender.computeAddressIdleResourceRecommendations.list`

You also need to [enable the Recommender API](https://console.cloud.google.com/flows/enableapi?apiid=recommender.googleapis.com)

Check the following official GCP docs for more:

- [Viewing and applying idle resources recommendations](https://cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Zone* - Location to check, it is specifically Google zones
- *Project ID* - Google Projects to Query. Leave blank to query all projects.
- *Unattached Days* - Days a volume has been unattached. Default is 30 days

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete volume after an approval

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

The recommender API also needs to be [enabled.](https://cloud.google.com/recommender/docs/enabling#gcloud).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required APIs to have enabled in the provider:

- Resource Manager API
- Compute Engine API
- Recommender API

Required permissions in the provider:

- resourcemanager.projects.get
- compute.disks.list

Required roles in the provider:

- Compute Recommender Viewer
- Compute Recommender Admin*

\* Only required for taking action (deletion); the policy will still function in a read-only capacity without these permissions.

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

### API Quotas

The google api sets quotas on the recommender api, which will generate a `429 RESOURCE_EXHAUSTED`. See [Quotas & Limits](https://cloud.google.com/recommender/quotas)
