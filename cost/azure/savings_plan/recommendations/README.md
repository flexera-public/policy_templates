# Azure Reserved Instances Recommendation

## What it does

This Policy leverages the [Azure API](https://learn.microsoft.com/en-us/rest/api/cost-management/benefit-recommendations/LIST?tabs=HTTP). It will raise incidents if Azure has any Savings Plan Purchase Recommendations, whose net savings exceeds the `Net Savings Threshold` parameter in the Policy. The Policy supports both Shared and Single subscription Savings Plan recommendations.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Look Back Period* - Number of days of prior usage to analyze.
- *Net Savings Threshold* - Specify the minimum net savings that should result in a recommendation
- *Reservation Scope* - Single or Shared Scoped Reservations
- *Reservation Term* - The Savings Plan term; 1 Year or 3 Year
- *Email addresses to notify* - Email addresses of the recipients you wish to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm)
for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no
credentials listed when you apply the policy, please contact your cloud admin, and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.CostManagement/*/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
