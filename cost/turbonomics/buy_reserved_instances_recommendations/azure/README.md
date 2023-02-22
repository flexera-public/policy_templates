# Turbonomics Buy Reserved Instances Recommendations Azure

## What it does

The Turbonomics Buy Reserved Instances Recommendations Azure policy utilizes Turbonomics [Credentials]https://turbonomic.com/api/v3/markets/{market_uuid}/actions endpoint to provide Azure purchasable RI recommendations for Reserved Instance coverage. From these recommendations we provide monthly savings estimates based on Turbonomics per hour costs

## Functional Details

- The policy queries the /api/v3/markets/{market_uuid}/actions endpoint for the turbonomics api and based on action will return action details and savings for on-boarded cloud instances
- The policy will error after a day, the authorization cookie parameter will need to be refreshed and re-run manually
- there is a need to run the login credentials against the [Credentials]https://xxxx.turbonomic.com/api/v3/login endpoint to manually recieve cookie authoriztion

### Input Parameters

- *Authorization Cookie"* - authorization cookie pulled from turbonomic login endpoint: [Credentials]https://xxxx.turbonomic.com/api/v3/login
- no_echo: true
- *Email addresses* - A list of email addresses to notify

### Required Flexera Roles

- policy_manager
- billing_center_viewer

- Turbonomics - administrator

### Cost

This Policy Template does not incur any cloud costs.
