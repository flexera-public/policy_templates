# Check For New Instance Types

## What it does

The Policy finds instance/machine types across the AWS, Azure, Google cloud vendors and compares them with the existing machine/instance types in our data file. Incident will be created if any new machine/instance type if found, containing missing machine/instance type name and vendor details.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created

## Policy Actions

The following policy action is taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

- This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`, `azure_rm`, `gce`

The following permissions must be allowed for the policy to run.

- AWS

    ```json
    {
      "Version": "2012-10-17",
      "Statement":[
      {
        "Effect":"Allow",
        "Action":[
          "ec2:DescribeInstances",
          "ec2:DescribeRegions"
        ],
        "Resource":"*"
      }
      ]
    }
    ```

- Azure
  - Microsoft.Compute/locations/vmSizes/read

- Google
  - The `compute.machineTypes.list` permission

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not incur any cloud costs.
