# Orgs and Clouds Vendor Accounts Report Policy

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**
This policy generates a list of cross organization Cloud Vendor Accounts connected to Flexera Optima based on
the bill connection settings for Azure and Google, as well as full list of AWS accounts under the payer account connected for each Flexera Organization.

_Note 1: 'enterprise_manager' user role is required for each organization._
_Note 2: If excluding orgs is needed use only either 'Excluded Organizations' or 'Exclucded organizations IDs' parameter, not both._

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email list* - Email addresses of the recipients you wish to notify
- *Excluded Organizations* - Names of organizations to exclude
- *Excluded Organizations IDs* - Names of organizations to exclude

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Required Permissions

This policy requires permissions to access RightScale resources (Optima).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Governance - enterprise_manager

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
