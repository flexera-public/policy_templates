# Superseded Instances Policy Template

## What it does

The Superseded Instances Policy Template is used to monitor an account a generate a list of superseded instances. This policy supports AWS, Azure, and AzureCSP. It also allows use of AMD, and Burstable types as replacement. There are fundamental differences between this and Optima Superseded Instances recommendations.

## Usage

This policy used Optima data to get a list of instances used in the month and their possible new types, as well it uses data in [Policies Data](https://github.com/rightscale/policy_templates/tree/master/data) to determine if an instance type has been superseded.  It will then list all the instances that have been superseded and their types. The `Monthly Estimated Cost` is an estimated cost for the instances with the current configuration, you will save a portion of that by moving to the instance type, the new instance types should be more performant as well. If the **New Instance Type** value in the incident report is "Unavailable", the current instance type does not currently exist in our Instance Type mapping.  Please raise an issue for the mapping to be updated with the current instance type.

## Permissions

- The `billing_center_viewer` role

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Billing Center Name* - List of Billing Center Names to check
- *Minimum Savings Threshold* - Specify the minimum monthly savings value required for a recommendation to be issued, on a per resource basis. Note: this setting applies to all recommendations. Example: 1.00
- *Minimum Instance Savings Threshold* - The recommended action for some recommendations may require an instance relaunch. Specify the minimum monthly savings value required for a recommendation of this nature to be issued, on a per instance basis. Note: this setting applies to multiple recommendations. Example: 100.00
- *Instance Type Category* - Instance Type Category to pick from.
  1. regular: AWS/Azure - Matches Optima Recommendation data
  1. next_gen: AWS - Latest generation upgrade
  1. burstable: AWS - If an instance can be replaced by a burstable type this will be recommended
  1. amd: AWS - next_gen + a series to allow you to use amd types for even more savings.

## Supported Clouds

- AWS
- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
