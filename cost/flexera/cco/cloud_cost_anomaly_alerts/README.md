# Cloud Cost Anomaly Alerts

## What It Does

This policy template reports any cloud cost anomalies in Flexera CCO that meet the criteria specified in the parameters. Optionally, it emails this report.

## How It Works

The policy queries the `/anomalies/report` endpoint of the Flexera CCO Bill Analysis API. User parameters are included in this API request to color the results.

The cost anomalies are identified using [Bollinger Bands](https://en.wikipedia.org/wiki/Bollinger_Bands). The bands are defined as follows:

- The moving average is calculated using a window size specified.
- The upper and lower band are calculated as distance of a given number of standard deviations from the moving average.
- Any point outside of the bands is considered as anomalous. If multiple cost anomalies are detected for the given dimensions, the data point with the greatest deviation is reported as incident.
- Additionally, a URL link is provided to a graphical report where all detected anomalies are shown.

For more details on Flexera Cloud Cost Anomaly Detection, please see the [documentation](https://docs.flexera.com/flexera/EN/Optima/CostAnomaly.htm).

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Time Period* - Number of days back to analyze for anomalies.
- *Minimum Period Spend* - Minimum spend over the time period required to include anomaly in results.
- *Minimum Period Spend Variance* - Minimum spend variance over the time period required to include anomaly in results. Variance is calculated as the difference (absolute value) between the total cost and the moving average.
- *Anomalies To Report* - Whether to report on anomalies above the upper limit, below the lower limit, or both.
- *Cost Metric* - Cost metric to use when analyzing spend for anomalies.
- *Cost Anomaly Dimensions* - Dimension names/IDs to report anomalies for.
  - Both dimension names, such as `Cloud Vendor Account`, and dimension IDs, such as `vendor_account`, can be used.
  - Dimension=Value formatting can be used to filter the results. For example, a value of `Cloud Vendor=AWS` will filter results to just AWS spend.
  - Filters are also automatically included as dimensions. For example, there is no need to specify both `Cloud Vendor` and `Cloud Vendor=AWS` in this parameter because the latter will automatically include the functionality of the former.
- *Cost Anomaly Limit* - Number of anomalies to include in the incident
- *Window Size* - Window size to use for [Bollinger Bands](https://en.wikipedia.org/wiki/Bollinger_Bands)
- *Standard Deviations* - Number of [standard deviations](https://en.wikipedia.org/wiki/Standard_deviation) for the [Bollinger Band](https://en.wikipedia.org/wiki/Bollinger_Bands)

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_manager`
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This policy template does not incur any cloud costs.
