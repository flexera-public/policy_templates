# Azure Rightsize Compute Instances

## What it does

This policy checks all the instances in Azure Subscriptions for the average CPU usage over the last 30 days. If the usage is less than the user provided Idle Instance CPU percentage threshold then the Virtual Machine is recommended for termination. If the usage is less than the user provided Inefficient Instance CPU percentage threshold then the Virtual Machine is recommended for downsizing. Both sets of Virtual Machines returned from this policy are emailed to the user.

## Functional Details

- The policy leverages the Azure API to check all instances and then checks the instance average CPU utilization over the past 30 days
- The policy identifies all instances that have CPU utilization below the Idle Instance CPU Threshold defined by the user, to provide a recommendation.
- The recommendation provided for Idle Instances is a termination action. These instancse can be terminated in an automated manner or after approval.
- The policy identifies all instances that have CPU utilization below the Inefficient Instance CPU Threshold defined by the user, to provide a recommendation.
- The recommendation provided for Inefficient/Underutilized Instances is a downsize action. These instancse can be downsized in an automated manner or after approval.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated, or downsized. Optima is used to receive the estimated savings which is the cost of the resource for the last full month. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is 0.0. The incident message detail includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.

## Input Parameters

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Idle Instance CPU Threshold (%)* - Average CPU threshold at which to trigger instance termination.
- *Inefficient Instance CPU Threshold (%)* - Average CPU threshold at which to trigger instance downsize.
- *Exclusion Tag Key* - An Azure-native instance tag key to ignore instances that you don't want to consider for downsizing. Example: exclude_utilization.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked.
- *Log to CM Audit Entries* - Boolean for whether or not to log any debugging information from actions to CM Audit Entries, this should be left set to No on Flexera EU.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification
- Terminate virtual machines (if idle) after approval
- Downsize virtual machines (if underutilized) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
