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
- `generation`
- `generation_next`

Instance types that have no entry in `instance_types.json` have `null` for both `generation` and `generation_next`.

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
| `generation` | string or null | Generation of the instance type: `current`, `previous`, or `retired`. `null` if the type is not listed in `instance_types.json`. See the generation values in the `instance_types.json` section below. |
| `generation_next` | string or null | Date, in `YYYY-MM-DD` format, when the instance type is expected to move to the next generation stage (`current` to `previous`, or `previous` to `retired`); `null` if AWS has not announced a date or if the type is not listed in `instance_types.json` |

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
  "ec2_classic": false,
  "generation": "current",
  "generation_next": null
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

### aws_sagemaker_pricing.json

**Script:** [`tools/cloud_data/aws/aws_sagemaker_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/aws/aws_sagemaker_pricing.py)

**Workflow:** [Generate AWS SageMaker Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-aws-sagemaker-pricing-json.yaml)

**Description:** On-demand SageMaker real-time inference endpoint hosting prices by region and instance type. Sourced from the AWS Price List API (`pricing:GetProducts`, ServiceCode: `AmazonSageMaker`). Only real-time inference hosting entries are included (usagetype containing `Hosting`, operation `SageMaker:Hosting`); training, batch transform, processing, notebook, and Studio entries are excluded. Used by policy templates that estimate costs or calculate savings for idle SageMaker endpoint recommendations.

**Structure:** Object keyed by AWS region code → SageMaker instance type → on-demand hourly price in USD.

| Field | Type | Description |
| --- | --- | --- |
| (price value) | number | On-demand hourly price in USD for the given region and instance type |

**Example:**

```json
{
  "us-east-1": {
    "ml.m5.2xlarge": 0.538,
    "ml.m5.xlarge": 0.269
  },
  "us-west-2": {
    "ml.m5.2xlarge": 0.538,
    "ml.m5.xlarge": 0.269
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

**Description:** Legacy reference data for EC2 instance types. This file is older and manually maintained. It should not be used in new policy templates. It exists to ensure that older policy templates continue to function and to supply some fields (such as `superseded`, `burst_info`, `ec2_classic`, `generation`, and `generation_next`) to the auto-generated `aws_ec2_instance_types.json` until automation is built for those fields. Each entry also records the generation of the instance type and, when AWS has announced one, the date it is expected to change, as described in the generation values below.

**Structure:** Object keyed by instance type name → specifications object.

| Field | Type | Description |
| --- | --- | --- |
| `generation` | string | Generation of the instance type: `current`, `previous`, or `retired`. See the generation values below. |
| `generation_next` | string or null | Date, in `YYYY-MM-DD` format, when the instance type is expected to move to the next generation stage (`current` to `previous`, or `previous` to `retired`); `null` if AWS has not announced a date. See the generation values below. |
| `up` | string or null | Next larger instance type in the same family |
| `down` | string or null | Next smaller instance type in the same family |
| `superseded` | object | Recommended replacement types by category: `regular`, `next_gen`, `burstable`, `amd` |
| `ec2_classic` | boolean | Whether the type was available on EC2-Classic |
| `enhanced_networking` | boolean | Whether the type supports enhanced networking |
| `vcpu` | string | Number of vCPUs (as a string) |
| `nfu` | string | Normalized Factor Unit count (as a string) |
| `memory` | string | Memory in GiB (as a string) |

**Generation values:**

- `current` - A current generation instance type that AWS recommends for new deployments.
- `previous` - An older generation instance type. It can still be launched in at least one AWS Region, but AWS no longer treats it as current generation.
- `retired` - The instance type can no longer be launched, either because AWS has removed it or ended its sale, or because the name does not match any instance type that AWS offers.

For EC2 instance types, the values come from the [EC2 Instance Types guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html) and the EC2 [DescribeInstanceTypes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceTypes.html) API. A type is `previous` if the guide lists it as a [previous generation instance](https://docs.aws.amazon.com/ec2/latest/instancetypes/pg.html) or if the API reports `CurrentGeneration` as `false` (the `properties.currentGeneration` field in `aws_ec2_instance_types.json`). The API is more recent than the guide for the `c5`, `c6gn`, `d2`, `g5`, `m5`, `m6i`, `r5`, `r6i`, `r7g`, and `r7gd` families, which the guide still lists as current generation, so these families are `previous`. `p3dn.24xlarge` is the reverse: the guide lists it as previous generation but the API reports it as current generation, so it is also `previous`. All other types that the guide lists and the API reports as current generation are `current`.

An EC2 type is `retired` when AWS has removed it. The `p3` family was [removed on 2026-01-01](https://docs.aws.amazon.com/ec2/latest/instancetypes/doc-history.html) and the `u-9tb1`, `u-12tb1`, `u-18tb1`, and `u-24tb1` families reached end of sale on 2025-06-20. The `dl1` and `g4ad` families are no longer returned by the API and are not listed in any Region on the [instance types by Region](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-regions.html) page. Very old types that the guide and the API no longer mention at all (`cc1`, `cc2`, `cg1`, `cr1`, `g2`, `hi1`, and `hs1`) are also `retired`, as are the `g4` family and the `m6g.24xlarge` and `m6gd.24xlarge` sizes, whose names do not match any instance type that AWS offers.

The `p2`, `f1`, and `g3s` families are `previous` rather than `retired` because the instance types by Region page still lists them in AWS GovCloud (US-West). The `i3.metal` and `u-6tb1.metal` sizes are `current` because the guide still lists them as current generation, even though the API does not return them.

The `db.*` entries are Amazon RDS DB instance classes, so their values follow the [RDS DB instance class documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Types.html) instead of the EC2 sources. The `db.m1`, `db.m2`, `db.m3`, `db.m4`, `db.r3`, `db.r4`, `db.t1`, and `db.t2` classes are `retired`: RDS ended support for `db.m4`, `db.r4`, and `db.t2` on 2024-12-31, no longer allows new `db.m3` and `db.r3` DB instances and began automatically upgrading existing ones on 2023-02-01, and no longer documents `db.m1`, `db.m2`, and `db.t1`. All other `db.*` classes are `current`, because RDS documents them as supported and does not publish a list of previous generation classes.

The `generation_next` field is the date when an instance type is expected to move to the next stage: from `current` to `previous`, or from `previous` to `retired`. A date is recorded only if it can be verified in official AWS documentation or announcements; otherwise the field is explicitly `null`. It is always `null` for `retired` types, because they have no next stage. When this data was last reviewed (2026-11-06), no upcoming date had been published for any EC2 instance type or RDS DB instance class, so every entry is `null`. AWS does not announce when a type stops being current generation, and its [EC2 FAQ](https://aws.amazon.com/ec2/faqs/) states that previous generation instances remain fully supported and that customers will be notified if AWS decides to deprecate them. Dates that have already passed, such as those listed above for the `p3`, `u-9tb1`, `u-12tb1`, `u-18tb1`, `u-24tb1`, `db.m3`, `db.m4`, `db.r3`, `db.r4`, and `db.t2` types, are not recorded because they are not upcoming changes.

This data is a point-in-time snapshot that must be updated manually when AWS changes the status of an instance type or announces a date for a change. New instance types that appear in `aws_ec2_instance_types.json` have `null` for `generation` and `generation_next` until an entry for them is added to this file.

**Example:**

```json
{
  "m5.large": {
    "generation": "previous",
    "generation_next": null,
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
