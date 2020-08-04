# Google Inefficient Instance Utilization using StackDriver

## What it does

This Policy Template gathers Google StackDriver utilization for instances on 30 day intervals and resizes them after user approval.

## Functional Details

- If APIs & Services are not enabled for a project, the policy will skip that particular project. On the next run if APIs & Services are enabled, then the project will be considered for execution.
- This policy uses the Google API to get a list of instances and Google StackDriver for metrics for instance performance and delivers a report. If you get an **N/A** in a field you will need to install the [StackDriver Agent](https://cloud.google.com/monitoring/agent/install-agent) on the instance to get those metrics.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Average used memory percentage* - Utilization below this percentage will raise an incident to resize the instance.
- *Average used CPU percentage* - Utilization below this percentage will raise an incident to resize the instance.
- *Exclusion Tag Key* - An google-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key

## Policy Actions

- Sends an email notification
- Resize instances after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `Monitoring Viewer` Role
- The `monitoring.timeSeries.list` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Observation Period

By default, this policy calculates utilization over a 30 day period.

To calculate over a different period of time, you can update the policy template.
Replace the `30` wherever you see `"start_date": new Date(new Date().setDate(new Date().getDate() - 30)).toISOString()` with the new number of days you want to use.

## Cost

This Policy Template does not incur any cloud costs.
