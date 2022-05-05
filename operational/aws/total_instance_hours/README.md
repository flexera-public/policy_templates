# AWS Usage Report - Number of Instance Hours Used

## What it does

This Policy Template leverages Optima to produce a stacked bar chart showing Total Instance Hours for AWS Instance Families used per month for the last 12 months.
This policy allows the user to specify a *Region* to filter results by, and will email the user specified in *Email addresses to notify*.

## Functional Details

- This policy supports a single AWS region or the entire Organization.
- This policy produces a stacked-bar chart showing Total Instance Hours by Instance Family for the top 8 most used Instance Families. All other Instance Families will be aggregated and displayed as "Other". Values shown in the graph are for the past 12 months.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Region* - Name of the AWS Region to filter by. Example: 'US West (Oregon)'. Leave this blank for 'Organization' scope
- *Email addresses to notify* - A list of email addresses to notify

## Required CMP Roles

- billing_center_viewer (note: this role must be applied at the Organization level)

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
