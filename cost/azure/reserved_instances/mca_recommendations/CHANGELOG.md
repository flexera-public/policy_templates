# Changelog

## v2.3

- Add option to include all Reservation types in one incident
- Add option to filter for Reservation term; 1 year or 3 year 

## v2.2

- Support for all Reservation types: ['VirtualMachines', 'SQLDatabases', 'PostgreSQL', 'ManagedDisk', 'MySQL', 'RedHat', 'MariaDB', 'RedisCache', 'CosmosDB', 'SqlDataWarehouse', 'SUSELinux', 'AppService', 'BlockBlob', 'AzureDataExplorer', 'VMwareCloudSimple']
- Added support for Shared subscription reservations
- Prevent incident updates when data doesn't change
- This policy replaces the [older policy](../recommendations) that uses the Azure EA key which was deprecated

## v2.1

- Added default_frequency "daily"

## v2.0

- initial release
