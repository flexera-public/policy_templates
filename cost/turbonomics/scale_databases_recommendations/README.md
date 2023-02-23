# Turbonomics Scale Databases Recommendations

## What it does

The Turbonomics Scale Databases Recommendations policy uses Turbonomics [Credentials](https://turbonomic.com/api/v3/markets/{market_uuid}/actions) endpoint to provide Scale Database/DatabaseServer recommendations. From these recommendations we provide monthly savings estimates based on Turbonomics per hour costs

## Input Parameters

- *Provider* - Cloud provider where we get recommendations, it supports AWS, Azure, Google or All of them together.
- *Authorization Cookie* - Authorization cookie pulled from turbonomic login endpoint: [Credentials](https://xxxx.turbonomic.com/api/v3/login)
  - no_echo: true
- *Email addresses to notify* - A list of email addresses to notify.

## Supported Clouds

- AWS
- Azure
- Google

## Required Flexera Roles

- policy_manager
- billing_center_viewer
- Turbonomics - administrator

## Cost

This Policy Template does not incur any cloud costs.
