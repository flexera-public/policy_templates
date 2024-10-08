# Google Cloud Run Anomaly Detection

## What It Does

This Policy uses Google Cloud Metrics data to identify anomalies for Cloud Run services using the [Standard Score (aka `Z-score`)](https://en.wikipedia.org/wiki/Standard_score) statistical method.

> The standard score is the number of standard deviations by which the value of a raw score (i.e., an observed value or data point) is above or below the mean value of what is being observed or measured.

This policy only uses Google Cloud Metric data and is designed to notify of anomalies <24 hours -- specifically before cost and usage data is available.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Lookback Time Period* - The time period to look back for anomalies. The longer the time period, the more accurate the anomaly detection will be.
- *Lookback Aggregation Period* - The time period to aggregate the metric data
- *Metric Name* - The name of the metric to monitor for anomalies
- *Threshold For Z-score* - The threshold for Z-scale, which is the number of consequent anomaly events to trigger an incident (i.e. 1, 2, 3)
- *Threshold For Consecutive Anomalies* - Number of Consecutive Anomalies to trigger an incident
- *Email addresses* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `compute.regions.list`
  - `run.services.list`
  - `monitoring.timeSeries.list`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
