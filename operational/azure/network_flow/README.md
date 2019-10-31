## NetFlow Top Talkers

### What it does

This Policy Template will analyze RISC Foundations NetFlow data and will leverage these traffic patterns to identify the top communication routes from each application stack to external dependencies.  

### Pre-requisites

- RISC Foundations assessment to have successfully discovered resources and analyzed application stacks
- Retrieve a RISC API Assessment Code and API Key from your Subscription Administrator.  See more about RISC API authentication requirements [here](https://portal.riscnetworks.com/app/documentation/?path=/using-the-platform/restful-api-access/)

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *RISC User ID* - Email address of the RISC User Account which will be used for authentication
- *RISC Hashed Password* - Hashed password to be used for authentication
- *RISC Assessment Code* - RISC Assessment Code to be used for authentication

### Supported Clouds

- VMware
- AWS
- Azure
- Google
- Oracle


### Cost

This Policy Template does not incur any cloud costs.
