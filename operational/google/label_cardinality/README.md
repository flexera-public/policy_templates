# Google Label Cardinality Report

## What It Does

This policy template is used to generate a label cardinality (how many unique values each label key has) report for Google Cloud, along with a list of those unique values for each label key. The report includes cardinality for all label values for Google Cloud Projects and Resources.

__NOTE: Google Cloud does not offer a straight-forward way to list all resources in a given Project along with their labels. This report should not be considered complete and should be used for general guidance. A list of supported resources is provided below.__

## How It Works

Using the associated APIs, labels for Google Projects and for the following resources are included in the report:

- Compute
  - Disks
  - Images
  - IP Addresses
  - Snapshots
  - Storage Pools
  - VPN Gateways
  - VPN Tunnels
  - Virtual Machines
- Database
  - Cloud SQL for MySQL Instances
- Storage
  - Object Storage Buckets

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `cloudsql.instances.get`
  - `cloudsql.instances.list`
  - `compute.addresses.get`
  - `compute.addresses.list`
  - `compute.disks.get`
  - `compute.disks.list`
  - `compute.images.get`
  - `compute.images.list`
  - `compute.instances.get`
  - `compute.instances.list`
  - `compute.snapshots.get`
  - `compute.snapshots.list`
  - `compute.storagePools.get`
  - `compute.storagePools.list`
  - `compute.vpnGateways.get`
  - `compute.vpnGateways.list`
  - `compute.vpnTunnels.get`
  - `compute.vpnTunnels.list`
  - `storage.buckets.get`
  - `storage.buckets.list`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Cloud SQL API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com)
- [Cloud Storage API](https://console.cloud.google.com/flows/enableapi?apiid=storage.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
