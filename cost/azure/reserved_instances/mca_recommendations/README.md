# Azure Reserved Instances Recommendation

## NOTE:  This policy supersedes the previous [Policy Template](../recommendations/) that used the Azure EA Key

## What it does

This Policy leverages the [Azure API](https://docs.microsoft.com/en-us/rest/api/consumption/reservationrecommendations/list). It will raise incidents if Azure has any Reservations Purchase Recommendations, whose net savings exceeds the `Net Savings Threshold` parameter in the Policy.  Supports Shared subscription Reservations and the following Reservation Types: ['VirtualMachines', 'SQLDatabases', 'PostgreSQL', 'ManagedDisk', 'MySQL', 'RedHat', 'MariaDB', 'RedisCache', 'CosmosDB', 'SqlDataWarehouse', 'SUSELinux', 'AppService', 'BlockBlob', 'AzureDataExplorer', 'VMwareCloudSimple']

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Look Back Period* - Number of days of prior usage to analyze.
- *Net Savings Threshold* - Specify the minimum net savings that should result in a recommendation
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no
credentials listed when you apply the policy, please contact your cloud admin, and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Consumption/reservationRecommendations/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
