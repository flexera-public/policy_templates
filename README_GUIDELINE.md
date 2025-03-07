# README Guideline

This document provides guidance on how to properly write a Policy Template README
file.  The purpose of this file to help the policy template developer create a
proper readme file, expedite the pull request review process, and have a
consistent feel across all README files.

The README file is an important artifact of the policy template.  It is the
customer facing documentation and should be written as such.  The README file
should be free of typos, spelling errors, easy to read and correct grammar.

## Readme File Sections

The readme file contains a number of sections which describes the policy template
details.  All sections should start with the Header 2 markdown (2 #, ##) for
the name it should contain header 1 markdown (1 #, #).

[Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)

All sections are required as noted.  Optional sections include Installation,
Cost or Other

### Name (REQUIRED)

The policy name is the readme file header.  It begins with the Header 2
markdown characters ##.  The name should match the value of the name field
inside the policy template.  The name includes the cloud supported and what
it checks.  If the policy is multi cloud then the cloud can be excluded and only
write what it checks

Example with supported cloud:

```markdown

## AWS Idle Compute Instances

```

Example: Multi Cloud.

```markdown

## Unapproved Instance Types

```

### What It Does (REQUIRED)

This section should be exactly written as the short_description of the policy
template without the links to the readme or docs site.  It should be a
non-technical description of what the policy checks as well as it's action.

Example:
Checks for AWS idle instances using CPU and Memory metrics and terminates them
after approval.

### Functional Description (REQUIRED)

In this section you describe how the policy functions, not what it does.  It
should include which clouds, APIs and how checks are made.  This would be a good
place to write some technical details about API usage and  metrics used for
gathering details etc.

### Input Parameters (REQUIRED)

Inputs parameters are the fields displayed when applying the policy template.
Each parameter listed in the policy template should be added to the readme.
Include extra details that may not fit into the parameter label or description
fields of the parameter.  The field label should be bolded and the description
and other details leave unbolded.

Example:

- *Email notify list* - Email addresses of the recipients you wish to notify.
- *Other parameter* - include detail and extra information here.

### Policy Actions (REQUIRED)

Include all the actions available to the user.  All policies will have at least
one action, the email notification.  There could be other actions such as
terminating or resizing an instance.  Include a list of all possible actions.

Example:

- Sends an email notification
- Terminate all instances after approval

### Prerequisites

This section describes what it takes to run the policy.  This may include the
Credential Managements, and provider permissions.  See more below.

### Installation (OPTIONAL)

In this section include additional configuration needed to run the policy.
Additional information may include setting up credentials in Cloud Management,
configuring an external system etc.

### Supported Clouds (OPTIONAL)

Show a list of the supported clouds for the policy.

Example:

- AWS
- Google
- ...

### Other (OPTIONAL)

Write additional details the policy designer, policy manager or policy approver
may need to know to use or change the policy.

### Example Readme

Copy and paste the example below to start a new policy readme from scratch.
See more details about each section above.  Read the example carefully and
replace the example text with the details that apply to your policy.

```markdown
# Replace this text with the policy name

## What It Does

Add details here

## Functional Description

Add functional detail here

## Input Parameters

This policy template has the following Input parameters which require value before
the policy can be applied.

- *Email notify list* - Email addresses of the recipients you wish to notify.
- *Other parameter* - include detail and extra information here.

## Policy Actions

Policy actions may include automation to alert or remediate violations found in the
Policy Incident. Actions that destroy or terminate a resource generally require
approval from the Policy Approver. This policy includes the following actions.

- Sends an email notification
- list additional actions if any.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm)
for connecting to the cloud -- in order to apply this policy you must have a
credential registered in the system that is compatible with this policy. If
there are no credentials listed when you apply the policy, please contact your
cloud admin and ask them to register a credential that is compatible with this
policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm)
to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

`` ```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":[
      "elasticloadbalancing:DescribeLoadBalancers",
      "elasticloadbalancing:DescribeInstanceHealth",
      "elasticloadbalancing:DescribeTags",
      "elasticloadbalancing:DeleteLoadBalancer"
    ],
    "Resource":"*"
    }
  ]
}
``` ``

## Supported Clouds

This policy template supports the following clouds:

- AWS
- Azure
- Google

## Other

Add other details here

## Costs

This Policy Template does not incur any cloud costs.

```
