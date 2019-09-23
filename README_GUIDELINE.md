# README Guideline

This document provides guidance on how to properly write a Policy Template README file.  The purpose of this file to help the policy template developer create a proper readme file and expedite the pull request review process.

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

### Inputs



### Actions

Include all the actions available to the user.

Example:

- email
- terminate all instances after approval

### Required Permissions

Write any CMP user roles the policy manager needs to apply the policy.  Also include any cloud specific permissions or policies

Example:

-

AWS IAM roles
```javascript


```

### Supported Clouds

Show a list of the supported clouds for the policy.

Example:  
- AWS
- Google
...

### Other
