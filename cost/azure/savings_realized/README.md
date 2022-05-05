# Azure Savings Realized from Reservations

## What it does

This Policy uses Optima to determine a view of total savings realized from using Compute reservations in Azure for the entire Organization across a period of historical months.

## Functional Details

- This policy supports only a view of savings realized from Azure reservations for the entire Organization.
- This policy uses the on-demand rate and the reserved instance rate by instance type and region to derive a savings rate. The policy then uses usage amount to calculate total savings realized.
- This policy produces a bar chart showing savings realized vs. total actual spend for the period of historical months specified.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Period Start Date* - The starting month of the historical data to analyze (in YYYY-MM format e.g., "2021-10")
- *Period End Date* - The ending month of the historical data to analyze (in YYYY-MM format)
- *Email addresses* - A list of email addresses to notify

## Required CMP Roles

- billing_center_viewer (note: this role must be applied at the Organization level)

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
