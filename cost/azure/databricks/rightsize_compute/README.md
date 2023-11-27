# Azure Databricks Rightsize Compute Instances

## What it does

This policy checks all the instances associated with Azure Databricks workspaces in Azure Subscriptions for the average or maximum CPU and/or memory usage over a user-specified number of days. If the usage is less than the user provided Idle Instance CPU and/or memory percentage threshold then the Virtual Machine is recommended for deletion. If the usage is less than the user provided Underutilized Instance CPU and/or Memory percentage threshold then the Virtual Machine is recommended for downsizing. Both sets of Virtual Machines returned from this policy are emailed to the user.

## Functional Details

- The policy identifies all Virtual Machine resources using the bill data from Flexera API
- The policy uses Azure API to get all utilization metrics for those resources during the lookback period.
- The policy identifies all instances that have CPU and/or memory utilization below the user-specified idle thresholds and provides the relevant recommendation.
- The recommendation provided for Idle Instances is a deletion action. The cluster or workspace can likely be deleted.
- The recommendation provided for Underutilized Instances is a downsize action. The cluster or workspace can likely be downsized.

### Policy savings details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is deleted or downsized. Cost data from Flexera is used to retrieve and calculate the estimated savings.

Because the virtual machine resources can often be short-lived and ephemeral, we use the actual cost during the lookback period to estimate Potential Monthly Savings.

If the lookback period is 30 days (default value), the estimated savings for a Delete is 100% the actual cost during that 30 day period for a Downsize is 50% the actual cost during that 30 day period.

If the lookback period is less than 30 days (1 month), we calculate what % of 30 days the lookback period is and then use that ratio to estimate the savings for a full month period (30 days).  If the actual cost during a 15-day lookback period was $100, the estimated savings calculation for a Delete is `(30/15) * $100`.  In this example, a Delete would estimate $200 Potential *Monthly* Savings and a Downsize would estimate $100 Potential *Monthly* Savings.

The savings is displayed in the Estimated Monthly Savings column. The incident message detail includes the sum of each resource *Estimated Monthly Savings* as *Potential Monthly Savings*.

## Prerequisites

### Create `Azure Databricks ClusterId` Tag Dimension in Flexera

This is required for the policy templates to be able to map each Azure Virtual Machine to a Databricks Cluster.

Navigate to *Administration > Custom Tags* in Flexera and Create a new Tag Dimension

| Tag Display Name | Tag Keys | Tag ID (if creating via API instead of UI) |
| ---------------- | -------- | --- |
| `Azure Databricks ClusterId` | `ClusterId` | `tag_azure_databricks_clusterid` |

> *Note: These values are case-sensitive*

### Credential configuration

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/skus/read`
  - `Microsoft.Insights/metrics/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Optional: **Databricks Credential** (*provider=databricks*)

Setting up authentication to the Azure Databricks workspaces themselves will enable getting additional metadata from the Databricks APIs (Cluster Name, Cluster Type, Cluster Tags)

#### Option 1: Authenticate to Databricks using Azure Service Principal (Recommended)

This is the recommended method and enables a single Azure Service Principal to traverse multiple Databricks workspaces in multiple subscriptions.

##### Grant Permission to Azure Service Principal in all Azure Databricks Workspaces

1. Get Service Principal's Client ID

   You can get this from the Azure Portal or via Flexera > Automation > Credentials and get the Client ID for the Azure RM Credential that is being used.  The Azure SP that is used for other Flexera Azure Policy Templates can be used for the Databricks Policy Templates.

1. Add Service Principal to all DB Workspace using the Client ID

   Databricks Workspace  Admin Settings > Service Principal (i.e. `https://{workspaceUrl}/?#setting/accounts/servicePrincipals` )

1. Grant Service Principal Permissions in DB Workspace

   We currently recommend adding Service Principal to `admin` group so it can see all clusters and compute resources within the cluster.

   Databricks Workspace > Admin Settings > Groups (i.e. `https://{workspaceUrl}/?#setting/accounts/groups` )

##### Create `OAuth2` Credential in Flexera

Replace these:

- `{access_token}`
- `{flexeraProjectId}`
- `{Credential Name}`
- `{credentialId}`
- `{clientId}`
- `{clientSecret}`
- `{tenantId}`

```sh
curl 'https://api.flexera.com/cred/v2/projects/{flexeraProjectId}/credentials/oauth2/{credentialId}' -X PUT -H 'Content-Type: application/json' -H 'Api-Version: 1.0' -H 'Authorization: Bearer {access_token}' --data-raw '{"description":"","name":"{Credential Name}","grantType":"client_credentials","tags":[{"key":"provider","value":"databricks"}],"clientCredentialsParams":{"additionalParams":{"resource":"2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"},"clientId":"{clientId}","clientSecret":"{clientSecret}"},"tokenUrl":"https://login.windows.net/{tenantId}/oauth2/token"}'
```

#### Option 2: Authenticate to Databricks using Databricks Personal Access Token

##### Create `API Key` Credential in Flexera

Replace these:

- `{access_token}`
- `{flexeraProjectId}`
- `{Credential Name}`
- `{credentialId}`
- `{personalAccessToken}`

```sh
curl 'https://api.flexera.com/cred/v2/projects/{flexeraProjectId}/credentials/oauth2/{credentialId}' -X PUT -H 'Content-Type: application/json' -H 'Api-Version: 1.0' -H 'Authorization: Bearer {access_token}' --data-raw '{"description":"","name":"{Credential Name}","field":"Authorization","location":"header","type":"Bearer","tags":[{"key":"provider","value":"databricks"}],"key":"{personalAccessToken}"}'
```

***Important*** - When creating an Applied Policy using a Databricks Personal Access Token credential, you must provide just 1 workspace identifier (Name or ID) in `param_databricks_workspace_list`.  Personal Access Tokens are workspace-scoped and a single applied policy cannot traverse multiple Databricks workspaces with a single Personal Access Token.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs

## Other Notes

### Results where `Databricks Cluster ID` equals `null`

These are virtual machines that the Flexera platform does not have costs for yet. If it were launched recently then we won't be able to map it (using cost method) for up to 24hrs.
