# README Guideline

This document provides guidance on how to properly write a Policy Template README file.  The purpose of this file to help the policy template developer create a proper readme file and expedite the pull request review process.  

The README file is an important artifact of the policy template.  It is the customer facing documentation and should be written as such.  The README file should be free of typos, easy to read and correct grammar.  

## Readme file sections

The readme file contains a number of sections which describes the policy template details.  All sections should start with the Header 3 markdown with 3 # for the name and it should contain header 2 markdown.


### Name

The name is the readme file header.  It begins with the Header 2 markdown characters ##.  The name should match the name in the name attribute inside the policy template.  The name include the cloud supported, what and what it checks.  If the policy is multi cloud then you can exclude the cloud and only write what it checks

Example with supported cloud:

```
## AWS Idle Compute Instances

```  

Example: Multi Cloud.  
```
## Unapproved Instance Types

```

### What It Does

This section should be exactly written as the short_description of the policy template without the links to the readme or docs site.  It should be a non-technical description of what the policy checks as well as it's action.  

Example:
Checks for AWS idle instances using CPU and Memory metrics and terminates them after approval.  

### Functional Description

In this section you describe how the policy functions, not what it does.  It should include which clouds, APIs and how checks are made.  This would be a good place to write some technical details about API usage.

### Inputs

Inputs are the parameters added to the policy template.  Each parameter listed in the policy template should be added to the readme.  Include extra details that may not fit into the parameter label or description fields of the parameter.  The field label should be bolded and the description and other details leave unbolded.

Example:

- *Email notify list* - Email addresses of the recipients you wish to notify.  
- *Other parameter* - include detail and extra information here.


### Actions

Include all the actions available to the user.

Example:

- Email
- Terminate all instances after approval

### Required Permissions

Write any CMP user roles the policy manager needs to apply the policy.  Also include any cloud specific permissions or policies needed.  This is also a good location to place details about

Some good examples are written in following policy policy_templates:
- https://github.com/flexera/policy_templates/tree/master/cost/aws/elb/clb_unused
- https://github.com/flexera/policy_templates/tree/master/cost/azure/object_storage_optimization


### Supported Clouds

Show a list of the supported clouds for the policy.

Example:  
- AWS
- Google
...

### Other

Write additional details the policy developer or user may need to know to use or change the policy.  
