# Google Recommender Policy

## What it does

This Policy finds Google Recommendations and reports when it finds them.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Recommender to Check* - [Google recommender](https://cloud.google.com/recommender/docs/recommenders) to run the policy against
- *Location* - Location to check, it can be the zone, region or global
- *Project ID* - Google Projects to Query. Leave blank to query all projects.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

The recommender API also needs to be [enabled.](https://cloud.google.com/recommender/docs/enabling#gcloud).

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `resourcemanager.projects.get` permission
- The `roles/recommender.billingAccountCudViewer` role
- The `roles/recommender.cloudAssetInsightsViewer` role
- The `roles/recommender.cloudsqlViewer` role
- The `roles/recommender.computeViewer` role
- The `roles/recommender.firewallViewer` role
- The `roles/recommender.iamViewer` role
- The `roles/recommender.productSuggestionViewer` role
- The `roles/recommender.projectCudViewer` role
- The `roles/recommender.projectUtilViewer` role

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

### API Quotas

The google api sets quotas on the recommender api, which will generate a `429 RESOURCE_EXHAUSTED`. See [Quotas & Limits](https://cloud.google.com/recommender/quotas)
