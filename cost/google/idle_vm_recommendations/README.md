# Google Idle VM Recommender

## Deprecated

This policy is no longer being updated. The [Google Rightsize VM Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_recommendations) policy now includes this functionality and is the recommended policy for getting idle VM recommendations.



This Policy finds Idle Virtual Machine Recommendations and reports when it finds them. You can then delete the idle instances

### How it works

This policy uses the GCP recommender `google.compute.instance.IdleResourceRecommender`, which identifies instances (VM) that have not been used over the previous 1 to 14 days, or, for new VMs, starting one day after VM creation: the algorithm considers the CPU and network usage in the last observation period. If CPU and network usage are below predefined thresholds, the Recommender classifies the VM as idle.

After a VM is created and running for at least one day during the observation period, Compute Engine begins generating idle VM recommendations for it. New recommendations are generated once per day.

It is important that the policy GCP credentials have at least one of the following permissions:

- `recommender.computeInstanceIdleResourceRecommendations.list`

You also need to [enable the Recommender API](https://console.cloud.google.com/flows/enableapi?apiid=recommender.googleapis.com)

Check the following official GCP docs for more:

- [How detection of idle VM instances works](https://cloud.google.com/compute/docs/instances/idle-vm-recommendations-overview#how_detection_of_idle_vm_instances_works)
- [Viewing idle VM instance recommendations](https://cloud.google.com/compute/docs/instances/viewing-and-applying-idle-vm-recommendations#viewing_idle_vm_instance_recommendations)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Zone* - Location to check, it is specifically Google zones
- *Project ID* - Google Projects to Query. Leave blank to query all projects.
- *Unattached Days* - Days a volume has been unattached. Default is 30 days

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Terminate idle VM after an approval

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
- monitoring.timeSeries.list
- compute.instances.list

Required roles in the provider:

- Compute Recommender Viewer
- Compute Recommender Admin*

\* Only required for taking action (termination); the policy will still function in a read-only capacity without these permissions.

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

### API Quotas

The google api sets quotas on the recommender api, which will generate a `429 RESOURCE_EXHAUSTED`. See [Quotas & Limits](https://cloud.google.com/recommender/quotas)
