# Application Migration Recommendations

## What it does

This Policy Template will analyze RISC CloudScape data and will generate recommendations for migrating application stacks to the most cost effective cloud providers & regions.

## Pre-requisites

- RISC Foundations & CloudScape assessment to have successfully discovered resources, analyzed application stacks, and generated migration data
- Retrieve a RISC API Assessment Code and API Key from your Subscription Administrator.  See more about RISC API authentication requirements [here](https://portal.riscnetworks.com/app/documentation/?path=/using-the-platform/restful-api-access/)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *RISC User ID* - Email address of the RISC User Account which will be used for authentication
- *RISC Hashed Password* - Hashed password to be used for authentication
- *RISC Assessment Code* - RISC Assessment Code to be used for authentication
- *Included Provides* - A list of Cloud providers to include. If blank all providers available will be included

## Supported Clouds

- AWS
- Azure
- Google
- Oracle
- Softlayer
- Rackspace
- Quest
- Tierpoint

## Cost

This Policy Template does not incur any cloud costs.
