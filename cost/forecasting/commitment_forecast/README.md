# Commitment Forecasting Policy

## What it does

This Policy uses Optima to determine a forecast against a commitment amount for the entire Organization. This policy allows the user to specify a Commitment target value, and track the current commitment spend to date, as well as projected commitment spend for a given period.

The policy uses the specified previous number of months, not including the current month to determine a straight-line forecast.

## Functional Details

- This policy supports a group of Billing Centers or the entire Organization.
- This policy uses the last month before current to guarantee full data.
- This policy produces a straight-line forecast by dividing the earliest month in the dataset by the last month in the dataset.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Cloud Vendor* - Name of the Cloud Vendor if the Budget Scope is 'Cloud Vendor'. Example: 'AWS' or 'GCP'. Leave this blank for 'Organization' scope
- *Commitment Period Start Date* - A date in the past to generate forecast from (YYYY-MM format)
- *Commitment Period End Date* - A date in the future to forecast up to (YYYY-MM format)
- *Total Commitment Target* - Specify total commitment target for the given Cloud Vendor and the specified time period.  Currency is irrelevant; the policy will default to whichever currency is used in Optima
- *Email addresses* - A list of email addresses to notify

## Required CMP Roles

- billing_center_viewer (note: this role must be applied at the Organization level)

## Supported Clouds

- All configured clouds

## Cost

This Policy Template does not incur any cloud costs.
