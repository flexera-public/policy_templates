# Azure Migrate Integration

## What it does

This Policy will collect the resources from a RISC Foundations assessment and seed Azure Migrate with the discovered servers.

## Pre-requisites

- RISC Foundations assessment to have successfully discovered resources and analyzed application stacks
- Retrieve a RISC API Assessment Code and API Key from your Subscription Administrator.  See more about RISC API authentication requirements [here](https://portal.riscnetworks.com/app/documentation/?path=/using-the-platform/restful-api-access/)
- Create an Azure Migrate project in the target Azure Subscription, and select "Flexera" as your Assessment Tool

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *RISC User ID* - Email address of the RISC User Account which will be used for authentication
- *RISC Hashed Password* - Hashed password to be used for authentication
- *RISC Assessment Code* - RISC Assessment Code to be used for authentication
- *Azure Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication
- *Azure Migrate Project Name* - The resource name of the Azure Migrate Project where RISC data should be populated

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
