# Straight-Line Forecasting Policy

## What it does

This Policy uses Optima to determine a forecast for a Billing Center or the entire Organization. The policy uses the specified previous number of months, not including the current month to determine a straight-line forecast.

## Functional Details

- This policy supports a group of Billing Centers or the entire Organization.
- This policy uses the last month before current to guarantee full data.
- This policy produces a straight-line forecast by dividing the earliest month in the dataset by the last month in the dataset.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - List of Billing Center Names to check
- *Lookback Months* - Number of months to lookback to generate forecast
- *Months to forecast* - Number of months in the future to forecast
- *Cost Metric* - specify options for amortized vs non-amortized and blended vs unblended costs
- *Email addresses* - A list of email addresses to notify

## Required CMP Roles

- billing_center_viewer (note: this role must be applied at the Organization level)

## Supported Clouds

- All configured clouds

## Cost

This Policy Template does not incur any cloud costs.
