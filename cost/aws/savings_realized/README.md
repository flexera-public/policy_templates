# AWS Savings Realized from Reservations

## What it does

This Policy uses Optima to determine a view of total savings realized from using Compute Reservations, Savings Plans, and Spot Instances in AWS, for the entire Organization or specified billing centers across a period of historical months.

## Functional Details

- This policy supports a view of savings realized from AWS Compute Reserved Instances, Savings Plans and Spot Instances.
- This policy supports a view of savings realized for a list of specific billing centers or for the entire Organization.
- This policy uses the on-demand rate and the reserved instance/savings plan/spot instance rate by instance type and region to derive a savings rate. The policy then uses usage amount to calculate total savings realized.
- This policy produces a bar chart showing savings realized vs. total actual spend for the period of historical months specified.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - List of Billing Center Names to check Savings Realized for. Leave blank for whole Organization view
- *Period Start Date* - The starting month of the historical data to analyze (in YYYY-MM format e.g., "2021-10")
- *Period End Date* - The ending month of the historical data to analyze (in YYYY-MM format)
- *Email addresses* - A list of email addresses to notify
- *Chart Type* - The type of bar chart to view savings realized data by

## Required CMP Roles

- billing_center_viewer (note: this role must be applied at the Organization level)

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
