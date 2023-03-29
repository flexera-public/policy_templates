# Turbonomic Delete Unattached Volumes Recommendations GCP

## What it does

The Turbonomics Delete Unattached Volumes Recommendations GCP policy utilizes Turbonomic Actions API endpoint (POST `https://turbonomic.com/api/v3/markets/{market_uuid}/actions`) to provide GCP Turbonomics Delete Unattached Volumes Recommendations.

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

- Google

### Required Flexera Roles

- policy manager
- billing_center_viewer

## Cost

- This Policy Template does not incur any cloud cost
