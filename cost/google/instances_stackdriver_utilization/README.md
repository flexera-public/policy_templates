# Google Inefficient Instance Utilization using StackDriver

## What it does

This Policy Template gathers Google StackDriver utilization for instances on 30 day intervals and resizes them after user approval.

## Functional Details

- This policy uses the Google API to get a list of instances and Google StackDriver for metrics for instance performance and delivers a report. If you get an **N/A** in a field you will need to install the [StackDriver Agent](https://cloud.google.com/monitoring/agent/install-agent) on the instance to get those metrics.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Google Cloud Project* - a Google Cloud Project ID
- *Average used memory percentage* - Utilization below this percentage will raise an incident to tag the instance.
- *Average used CPU percentage* - Utilization below this percentage will raise an incident to tag the instance.
- *Exclusion Tag Key* - An google-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key

## Policy Actions

- Sends an email notification
- Resize instances after approval

## Prerequisites

This policy requires the Google Cloud Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *gce* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Google Required Permissions

- Google - The `Monitoring Viewer` Role

## Supported Clouds

- Google

## Observation Period

By default, this policy calculates utilization over a 30 day period.

To calculate over a different period of time, you can update the policy template.
Replace the `30` wherever you see `"start_date": new Date(new Date().setDate(new Date().getDate() - 30)).toISOString()` with the new number of days you want to use.

## Cost

This Policy Template does not incur any cloud costs.