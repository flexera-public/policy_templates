# AWS Cloud Data

Various AWS-specific data assets, such as pricing data. Some assets are manually maintained and some are generated through automation; see the [Cloud Data Scripts README](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/README.md) for more information on how these assets are generated.

## Auto-Generated Files

The following files are produced by scripts in [`tools/cloud_data/aws/`](https://github.com/flexera-public/policy_templates/tree/master/tools/cloud_data/aws) and are kept up to date by scheduled GitHub Actions workflows that open automated pull requests when the data changes.

### aws_ec2_instance_types.json

**Script:** [`tools/cloud_data/aws/aws_ec2_instance_types.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/aws/aws_ec2_instance_types.py)

**Workflow:** [Generate AWS EC2 Instance Types JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-aws-ec2-instance-types-json.yaml)

**Description:** A JSON array of all AWS EC2 instance type objects. Data is fetched from the AWS `DescribeInstanceTypes` API and merged with manual supplementary data. Use this file in policy templates that need detailed specifications for EC2 instance types.

Some fields are currently sourced from the legacy `instance_types.json` file until proper automation is built to derive them:

- `burst_info`
- `superseded`
- `ec2_classic`

**Structure:** Array of objects, one per EC2 instance type.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Full instance type name, e.g. `"t3.micro"` |
| `family` | string | Instance family prefix, e.g. `"t3"` |
| `size` | string | Size portion of the name, e.g. `"micro"` |
| `size_rank` | number | Integer rank for sorting sizes smallest to largest within a family |
| `cpu` | object | CPU details: `cores`, `vcpus`, `nfus`, `manufacturer`, `architectures`, `clockSpeedInGhz` |
| `memory` | object | Memory details: `sizeInMiB` |
| `network` | object | Network details: `baselineBandwidthInGbps`, `peakBandwidthInGbps`, `maximumNetworkInterfaces` |
| `storage` | object | EBS details: `baseline` and `maximum` objects with `bandwidthInMbps`, `iops`, `throughputInMBps`; also `maximumEbsAttachments` |
| `properties` | object | Boolean flags and metadata: `currentGeneration`, `bareMetal`, `hibernationSupported`, `hypervisor`, `instanceStorageSupported`, and many others |
| `burst_info` | object or null | CPU burst credit info for burstable instance types; `null` for non-burstable types |
| `superseded` | object or null | Recommended replacement instance types by category (`regular`, `next_gen`, `burstable`, `amd`); `null` if not superseded |
| `ec2_classic` | boolean | Whether the instance type was available on EC2-Classic (legacy network) |

**Example:**

```json
{
  "name": "t2.2xlarge",
  "family": "t2",
  "size": "2xlarge",
  "size_rank": 64,
  "cpu": {
    "cores": 8,
    "vcpus": 8,
    "nfus": 16,
    "manufacturer": "Intel",
    "architectures": ["x86_64"],
    "clockSpeedInGhz": 2.3
  },
  "memory": { "sizeInMiB": 32768 },
  "network": {
    "baselineBandwidthInGbps": 1.0,
    "peakBandwidthInGbps": 1.024,
    "maximumNetworkInterfaces": 3
  },
  "storage": {
    "baseline": { "bandwidthInMbps": null, "iops": null },
    "maximum": { "bandwidthInMbps": null, "iops": null },
    "maximumEbsAttachments": 40
  },
  "properties": {
    "currentGeneration": true,
    "bareMetal": false,
    "hypervisor": "xen",
    "hibernationSupported": true
  },
  "burst_info": null,
  "superseded": null,
  "ec2_classic": false
}
```

### aws_ec2_pricing.json

**Script:** [`tools/cloud_data/aws/aws_ec2_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/aws/aws_ec2_pricing.py)

**Workflow:** [Generate AWS EC2 Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-aws-ec2-pricing-json.yaml)

**Description:** On-demand EC2 instance pricing by region, instance type, and operating system. Sourced from the AWS Price List API. Used by policy templates that estimate costs or calculate savings for EC2 rightsizing and reservation recommendations.

**Note:** Requires approximately 10 GB of free disk space during generation due to the large size of the raw AWS price file.

**Structure:** Object keyed by AWS region code → instance type family (without size) → OS name → pricing object.

| Field | Type | Description |
| --- | --- | --- |
| `pricePerUnit` | number | On-demand hourly price in USD |
| `sku` | string | AWS Price List SKU identifier |

**Example:**

```json
{
  "us-east-1": {
    "m5": {
      "Linux": { "pricePerUnit": 0.192, "sku": "4NA7Y494T4WRT4CQ" }
    }
  }
}
```

### aws_rds_pricing.json

**Script:** [`tools/cloud_data/aws/aws_rds_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/aws/aws_rds_pricing.py)

**Workflow:** [Generate AWS RDS Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-aws-rds-pricing-json.yaml)

**Description:** On-demand RDS instance pricing by region, instance type, database engine, and deployment type. Sourced from the AWS Price List API. Used by policy templates that estimate costs or calculate savings for RDS rightsizing recommendations.

**Note:** Requires approximately 10 GB of free disk space during generation due to the large size of the raw AWS price file.

**Structure:** Object keyed by AWS region code → instance type → engine name → deployment type → pricing object.

| Field | Type | Description |
| --- | --- | --- |
| `pricePerUnit` | number | On-demand hourly price in USD |
| `sku` | string | AWS Price List SKU identifier |

**Example:**

```json
{
  "us-east-1": {
    "db.m5.large": {
      "MySQL": {
        "Single-AZ": { "pricePerUnit": 0.171, "sku": "WJU4KP7YN7AWAQE8" }
      }
    }
  }
}
```

### regions.json

**Script:** [`tools/cloud_data/aws/aws_cheaper_regions.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/aws/aws_cheaper_regions.py)

**Workflow:** [Update AWS Cheaper Regions](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-aws-cheaper-regions.yaml)

**Description:** A list of all AWS regions, each annotated with the cheapest alternative region in the same geographic group (if one exists). "Cheaper" is determined by comparing median Linux on-demand EC2 prices across all instance types available in both regions. Used by policy templates that recommend moving workloads to cheaper regions.

**Structure:** Array of objects, one per AWS region.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Human-readable region name, e.g. `"US West (N. California)"` |
| `region` | string | AWS region code, e.g. `"us-west-1"` |
| `cheaper` | string or null | Region code of the cheapest comparable region; `null` if this region is already the cheapest |
| `cheaper_ratio` | number or null | Ratio of cheaper region median price to this region's median price (e.g. `0.85` = 15% cheaper); `null` if no cheaper region |

**Example:**

```json
[
  { "name": "US East (N. Virginia)", "region": "us-east-1", "cheaper": null, "cheaper_ratio": null },
  { "name": "US West (N. California)", "region": "us-west-1", "cheaper": "us-east-2", "cheaper_ratio": 0.85 }
]
```

## Manually Maintained Files

### aws_opensearch_instance_types.json

**Description:** Hardware specifications for Amazon OpenSearch Service data node instance types, including vCPU count, memory, local NVMe storage capacity, and documented network baseline bandwidth. This file is used by policy templates that recommend rightsizing for OpenSearch domains to determine downsize candidates and to evaluate disk, network, and storage risk flags. There is no AWS API that returns these values, so this file is manually maintained based on AWS documentation.

**Structure:** Object keyed by instance type name (without the `.search` suffix) → specifications object.

| Field | Type | Description |
| --- | --- | --- |
| `instanceType` | string | Full instance type name as used in OpenSearch, e.g. `"c5.large.search"` |
| `family` | string | Instance family prefix, e.g. `"c5"` |
| `size` | string | Size portion of the name, e.g. `"large"` |
| `size_rank` | number | Integer rank for sorting sizes smallest to largest within a family |
| `vcpu` | number | Number of vCPUs |
| `memoryGiB` | number | Memory in GiB |
| `localStorageGB` | number or null | Total local NVMe storage in GB; `null` for EBS-only instance types |
| `networkBaselineBandwidthGbps` | number | Documented network baseline bandwidth in Gbps |
| `supportsEBS` | boolean | Whether the instance type supports EBS volumes |

**Example:**

```json
{
  "c5.large": {
    "instanceType": "c5.large.search",
    "family": "c5",
    "size": "large",
    "size_rank": 4,
    "vcpu": 2,
    "memoryGiB": 4,
    "localStorageGB": null,
    "networkBaselineBandwidthGbps": 0.75,
    "supportsEBS": true
  }
}
```

### aws_extended_support_dates.json

**Description:** Extended support dates and hourly rates for AWS managed services (e.g. RDS, ElastiCache). Used by policy templates that identify resources running on versions approaching or past end-of-standard-support, and that estimate the cost of extended support fees.

**Structure:** Array of objects, one per supported service/engine/version combination.

| Field | Type | Description |
| --- | --- | --- |
| `service` | string | AWS service name, e.g. `"RDS"` |
| `engine` | string | Database engine name, e.g. `"MySQL"` |
| `version` | string | Engine version string, e.g. `"5.7"` |
| `extended_support_start` | string | Date when extended support begins (ISO 8601 date) |
| `extended_support_end` | string | Date when extended support ends (ISO 8601 date) |
| `hourly_rate` | number | Hourly USD charge per vCPU for extended support |
| `rate_unit` | string | Unit for the `hourly_rate` field, e.g. `"vCPU-hr"` |

**Example:**

```json
[
  {
    "service": "RDS",
    "engine": "MySQL",
    "version": "5.7",
    "extended_support_start": "2024-02-29",
    "extended_support_end": "2025-02-28",
    "hourly_rate": 0.1,
    "rate_unit": "vCPU-hr"
  }
]
```

### elasticache_types.json

**Description:** A simple list of all supported Amazon ElastiCache node type names. Used by policy templates that need to validate or enumerate ElastiCache instance types.

**Structure:** Array of strings, each being a valid ElastiCache node type name.

**Example:**

```json
["m6g.large", "m6g.xlarge", "r6g.large", "r6g.xlarge"]
```

### instance_types.json

**Description:** Legacy reference data for EC2 instance types. This file is older and manually maintained. It should not be used in new policy templates. It exists to ensure that older policy templates continue to function and to supply some fields (such as `superseded`, `burst_info`, and `ec2_classic`) to the auto-generated `aws_ec2_instance_types.json` until automation is built for those fields.

**Structure:** Object keyed by instance type name → specifications object.

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | Next larger instance type in the same family |
| `down` | string or null | Next smaller instance type in the same family |
| `superseded` | object | Recommended replacement types by category: `regular`, `next_gen`, `burstable`, `amd` |
| `ec2_classic` | boolean | Whether the type was available on EC2-Classic |
| `enhanced_networking` | boolean | Whether the type supports enhanced networking |
| `vcpu` | string | Number of vCPUs (as a string) |
| `nfu` | string | Normalized Factor Unit count (as a string) |
| `memory` | string | Memory in GiB (as a string) |

**Example:**

```json
{
  "m5.large": {
    "up": "m5.xlarge",
    "down": "m5.medium",
    "superseded": { "regular": "m6i.large", "next_gen": "m7i.large", "burstable": "", "amd": "m6a.large" },
    "ec2_classic": false,
    "enhanced_networking": true,
    "vcpu": "2",
    "nfu": "4",
    "memory": "8"
  }
}
```

### redshift_types.json

**Description:** Reference data for Amazon Redshift node types, including upgrade/downgrade relationships and hardware specifications. Used by policy templates that recommend Redshift cluster rightsizing.

**Structure:** Object keyed by Redshift node type name → specifications object.

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | Next larger node type to upgrade to |
| `down` | string or null | Next smaller node type to downgrade to |
| `vcpu` | number | Number of vCPUs |
| `memory` | number | Memory in GiB |
| `storage` | number | Managed storage capacity in TB |

**Example:**

```json
{
  "ra3.xlplus": {
    "up": "ra3.4xlarge",
    "down": "ra3.large",
    "vcpu": 4,
    "memory": 32,
    "storage": 32
  }
}
```
