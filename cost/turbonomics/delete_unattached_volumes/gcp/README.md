# Turbonomics Delete Unattached Volumes Recommendations GCP

## What it does

The Turbonomics Delete Unattached Volumes Recommendations GCP policy utilizes Turbonomic Actions API endpoint (POST `https://turbonomic.com/api/v3/markets/{market_uuid}/actions`) to provide GCP Turbonomics Delete Unattached Volumes Recommendations.

## Functional Details

- The policy queries the /api/v3/market/{market_uuid}/actions endpoint for the Turbonomic API and based on action will return details and savings for unattached volumes for on-boarded cloud instances.
- The policy will error after a day, the authorization cookie parameter will need to be refreshed and re-run manually
- there is a need to run the login credentials against the (`https://xxxx.turbonomic.com/api/v3/login`) endpoint to manually receive cookie authorization

## Input Parameters

- *Authorization Cookie"* - authorization cookie pulled from Turbonomic login endpoint: (POST `https://xxxx.turbonomic.com/api/v3/login`)
- no_echo: true
- *Email addresses"* - a list of email addresses to notify

### Required Flexera Roles

- policy manager
- billing_center_viewer

## Cost

- This Policy Template does not incur any cloud cost
