# Azure Reserved Instances Utilization MCA

## What it does

This Policy Template leverages the [Azure API for Reserved Instance Utilization and Details](https://learn.microsoft.com/en-us/rest/api/reserved-vm-instances/reservation/list-all). It will notify only if utilization of a RI falls below the value specified in the `Show Reservations with utilization below this value (%)` field. It examines the RI utilization for the prior 7 days or 30 days.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure Endpoint* - Azure Endpoint to access resources
- *Look Back Period* - The number of days of past Azure Reservation Utilization data to analyze
- *Show Reservations with utilization below this value (%)* - Number between 1 and 100
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Capacity/reservationorders/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.

