# Google Unlabeled Resources

## What it does

Find all Google cloud resources(disks, images, instances, snapshots, buckets, vpnGateways) missing any of the user provided labels with the option to update the resources with the missing labels.

## Functional Details

- The policy leverages the Google Cloud API to retrieve a list of all labelable resources across Google Cloud Projects.
- Using the 'List of labels' parameter, the policy identifies all resources that are missing the label keys specified by the user.
- The policy outputs resources missing the specified label keys as well as resources with the specified label keys but are missing label values.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *List of labels* - List of labels to find resources which are not labeled by given inputs.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Label to the selected resources with given input

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - Roles
    - `Monitoring Viewer`

  - Permissions
    - `compute.disks.list`
    - `compute.instances.list`
    - `compute.disks.setLabels`
    - `compute.externalVpnGateways.list`
    - `compute.images.list`
    - `compute.externalVpnGateways.setLabels`
    - `compute.images.setLabels`
    - `compute.instances.setLabels`
    - `compute.snapshots.list`
    - `compute.snapshots.setLabels`
    - `compute.vpnGateways.list`
    - `compute.vpnGateways.setLabels`
    - `compute.images.setLabels`
    - `storage.buckets.list`
    - `storage.buckets.update`
    - `resourcemanager.projects.get`

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
