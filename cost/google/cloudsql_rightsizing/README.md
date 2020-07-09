# Google Rightsize CloudSQL Instances

## What it does

This Policy Template checks Google Cloud SQL instances based on provided CPU threshold over a 30 day average and resizes them after approval.

## Functional Details

- This policy identifies all Google CloudSQL instances reporting performance metrics to stackdriver whose CPU utilization is below the thresholds set in the **Average used CPU % - Downsize Threshold** and **Average used CPU % - Upsize Threshold** parameters.
- If APIs & Services are not enabled for a project, the policy will skip that particular project. On the next run if APIs & Services are enabled, then the project will be considered for execution.
- The **Exclusion Tag Key:Value** parameter is a string value.  Supply the Tag Key & Value.  If the exclusion tag is used on an CloudSQL Instance, that Instance is presumed to be exempt from this policy.
- The rightsizing escalation can be automated, executed after approval, or skipped.

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

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `Monitoring Viewer` Role
- The `sqlservice.admin` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.
