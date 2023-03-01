# Turbonomic Rightsize Virtual Volumes Recommendations Azure

## What it does

The Turbonomic Rightsize Virtual Volumes Recommendations Azure policy uses Turbonomic Actions endpoint (POST xxxx.turbonomic.com/api/v3/markets/Market/actions) and Business Units endpoint (GET xxxx.turbonomic.com/api/v3/businessunits) to provide Rightsize Virtual Volumes recommendations. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs.

## Input Parameters

- *Provider* - Cloud provider where we get recommendations, it supports Azure.
- *Authorization Cookie* - Authorization cookie pulled from manual source.
  - no_echo: true
- *Email addresses to notify* - A list of email addresses to notify.
- *Turbonomic endpoint* - Turbonomic endpoint where we'll get all data and authorization validation.

## Supported Clouds

- Azure

## Required Flexera Roles

- policy_manager
- billing_center_viewer

## Cost

This Policy Template does not incur any cloud costs.
