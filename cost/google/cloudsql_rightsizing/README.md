# Google Rightsize CloudSQL Instances

## What it does

This Policy Template checks Google Cloud SQL instances based on provided CPU threshold over a 30 day average and resizes them after approval.

## Functional Details

- This policy identifies all Google CloudSQL instances reporting performance metrics to stackdriver whose CPU utilization is below the thresholds set in the **Average used CPU % - Downsize Threshold** and **Average used CPU % - Upsize Threshold** parameters.
- If APIs & Services are not enabled for a project, the policy will skip that particular project. On the next run if APIs & Services are enabled, then the project will be considered for execution.
- The **Exclusion Tag Key:Value** parameter is a string value.  Supply the Tag Key & Value.  If the exclusion tag is used on an CloudSQL Instance, that Instance is presumed to be exempt from this policy.
- The rightsizing escalation can be automated, executed after approval, or skipped.
- This policy does not support custom tiers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - A list of email addresses to notify
- *Average used CPU % - Upsize threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU % - Downsize Threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key:Value* - Cloud native label to ignore instances. Format: Key:Value
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Resize Instances" action while applying the policy, all the identified instances will be resized.

## Policy Actions

- Sends an email notification
- Resize DB instances after approval

## Prerequisites

This Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Cloud SQL API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com)
- [Recommender API](https://console.cloud.google.com/flows/enableapi?apiid=recommender.googleapis.com)

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - Roles
    - `Monitoring Viewer`

  - Permissions
    - `sqlservice.admin`
    - `resourcemanager.projects.get`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
