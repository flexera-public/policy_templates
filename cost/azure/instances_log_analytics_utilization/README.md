# Azure Inefficient Instance Utilization using Log Analytics

## What it does

This Policy Template uses performance metrics from Log Analytics from the last 30 days to identify underutilized instances and provides rightsizing recommendations. Once recommendations are generated, instances can be rightsized in an automated manner or after approval. This is meant to be run as a weekly policy.

## Functional Details

- This policy identifies all instances reporting performance metrics to Log Analytics whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters. Once recommendations are generated, instances can be rightsized in an automated manner or after approval.
- The **Exclusion Tag Key** parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Average used memory percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key* - An Azure-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Downsize Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be downsized.

## Policy Actions

- Sends an email notification
- Resize virtual machines after approval

## Prerequisites

Azure Service Principal (AKA Azure Active Directory Application) with the below mentioned role and permission are required in the target subscription.

Virtual Machines must have the Log Analytics/OMS Agent installed for sending performance metrics to a Azure Log Analytics workspace.

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:
Two provider tags needs to be created using the same credentials for running this policy.

Provider tag value to match this policy: `azure_rm` and `azure_log`

Required role and permission in the provider:

Role:

- [Log Analytics Reader](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/manage-access)

Permission:

- [Microsoft.Compute/virtualMachines/write](https://docs.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftcompute)

## Supported Clouds

- Azure Resource Manager

## Observation Period

By default, this policy calculates utilization over a 30 day period.

To calculate over a different period of time, you can update the policy template.
Replace the `30` wherever you see `query "timespan","P30D"` with the new number of days you want to use.

## Cost

This Policy Template does not incur any cloud costs.
