# Turbonomic Rightsize Virtual Machines Recommendations Azure

## What it does

The Turbonomic Rightsize Virtual Machines Recommendations Azure policy utilizes Turbonomic Actions endpoint (POST xxxx.turbonomic.com/api/v3/markets/Market/actions), Business Units endpoint (GET xxxx.turbonomic.com/api/v3/businessunits) and Actions Details endpoint (POST xxxx.turbonomic.com/api/v3/actions/details) to provide Scale Virtual Machines Recommendations. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs.

### Input Parameters

- *Provider* - Cloud provider. Allows Azure subscriptions.
- *Authorization Cookie* - authorization cookie pulled from manual source.
  - no_echo: true
- *Email addresses* - A list of email addresses to notify.
- *Turbonomic Endpoint* - Host of the Turbonomic endpoint.

### Required Flexera Roles

- policy_manager
- billing_center_viewer

### Cost

This Policy Template does not incur any cloud costs.
