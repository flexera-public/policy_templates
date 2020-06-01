# Google unlabeled Resources

## What it does

Find all Google cloud resources(disks, images, instances, snapshots, buckets, vpnGateways) missing any of the user provided labels with the option to update the resources with the missing labels.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *List of labels* - List of labels to find resources which are not labeled by given inputs.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Label to the selected resources with given input

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `Monitoring Viewer` Role
- The `compute.disks.list` permission
- The `compute.instances.list` permission
- The `compute.disks.setLabels` permission
- The `compute.externalVpnGateways.list` permission
- The `compute.images.list` permission
- The `compute.externalVpnGateways.setLabels` permission
- The `compute.images.setLabels` permission
- The `compute.instances.setLabels` permission
- The `compute.snapshots.list` permission
- The `compute.snapshots.setLabels` permission
- The `compute.vpnGateways.list` permission
- The `compute.vpnGateways.setLabels` permission
- The `compute.images.setLabels` permission
- The `storage.buckets.list` permission
- The `storage.buckets.update` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.