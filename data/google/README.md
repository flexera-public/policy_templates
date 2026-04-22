# Google Cloud Data

Various Google-specific data assets, such as pricing data. Some assets are manually maintained and some are generated through automation; see the [Cloud Data Scripts README](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/README.md) for more information on how these assets are generated.

## Auto-Generated Files (Manual Run)

The following files are produced by scripts in [`tools/cloud_data/google/`](https://github.com/flexera-public/policy_templates/tree/master/tools/cloud_data/google). Unlike the AWS and Azure scripts, there are no scheduled GitHub Actions workflows for these files; they must be regenerated manually by running the scripts locally when an update is needed.

### google_compute_instance_types.json

**Script:** [`tools/cloud_data/google/google_compute_instance_types.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/google/google_compute_instance_types.py)

**Description:** A JSON array of all Google Compute Engine (GCE) VM instance type objects. Data is fetched from the GCE `machineTypes.aggregatedList` API. Use this file in policy templates that need detailed specifications for GCE instance types.

**Note:** Requires Google Application Default Credentials with `compute.machineTypes.list` permission to run.

**Structure:** Array of objects, one per GCE machine type.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Full machine type name, e.g. `"n2-standard-4"` |
| `family` | string | Instance family prefix, e.g. `"n2"` |
| `variant` | string | Variant portion of the name after the family, e.g. `"standard-4"` |
| `description` | string | Human-readable description including vCPU and RAM specs |
| `superseded` | object or null | Recommended replacement machine types; `null` if not superseded |
| `zones` | array | List of GCP zones where this machine type is available |
| `specs` | object | Raw GCE API fields: `guestCpus`, `memoryMb`, `memoryGb`, `imageSpaceGb`, `maximumPersistentDisks`, `maximumPersistentDisksSizeGb`, `isSharedCpu`, `architecture`, `accelerators`, `scratchDisks` |

**Example:**

```json
{
  "name": "n2-standard-4",
  "family": "n2",
  "variant": "standard-4",
  "description": "General-purpose: 4 vCPUs, 16 GB RAM",
  "superseded": null,
  "zones": ["us-central1-a", "us-central1-b"],
  "specs": {
    "guestCpus": 4,
    "memoryMb": 16384,
    "memoryGb": 16,
    "imageSpaceGb": 0,
    "maximumPersistentDisks": 128,
    "isSharedCpu": false,
    "architecture": "X86_64"
  }
}
```

### google_vm_pricing.json

**Script:** [`tools/cloud_data/google/google_vm_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/google/google_vm_pricing.py)

**Description:** Estimated on-demand hourly prices in USD for all GCE machine types, computed using per-vCPU and per-GB-RAM prices for the `us-central1-a` zone. Prices are calculated as `vCPUs × vCPU_price + memory_GB × memory_price`. Used by policy templates that estimate costs or calculate savings for GCE rightsizing recommendations.

**Note:** Requires Google Application Default Credentials with `cloudbilling.services.get` permission to run.

**Structure:** Object keyed by machine type name → estimated hourly price in USD (number).

**Example:**

```json
{
  "n2-standard-4": 0.1902,
  "n2-standard-8": 0.3804,
  "e2-micro": 0.0084
}
```

## Manually Maintained Files

### instance_types.json

**Description:** Legacy reference data for GCE machine types. This file is older and manually maintained. It should not be used in new policy templates. It exists to ensure that older policy templates continue to function as intended.

**Structure:** Object keyed by machine type name → specifications object.

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | Next larger machine type to upgrade to |
| `down` | string or null | Next smaller machine type to downgrade to |
| `superseded` | object or null | Recommended replacement machine types |

**Example:**

```json
{
  "n1-standard-4": {
    "up": "n1-standard-8",
    "down": "n1-standard-2",
    "superseded": { "regular": "n2-standard-4" }
  }
}
```

### regions.json

**Description:** A reference list of all Google Cloud regions, each annotated with the cheapest alternative region in the same geographic group (if one exists). Used by policy templates that recommend moving workloads to cheaper regions.

**Structure:** Array of objects, one per GCP region.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Human-readable region name, e.g. `"US Central Iowa"` |
| `region` | string | GCP region code, e.g. `"us-central1"` |
| `cheaper` | string or null | Region code of the cheapest comparable region; `null` if this region is already the cheapest |
| `cheaper_ratio` | number or null | Ratio of cheaper region median price to this region's median price (e.g. `0.86` = 14% cheaper); `null` if no cheaper region |

**Example:**

```json
[
  { "name": "US Central Iowa", "region": "us-central1", "cheaper": null, "cheaper_ratio": null },
  { "name": "Asia Pacific Hong Kong", "region": "asia-east2", "cheaper": "asia-east1", "cheaper_ratio": 0.86 }
]
```
