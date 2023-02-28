# Turbonomic Allocate Virtual Machine Recommendations Azure

## What it does

The Turbonomic Allocate Virtual Machines Recommendations Azure policy utilizes Turbonomic (POST `https://turbonomic.com/api/v3/markets/{market_uuid}/actions`) endpoint to provide Azure VM allocation recommendations for Reserved Instance coverage. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs

## Functional Details

- The policy queries the /api/v3/markets/{market_uuid}/actions endpoint for the Turbonomic API and based on action will return action details and savings for on-boarded cloud instances
- The policy will error after a day, the authorization cookie parameter will need to be refreshed and re-run manually
- There is a need to run the login credentials against the (`https://xxxx.turbonomic.com/api/v3/login`) endpoint to manually recieve cookie authorization

### Input Parameters

- *Authorization Cookie"* - authorization cookie pulled from turbonomic login endpoint: (POST `https://xxxx.turbonomic.com/api/v3/login`)
- no_echo: true
- *Email addresses* - A list of email addresses to notify

### Required Flexera Roles

- policy_manager
- billing_center_viewer

### Cost

This Policy Template does not incur any cloud costs.
