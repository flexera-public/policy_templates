# Turbonomics Scale Virtual Machines Recommendations AWS

## What it does

The Turbonomics Scale Virtual Machines Recommendations AWS policy utilizes Turbonomics [Credentials](https://turbonomic.com/api/v3/markets/{market_uuid}/actions) endpoint to provide Scale Virtual Machines Recommendations. From these recommendations we provide monthly savings estimates based on Turbonomics per hour costs.

### Input Parameters

- *Provider* - Cloud provider. Allows AWS, Azure subscriptions or GCP projects.
- *Authorization Cookie* - authorization cookie pulled from manual source.
  - no_echo: true
- *Email addresses* - A list of email addresses to notify.

### Required Flexera Roles

- policy_manager
- billing_center_viewer

### Cost

This Policy Template does not incur any cloud costs.
