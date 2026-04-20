# Azure Cloud Data

Various Azure-specific data assets, such as pricing data. Some assets are manually maintained and some are generated through automation; see the [Cloud Data Scripts README](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/README.md) for more information on how these assets are generated.

## Auto-Generated Files

The following files are produced by scripts in [`tools/cloud_data/azure/`](https://github.com/flexera-public/policy_templates/tree/master/tools/cloud_data/azure) and are kept up to date by scheduled GitHub Actions workflows that open automated pull requests when the data changes.

### azure_compute_instance_types.json

**Script:** [`tools/cloud_data/azure/azure_compute_instance_types.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_compute_instance_types.py)

**Workflow:** [Generate Azure Compute Instance Types JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-compute-instance-types-json.yaml)

**Description:** A JSON array of Azure virtual machine SKU objects. Data is fetched from the Azure Management API and merged with Instance Size Flexibility (ISF) ratio data and select fields from the legacy `instance_types.json` file. Use this file in policy templates that need detailed specifications for Azure VM instance types.

Some fields are currently sourced from the legacy `instance_types.json` file until proper automation is built to derive them:

- `superseded`
- `specs.nfu`

**Structure:** Array of objects, one per VM SKU.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Full VM size name, e.g. `"Standard_D2s_v3"` |
| `tier` | string | Pricing tier, e.g. `"Standard"` or `"Basic"` |
| `size` | string | Size portion of the name, e.g. `"D2s_v3"` |
| `family` | string | Azure VM family identifier, e.g. `"standardDSv3Family"` |
| `superseded` | object | Recommended replacement SKUs, e.g. `{ "regular": "Standard_D2s_v5" }` |
| `localDisk` | boolean | Whether the VM size includes a local (temporary) disk |
| `specs` | object | Raw Azure API capability values: `vCPUs`, `MemoryGB`, `MaxDataDiskCount`, `PremiumIO`, `AcceleratedNetworkingEnabled`, `nfu`, and many others |

**Example:**

```json
{
  "name": "Standard_D2s_v3",
  "tier": "Standard",
  "size": "D2s_v3",
  "family": "standardDSv3Family",
  "superseded": { "regular": "Standard_D2s_v5" },
  "localDisk": false,
  "specs": {
    "nfu": "4",
    "vCPUs": "2",
    "MemoryGB": "8",
    "MaxDataDiskCount": "4",
    "PremiumIO": "True"
  }
}
```

### azure_db_storage_pricing.json

**Script:** [`tools/cloud_data/azure/azure_db_storage_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_db_storage_pricing.py)

**Workflow:** [Generate Azure DB Storage Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-db-storage-pricing-json.yaml)

**Description:** Per-region, per-tier storage pricing (USD per GB per month) for Azure SQL Database. Sourced from the Azure Retail Prices API. Used by policy templates that estimate costs related to Azure SQL Database storage.

**Structure:** Object keyed by ARM region name → service tier → pricing object.

| Field | Type | Description |
| --- | --- | --- |
| `sku` | string | Azure Retail Prices API SKU identifier |
| `unitPrice` | number | Price per GB per month in USD |

**Service tiers:** `BusinessCritical`, `GeneralPurpose`, `Hyperscale`

**Example:**

```json
{
  "eastus": {
    "BusinessCritical": { "sku": "DZH318Z0BQDS/0008", "unitPrice": 0.3 },
    "GeneralPurpose": { "sku": "DZH318Z0BQDS/0009", "unitPrice": 0.115 }
  }
}
```

### azure_linux_license_pricing.json

**Script:** [`tools/cloud_data/azure/azure_linux_license_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_linux_license_pricing.py)

**Workflow:** [Generate Azure Linux License Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-linux-license-pricing-json.yaml)

**Description:** Hourly license prices (USD) for Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES) on Azure, sourced from the `Virtual Machines Licenses` service in the Azure Retail Prices API. These are global prices (not region-specific). Used by policy templates that calculate estimated savings from enabling Azure Hybrid Use Benefit on Linux VMs.

**Structure:** Object with two top-level keys, `RHEL` and `SUSE`, each containing product names mapped to pricing tables.

For **RHEL**, each product maps vCPU count (as a string integer) to a USD hourly price.

For **SUSE**, each product maps a vCPU tier range string to a USD hourly price. Tier range keys are `"1-2"`, `"3-4"`, and `"5+"`.

**RHEL products:** `Red Hat Enterprise Linux`, `Red Hat Enterprise Linux with HA`, `Red Hat Enterprise Linux for SAP with HA`, `SQL Server Enterprise Red Hat Enterprise Linux`, `SQL Server Standard Red Hat Enterprise Linux`, `SQL Server Web Red Hat Enterprise Linux`

**SUSE products:** `SUSE Linux Enterprise Server Standard`, `SUSE Linux Enterprise Server Priority`, `SUSE Linux Enterprise Server for HPC Standard`, `SUSE Linux Enterprise Server for HPC Priority`, `SUSE for SAP Linux Enterprise Server`, `SUSE Enterprise Linux Server for SQL with HA`

**Example:**

```json
{
  "RHEL": {
    "Red Hat Enterprise Linux": {
      "1": 0.0144,
      "2": 0.0288,
      "4": 0.0576,
      "8": 0.1152
    }
  },
  "SUSE": {
    "SUSE Linux Enterprise Server Standard": {
      "1-2": 0.065,
      "3-4": 0.125,
      "5+": 0.15
    }
  }
}
```

### azure_md_pricing.json

**Script:** [`tools/cloud_data/azure/azure_md_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_md_pricing.py)

**Workflow:** [Generate Azure MD Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-md-pricing-json.yaml)

**Description:** Per-region, per-SKU pricing for Azure Managed Disks, sourced from the Azure Retail Prices API. Prices are in USD per month. Used by policy templates that estimate costs or savings related to Azure Managed Disk rightsizing or deletion.

**Structure:** Object keyed by region display name (or `"Global"` for globally priced SKUs) → disk SKU identifier → pricing object. Region keys use the Azure Retail Prices API display name format (e.g. `"US East"`).

| Field | Type | Description |
| --- | --- | --- |
| `sku` | string | Human-readable SKU name, e.g. `"E10 LRS"` |
| `currencyCode` | string | Always `"USD"` |
| `pricePerUnit` | number | Price per month in USD |
| `unitOfMeasure` | string | Always `"1/Month"` |
| `productName` | string | Azure product name, e.g. `"Standard SSD Managed Disks"` |

**Example:**

```json
{
  "US East": {
    "E10_LRS": {
      "currencyCode": "USD",
      "sku": "E10 LRS",
      "pricePerUnit": 8.0,
      "unitOfMeasure": "1/Month",
      "productName": "Standard SSD Managed Disks"
    }
  }
}
```

### azure_md_tier_types.json

**Script:** [`tools/cloud_data/azure/azure_md_tier_types.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_md_tier_types.py)

**Description:** Technical specifications and upgrade/downgrade relationships for all Azure Managed Disk SKUs (Standard HDD `S`, Standard SSD `E`, and Premium SSD `P` tiers). This file is generated by running `azure_md_tier_types.py`, which contains the tier data as static constants. There is no scheduled workflow; update the script constants and regenerate if Azure releases new disk SKUs. Used by policy templates that recommend Managed Disk rightsizing.

**Structure:** Object keyed by disk SKU identifier (e.g. `"E10"`, `"S30"`, `"P40"`) → specifications object.

| Field | Type | Description |
| --- | --- | --- |
| `sizeGiB` | number | Disk capacity in GiB |
| `tier` | string | Disk product tier: `"Standard"`, `"StandardSSD"`, or `"Premium"` |
| `IOPS` | number | Maximum IOPS for the disk SKU |
| `throughput` | number | Maximum throughput in MB/s |
| `maxShares` | number | Maximum number of VMs that can share the disk; `-1` = not supported |
| `maxBurstIOPS` | number | Maximum burst IOPS; `-1` = no burst support |
| `maxBurstThroughput` | number | Maximum burst throughput in MB/s; `-1` = no burst support |
| `downgrades` | object | `{ "tier": <tier_name_or_null>, "size": <sku_or_null> }` — the recommended smaller SKU within the same tier, if one exists |

**Example:**

```json
{
  "E10": {
    "sizeGiB": 128,
    "tier": "StandardSSD",
    "IOPS": 500,
    "throughput": 60,
    "maxShares": 3,
    "maxBurstIOPS": 4000,
    "maxBurstThroughput": 200,
    "downgrades": { "tier": null, "size": "E6" }
  }
}
```

### azure_sqlmi_storage_pricing.json

**Script:** [`tools/cloud_data/azure/azure_sqlmi_storage_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_sqlmi_storage_pricing.py)

**Workflow:** [Generate Azure SQL MI Storage Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-sqlmi-storage-pricing-json.yaml)

**Description:** Per-region, per-tier storage pricing (USD per GB per month) for Azure SQL Managed Instance. Sourced from the Azure Retail Prices API. Used by policy templates that estimate costs related to Azure SQL Managed Instance storage.

**Structure:** Object keyed by ARM region name → service tier → pricing object. Identical in shape to `azure_db_storage_pricing.json`.

| Field | Type | Description |
| --- | --- | --- |
| `sku` | string | Azure Retail Prices API SKU identifier |
| `unitPrice` | number | Price per GB per month in USD |

**Service tiers:** `BusinessCritical`, `GeneralPurpose`

**Example:**

```json
{
  "eastus": {
    "BusinessCritical": { "sku": "DZH318Z0BQDX/0001", "unitPrice": 0.3 },
    "GeneralPurpose": { "sku": "DZH318Z0BQDX/000D", "unitPrice": 0.115 }
  }
}
```

### azure_vm_families.json

**Script:** [`tools/cloud_data/azure/azure_vm_families.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_vm_families.py)

**Workflow:** [Generate Azure VM Families JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-vm-families-json.yaml)

**Description:** Instance Size Flexibility (ISF) ratio table for Azure VM sizes. ISF ratios are used by Azure Reserved Instance recommendations to determine how a reservation for one VM size applies to other sizes in the same family. Used by policy templates that analyze Reserved Instance coverage or recommend RI purchases.

**Structure:** Array of objects, one per VM size.

| Field | Type | Description |
| --- | --- | --- |
| `instance_family` | string | Human-readable Azure VM family name, e.g. `"Av2 Series"` |
| `instance_type` | string | Full VM size name, e.g. `"Standard_A2_v2"` |
| `ratio` | number | ISF ratio relative to the smallest size in the family |

**Example:**

```json
[
  { "instance_family": "Av2 Series", "instance_type": "Standard_A1_v2", "ratio": 1 },
  { "instance_family": "Av2 Series", "instance_type": "Standard_A2_v2", "ratio": 2.1 },
  { "instance_family": "Av2 Series", "instance_type": "Standard_A4_v2", "ratio": 4.4 }
]
```

### azure_vm_pricing.json

**Script:** [`tools/cloud_data/azure/azure_vm_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_vm_pricing.py)

**Workflow:** [Generate Azure VM Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-vm-pricing-json.yaml)

**Description:** Hourly on-demand (Consumption) and AHUB-eligible (DevTestConsumption) retail prices in USD for Azure VM SKUs by region and OS. Sourced from the Azure Retail Prices API. Used by policy templates that calculate costs or estimate savings from Azure Hybrid Use Benefit on Windows VMs.

**Structure:** Object keyed by region display name (Azure Retail Prices API format, e.g. `"US East"`) → VM type group identifier → OS key → pricing object. The OS key is typically `"Linux"` or `"Windows"`.

| Field | Type | Description |
| --- | --- | --- |
| `pricePerUnit` | number | Hourly on-demand (Consumption) price in USD |
| `pricePerUnitAHUB` | number or null | Hourly AHUB/DevTest price in USD; `null` if not available for this SKU |
| `sku` | string | Azure Retail Prices API SKU identifier |

**Example:**

```json
{
  "US East": {
    "Dsv3 Type3": {
      "Linux": {
        "pricePerUnit": 0.096,
        "pricePerUnitAHUB": null,
        "sku": "DZH318Z0BQPS"
      },
      "Windows": {
        "pricePerUnit": 0.188,
        "pricePerUnitAHUB": 0.096,
        "sku": "DZH318Z0BQPT"
      }
    }
  }
}
```

### regions.json

**Script:** [`tools/cloud_data/azure/azure_cheaper_regions.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_cheaper_regions.py)

**Workflow:** [Update Azure Cheaper Region Ratios](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-azure-cheaper-regions.yaml)

**Description:** A list of all Azure regions with their ARM region ID, display name, and information about the cheapest alternative region in the same geographic group. The `cheaper` and `cheaper_ratio` fields are calculated by comparing median Linux on-demand VM prices across all instance types available in both regions. Regions not assigned to a geographic group have `null` values for both fields. Used by policy templates that recommend relocating resources to lower-cost regions.

**Structure:** Array of objects, one per Azure region.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Azure region display name, e.g. `"East US"` |
| `region` | string | ARM region identifier, e.g. `"eastus"` |
| `cheaper` | string or null | ARM region ID of the cheapest in-group alternative; `null` if no cheaper region exists or the region has no group assignment |
| `cheaper_ratio` | number or null | Ratio of the cheaper region's median price to this region's median price (values below `1.0` indicate the alternative is cheaper); `null` when `cheaper` is `null` |

**Example:**

```json
[
  { "name": "East US", "region": "eastus", "cheaper": null, "cheaper_ratio": null },
  { "name": "South Central US", "region": "southcentralus", "cheaper": "eastus", "cheaper_ratio": 0.83 }
]
```

## Manually Maintained Files

The following files do not have automated generation scripts that pull from live APIs. They must be updated manually when Azure adds new SKUs, service tiers, or OS versions. Open a pull request to update them.

### azure_esu_os_versions.json

**Description:** A list of Windows and SQL Server OS versions that are eligible for, or are subject to, Azure Extended Security Updates (ESU). Each entry defines how to identify a VM image by its publisher, offer, or SKU strings, along with the OS end-of-life date and ESU timeline. Used by policy templates that identify VMs running OS versions that incur Extended Security Update charges.

**Structure:** Array of objects, one per OS version.

| Field | Type | Description |
| --- | --- | --- |
| `publisher` | string | Azure image publisher name, e.g. `"MicrosoftWindowsServer"` |
| `sku_contains` | string | Substring to match against the image SKU field |
| `offer_contains` | string | Substring to match against the image offer field |
| `os_name` | string | Human-readable OS name, e.g. `"Windows Server 2012 R2"` |
| `eol_date` | string | ISO 8601 date when mainstream support ended |
| `esu_end_date` | string | ISO 8601 date when Extended Security Updates end |
| `esu_status` | string | Current ESU status, e.g. `"Year 1"`, `"Year 2"`, `"Year 3"` |

**Example:**

```json
[
  {
    "publisher": "MicrosoftWindowsServer",
    "sku_contains": "2012-R2",
    "offer_contains": "WindowsServer",
    "os_name": "Windows Server 2012 R2",
    "eol_date": "2018-10-09",
    "esu_end_date": "2026-10-13",
    "esu_status": "Year 3"
  }
]
```

### azure_synapse_tier_types.json

**Description:** The ordered scale-up and scale-down chain for Azure Synapse Analytics (dedicated SQL pool) DWU SKUs. Used by policy templates that recommend scaling Synapse pools up or down.

**Structure:** Object keyed by Synapse DWU SKU name → resize relationship object.

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | The next larger DWU SKU; `null` if this is the largest available |
| `down` | string or null | The next smaller DWU SKU; `null` if this is the smallest available |

**Example:**

```json
{
  "DW100c": { "up": "DW200c", "down": null },
  "DW200c": { "up": "DW300c", "down": "DW100c" },
  "DW30000c": { "up": null, "down": "DW15000c" }
}
```

### instance_types.json

**Description:** Legacy VM instance type data. An older, manually maintained counterpart to `azure_compute_instance_types.json`. **Do not use this file in new policy templates.** It is retained only to ensure existing policy templates that reference it continue to function. Some fields in `azure_compute_instance_types.json` (specifically `superseded` and `specs.nfu`) are currently sourced from this file.

**Structure:** Object keyed by VM size name → resize and specification object.

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | The next larger VM size in the same family |
| `down` | string or null | The next smaller VM size in the same family |
| `superseded` | object or null | Recommended replacement sizes, e.g. `{ "regular": "Standard_D2s_v5" }` |
| `vcpu` | number | Number of vCPUs |
| `memory` | string | Memory in GB as a string, e.g. `"8"` |

**Example:**

```json
{
  "Standard_D2s_v3": {
    "up": "Standard_D4s_v3",
    "down": "Standard_D1s_v3",
    "superseded": { "regular": "Standard_D2s_v5" },
    "vcpu": 2,
    "memory": "8"
  }
}
```

### mysql_flexible_tier_types.json

**Description:** The ordered scale-up and scale-down chain for Azure Database for MySQL Flexible Server SKUs, organized by compute tier. Used by policy templates that recommend rightsizing MySQL Flexible Server instances.

**Structure:** Object keyed by compute tier name → SKU name → resize relationship object.

**Compute tiers:** `Burstable`, `GeneralPurpose`, `MemoryOptimized`

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | vCPU count of the next larger SKU in the tier; `null` if largest |
| `down` | string or null | vCPU count of the next smaller SKU in the tier; `null` if smallest |
| `up_sku` | string or null | Full SKU name of the next larger instance; `null` if largest |
| `down_sku` | string or null | Full SKU name of the next smaller instance; `null` if smallest |

**Example:**

```json
{
  "Burstable": {
    "Standard_B1s": { "up": "2", "down": null, "up_sku": "Standard_B2s", "down_sku": null },
    "Standard_B2s": { "up": "4", "down": "1", "up_sku": "Standard_B4ms", "down_sku": "Standard_B1s" }
  }
}
```

### resource_types.json

**Description:** A catalog of Azure resource type strings with flags indicating whether each type appears in cost reports and supports resource tags. Used by policy templates that enumerate or filter Azure resources by type.

**Structure:** Object keyed by Azure resource type string (e.g. `"Microsoft.Compute/virtualMachines"`) → attribute flags object.

| Field | Type | Description |
| --- | --- | --- |
| `costReport` | boolean | Whether this resource type typically generates cost line items |
| `supportsTags` | boolean | Whether Azure allows tags to be applied to resources of this type |

**Example:**

```json
{
  "Microsoft.Compute/virtualMachines": { "costReport": true, "supportsTags": true },
  "Microsoft.AAD/DomainServices/oucontainer": { "costReport": false, "supportsTags": false }
}
```

### sql_service_tier_types.json

**Description:** The ordered scale-up and scale-down chain for Azure SQL Database SKUs, organized by service tier. Used by policy templates that recommend rightsizing Azure SQL Database instances.

**Structure:** Object keyed by service tier name → SKU identifier → resize relationship object.

**Service tiers:** `Basic`, `Standard`, `Premium`, `GeneralPurpose`, `Hyperscale`, `BusinessCritical`

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | SKU identifier of the next larger option within this tier; `null` if largest |
| `down` | string or null | SKU identifier of the next smaller option within this tier; `null` if smallest |

**Example:**

```json
{
  "Standard": {
    "Standard_10": { "up": "20", "down": null },
    "Standard_20": { "up": "50", "down": "10" },
    "Standard_50": { "up": "100", "down": "20" }
  }
}
```

### sqlmi_tier_types.json

**Description:** The ordered scale-up and scale-down chain for Azure SQL Managed Instance SKUs, organized by service tier. Used by policy templates that recommend rightsizing Azure SQL Managed Instance deployments.

**Structure:** Object keyed by service tier name → SKU identifier → resize relationship object.

**Service tiers:** `GeneralPurpose`, `Hyperscale`, `BusinessCritical`

| Field | Type | Description |
| --- | --- | --- |
| `up` | string or null | SKU identifier of the next larger option within this tier; `null` if largest |
| `down` | string or null | SKU identifier of the next smaller option within this tier; `null` if smallest |

**Example:**

```json
{
  "GeneralPurpose": {
    "GP_Gen5_4": { "up": "8", "down": null },
    "GP_Gen5_8": { "up": "16", "down": "4" },
    "GP_Gen5_16": { "up": "24", "down": "8" }
  }
}
```
