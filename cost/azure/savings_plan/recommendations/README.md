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

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.CostManagement/*/read`*

\* Only `Microsoft.CostManagement/benefitRecommendations/read` is actually needed but this cannot be added in isolation via the Azure Portal. It is recommended that you add the role and then set all other permissions to NotAction as shown in the below JSON example:

```json
{
  "id": "/subscriptions/{{subscriptionId}}/providers/Microsoft.Authorization/roleDefinitions/{{roleDefinitionId}}",
  "properties": {
    "roleName": "Savings Plan Recommendations",
    "description": "",
    "assignableScopes": [
      "/subscriptions/{{subscriptionId}}"
    ],
    "permissions": [
      {
        "actions": [
          "Microsoft.CostManagement/*/read"
        ],
        "notActions": [
          "Microsoft.CostManagement/alerts/read",
          "Microsoft.CostManagement/budgets/read",
          "Microsoft.CostManagement/cloudConnectors/read",
          "Microsoft.CostManagement/dimensions/read",
          "Microsoft.CostManagement/exports/read",
          "Microsoft.CostManagement/externalBillingAccounts/read",
          "Microsoft.CostManagement/externalBillingAccounts/dimensions/read",
          "Microsoft.CostManagement/externalBillingAccounts/query/read",
          "Microsoft.CostManagement/externalBillingAccounts/externalSubscriptions/read",
          "Microsoft.CostManagement/externalBillingAccounts/forecast/read",
          "Microsoft.CostManagement/externalSubscriptions/read",
          "Microsoft.CostManagement/externalSubscriptions/dimensions/read",
          "Microsoft.CostManagement/externalSubscriptions/query/read",
          "Microsoft.CostManagement/externalSubscriptions/forecast/read",
          "Microsoft.CostManagement/forecast/read",
          "Microsoft.CostManagement/operations/read",
          "Microsoft.CostManagement/query/read",
          "Microsoft.CostManagement/reports/read",
          "Microsoft.CostManagement/views/read"
        ],
        "dataActions": [],
        "notDataActions": []
      }
    ]
  }
}
```

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
