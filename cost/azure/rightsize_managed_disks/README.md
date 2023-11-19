# Azure Rightsize Managed Disks

## What it does

This policy checks the percentage of disk space used of the Azure managed disks and suggest rightsizing recommendations 

Drafts:

Since the total cost of Standard SSDs storage depends on the size and number of disks, the number of transactions, and the number of outbound data transfers, and these capacities are all givenand limited by the disk size.

## Functional details

## Input parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore instances that you don't want to consider for downsizing or deletion. Format: Key:Value
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Minimum used disk space percentage to consider a managed disk for downsizing* - The minimum used disk space percentage threshold at which to consider a disk to be 'oversized' and therefore be flagged for downsizing.

## Actions

## Prerequisites

## Credential configuration

## Supported clouds

- Azure

## Cost
