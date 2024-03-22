# Turbonomic Delete Unattached Volumes Recommendations Azure

## What it does

The Turbonomic Delete Unattached Volumes Recommendations Azure policy uses Turbonomic Actions API endpoint (POST xxxx.turbonomic.com/api/v3/markets/Market/actions) and Business Units endpoint (GET xxxx.turbonomic.com/api/v3/businessunits) to provide delete unattached volumes recommendations. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs.

## Functional Details

- The policy queries the /api/v3/market/{market_uuid}/actions endpoint for the Turbonomic API and based on action will return details and savings for unattached volumes for on-boarded cloud instances.
- The policy will fail after a day, the authorization cookie parameter will need to be refreshed and re-run manually.
- There is a need to run the login credentials against the (`https://xxxx.turbonomic.com/api/v3/login`) endpoint to manually receive cookie authorization.

## Input Parameters

- *Provider* - Cloud provider where we get recommendations, it supports Azure.
- *Authorization Cookie* - Authorization cookie pulled from manual source.
  - no_echo: true
- *Email addresses to notify* - A list of email addresses to notify.
- *Turbonomic endpoint* - Turbonomic endpoint where we'll get all data and authorization validation.
- *Unused days* - The number of days a volume has been unused. The days should be greater than zero.

## Supported Clouds

- Azure

### Required Flexera Roles

- policy manager
- billing_center_viewer

## Cost

- This Policy Template does not incur any cloud cost
