# Billing Center Cost Anomaly Policy

**NOTE:** This policy is be deprecated and replaced by this [new version](../cloud_cost_anomaly_alerts)

## What it does

The Cost Anomaly Policy will analyze the spend of all Billing Centers in an Organization over a specified time period.  If the percentage change of the most recent period compared to the previous period exceeds the specified threshold, then an Incident will be raised.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- The policy polls all Billing Centers, looking for any that have exceeded the Percent Change threshold and the Minimum Period Spend requirement
- The last 2 days are not included in the analysis, due to potential delays of the cloud providers updating their billing data

### Input Parameters

- *Time Period* - Number of days to analyze in each period. For example, if `6` days is set, then the latest time period will be 8 days ago to 3 days ago (to account for cloud provider bill delays) and the previous time period will be 14 days ago to 9 days ago.
  - Minimum Value: 1
  - Maximum Value: 31
- *Anomaly Threshold* - Percentage change threshold.  If the percentage change of Billing Center spend from the latest time period compared to the previous time period exceeds this value, then an Incident will be raised.
- *Minimum Period Spend* - The spend of a billing center for either the previous period or current period must exceed this threshold to raise an Incident.
- *Cost Metric* - Specify options for amortized vs nonamortized and blended vs unblended costs.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Billing Center List* - List of Billing Center names you want to report on. Names must be exactly as shown in Optima.
  Leave the field blank to report on all Billing Centers.

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not incur any cloud costs.
