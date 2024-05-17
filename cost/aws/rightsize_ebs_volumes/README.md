# AWS Rightsize EBS Volumes

## What It Does

This policy checks all the EBS volumes in an AWS Account for Read and Write Operations and Provisioned IOPS metrics over a user-specified number of days.  If the volume is unattached, or has zero read or write operations for the lookback period, then the Volume is considered "Idle" and recommended for deletion (with option to create snapshot before).  For the volumes not considered Idle, if volume is a Provisioned IOPS volume and usage less than the user provided threshold for Provisioned IOPS % then it is considered "Underutilized" and recommended for rightsizing.

This policy does not currently support Capacity Used % for identified Underutilized volumes because of complexity involved with mapping the volume device mount(s) to the OS mount points for each disk, which is required to map the volume to the `disk_used_percent` metric provided by the CloudWatch Agent on the EC2 Instance.  This device to mount point information is typically retrieved from the OS/Application layer (i.e. `df -h`):

```sh
$ df -h
Filesystem        Size  Used Avail Use% Mounted on
devtmpfs          4.0M     0  4.0M   0% /dev
tmpfs             453M     0  453M   0% /dev/shm
tmpfs             182M  436K  181M   1% /run
/dev/nvme0n1p1    8.0G  2.0G  6.1G  24% /
tmpfs             453M     0  453M   0% /tmp
/dev/nvme1n1      8.0G   90M  7.9G   2% /data-backup
/dev/nvme2n1      8.0G   90M  7.9G   2% /data
/dev/nvme0n1p128   10M  1.3M  8.7M  13% /boot/efi
```

In this example, we know an example volume (`vol-a1b2c3d4`) is mounted on `/dev/nvme1`.  This information is provided by the `ec2:DescribeVolumes` API response, but we don't have a way to get the the mount point (`/data-backup`) without information from the OS.  The policy template does not attempt to map this information, but we are exploring this topic and hope to add recommendations for Storage Capacity Used % future releases.  Added complexity for disks that have multiple partitions, or mount points that span multiple volumes (RAID, LVM, etc..)

## Functional Details

- The policy leverages the AWS API to retrieve a list of all volumes in an AWS Account
- The policy identifies all volumes
- The policy gets read/write operations for all volumes
- The policy evaluates read/write and identifies idle volumes based on volumes that have zero read and write ops
- The policy gets read/write operations utilization for Provisioned IOPS volumes
- The policy evaluates utilization data for volumes and identifies underutilized based on user provided threshold
- The policy estimates savings for idle volumes to be 100% of the monthly volume cost
- The policy estimates savings for underutilized volumes to be the difference based on recommended % change in Provisioned IOPS

### Policy savings details

The policy estimates savings for idle volumes to be 100% of the monthly volume cost

The policy estimates savings for underutilized volumes to be the difference based on recommended % change in Provisioned IOPS or Capacity.  For example, if downsize IOPS by 50%, then estimated savings is 50% of the cost of the original volume.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the volume is upgraded from GP2 to GP3.

- The `Estimated Monthly Cost` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month. This value is not used for calculating savings but is provided as a reference.
- Since the `Estimated Monthly Cost` of individual resources is obtained from Flexera CCO, it will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The AWS Pricing API is used to retrieve the list price of the current volume type and the recommended volume type. The `Estimated Monthly Savings` is calculated by subtracting the estimated price of the recommended GP3 volume type from the price of the current GP2 volume type.
- Since `Estimated Monthly Savings` is calculated based on list prices obtained from the AWS Pricing API, they will *not* take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- If the Flexera organization is configured to use a currency other than USD, the savings values will be converted from USD using the exchange rate at the time that the policy executes.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *AWS Regional Pricing API* - The regional AWS Pricing API to use when retrieving pricing data. Pricing may vary based on region. More details on these endpoints and how functionality differs between them can be found in the [AWS Price List Query API documentation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/using-price-list-query-api.html#price-list-query-api-endpoints).
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Upgrade Volumes to GP3" action while applying the policy, all the volumes that appear in the raised incident will be upgraded to GP3.

## Policy Actions

- Sends an email notification
- Upgrade GP2 volumes to GP3 after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeVolumes`
  - `ec2:ModifyVolume`*
  - `pricing:GetProducts`

  \* Only required for taking action (upgrading to GP3); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeVolumes",
                  "ec2:ModifyVolume",
                  "pricing:GetProducts"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
