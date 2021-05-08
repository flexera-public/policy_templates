# Flexera IAM Explicit User Roles

## What it does

This policy identifies users in Flexera IAM that have explicit user roles assigned.

## Functional Details

This policy leverages the Flexera IAM API to collect a list of users that have explicit roles assigned.
Best practices dictate that role sbe assigned to groups and users be added/removed from groups based on the level of access they require.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Actions

- Emails a report of users with explicit permissions assigned.

## Pre-requisites

- The policy must be applied by a user with the `enterprise_manager` role.

### Credential Configuration

This policy uses pass-thru authentication and does not require a credential to be configured.

## Supported Services

- Flexera IAM

## Cost

This Policy Template does not incur any cloud costs.
