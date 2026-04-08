#!/usr/bin/env python3
"""
Calculates and updates the cheaper and cheaper_ratio fields for Azure regions in
data/azure/regions.json.

For each region, every other region sharing the same geographic group is compared
using the median Linux on-demand VM price ratio (candidate / source) across all
instance types available in both regions. The cheapest in-group candidate becomes
the new value of the 'cheaper' field; the ratio becomes cheaper_ratio. If no
in-group region is strictly cheaper (ratio < 1.0), both fields are set to null.

Because Azure ARM region IDs (e.g. "eastus") have no structured prefix equivalent
to AWS region IDs, geographic groups are defined in the AZURE_GEO_GROUPS table
below. Regions absent from the table (staging variants, geographic aggregates,
etc.) are excluded from all comparisons and always have cheaper=null.

The local azure_vm_pricing.json file keys pricing data by the Azure Retail Prices
API 'location' display name (e.g. "US East"), while data/azure/regions.json uses
ARM region IDs (e.g. "eastus"). This script fetches a compact ARM-to-location
mapping from the Azure Retail Prices API, then uses the local pricing file for all
ratio calculations.

Example: a cheaper_ratio of 0.85 means the recommended region is typically 15% cheaper.

Prerequisite: data/azure/azure_vm_pricing.json must be present and up to date.
Produces:     data/azure/regions.json (cheaper and cheaper_ratio updated in place)
Usage:        python3 tools/cloud_data/azure/azure_cheaper_regions.py
              (Run from the root of the policy_templates repository.)
"""

import json
import statistics

import requests

PRICING_FILENAME = "data/azure/azure_vm_pricing.json"
REGIONS_FILENAME = "data/azure/regions.json"
AZURE_PRICE_API = "https://prices.azure.com/api/retail/prices"

# Maps ARM region IDs to geographic groups. Mirrors the prefix-based grouping
# used for AWS (us, eu, ap, me, af, ca, br, mx). Regions not listed here are
# treated as staging/aggregate regions and are excluded from all comparisons.
AZURE_GEO_GROUPS = {
    # United States
    "eastus": "us", "eastus2": "us",
    "westus": "us", "westus2": "us", "westus3": "us",
    "centralus": "us", "northcentralus": "us",
    "southcentralus": "us", "westcentralus": "us",
    # Europe — one group so every European region can be compared against the
    # full EU portfolio (mirrors how ap-* covers all of Asia Pacific for AWS)
    "northeurope": "eu", "westeurope": "eu",
    "uksouth": "eu", "ukwest": "eu",
    "francecentral": "eu", "francesouth": "eu",
    "germanywestcentral": "eu", "germanynorth": "eu",
    "swedencentral": "eu",
    "norwayeast": "eu", "norwaywest": "eu",
    "switzerlandnorth": "eu", "switzerlandwest": "eu",
    "polandcentral": "eu",
    "italynorth": "eu",
    "spaincentral": "eu",
    # Asia Pacific
    "southeastasia": "ap", "eastasia": "ap",
    "japaneast": "ap", "japanwest": "ap",
    "koreacentral": "ap", "koreasouth": "ap",
    "centralindia": "ap", "southindia": "ap", "westindia": "ap",
    "jioindiacentral": "ap", "jioindiawest": "ap",
    "australiaeast": "ap", "australiasoutheast": "ap",
    "australiacentral": "ap", "australiacentral2": "ap",
    "newzealandnorth": "ap",
    # Middle East
    "uaenorth": "me", "uaecentral": "me",
    "qatarcentral": "me",
    "israelcentral": "me",
    # Africa
    "southafricanorth": "af", "southafricawest": "af",
    # Canada
    "canadacentral": "ca", "canadaeast": "ca",
    # Brazil / South America
    "brazilsouth": "br", "brazilsoutheast": "br",
    # Mexico
    "mexicocentral": "mx",
}


def build_arm_to_location_mapping(needed_arm_regions):
    """Build an armRegionName -> pricing location key mapping for the needed regions.

    Queries the Azure Retail Prices API for a widely-available VM SKU (Standard_D2s_v3)
    to extract all (armRegionName, location) pairs in a single, small API call. Falls
    back to a broader paginated query if any needed regions are still unmapped.

    Args:
        needed_arm_regions: Set of armRegionName strings that must be resolved.

    Returns:
        A dict mapping armRegionName -> location display name.
    """
    mapping = {}

    def fetch_mapping(params):
        url = AZURE_PRICE_API
        while url:
            response = requests.get(url, params=params)
            data = response.json()
            for item in data.get("Items", []):
                arm_region = item.get("armRegionName", "")
                location = item.get("location", "")
                if arm_region and location and arm_region not in mapping:
                    mapping[arm_region] = location
            if needed_arm_regions and needed_arm_regions.issubset(mapping.keys()):
                break
            url = data.get("NextPageLink")
            params = None

    print("  Pass 1: querying Azure Pricing API with Standard_D2s_v3 to build region mapping...")
    fetch_mapping({
        "$filter": (
            "serviceName eq 'Virtual Machines' and priceType eq 'Consumption' "
            "and armSkuName eq 'Standard_D2s_v3'"
        )
    })

    still_missing = needed_arm_regions - mapping.keys()
    if still_missing:
        print(f"  Pass 2: {len(still_missing)} region(s) still unmapped; retrying with broader query...")
        fetch_mapping({
            "$filter": "serviceName eq 'Virtual Machines' and priceType eq 'Consumption'"
        })

    still_missing = needed_arm_regions - mapping.keys()
    if still_missing:
        print(f"  WARNING: Could not resolve pricing location for: {sorted(still_missing)}")

    print(f"  Resolved {len(mapping)} ARM region(s) to pricing location name(s).")
    return mapping


def compute_ratio(source_prices, candidate_prices):
    """Return the median Linux price ratio (candidate / source) for common VM types.

    Returns a float rounded to 2 decimal places, or None if fewer than 2 common
    instance types with valid Linux on-demand pricing exist.
    """
    ratios = []
    for instance_type, source_data in source_prices.items():
        candidate_data = candidate_prices.get(instance_type)
        if not candidate_data:
            continue
        source_price = source_data.get("Linux", {}).get("pricePerUnit")
        candidate_price = candidate_data.get("Linux", {}).get("pricePerUnit")
        if source_price and candidate_price and float(source_price) > 0 and float(candidate_price) > 0:
            ratios.append(float(candidate_price) / float(source_price))

    if len(ratios) < 2:
        return None

    return round(statistics.median(ratios), 2)


def find_cheapest_in_group(region_id, geo_group, pricing, arm_to_location, all_regions):
    """Return (cheapest_region_id, ratio) for the cheapest same-group candidate.

    Compares the source region against every other region in the same geographic
    group that has both an ARM-to-location mapping and Azure VM pricing data.
    Returns (None, None) when no in-group candidate has a ratio strictly below 1.0.
    """
    source_location = arm_to_location.get(region_id)
    if not source_location:
        return None, None

    source_prices = pricing.get(source_location)
    if not source_prices:
        return None, None

    best_region = None
    best_ratio = None

    for entry in all_regions:
        candidate_id = entry["region"]
        if candidate_id == region_id:
            continue
        if AZURE_GEO_GROUPS.get(candidate_id) != geo_group:
            continue
        candidate_location = arm_to_location.get(candidate_id)
        if not candidate_location:
            continue
        candidate_prices = pricing.get(candidate_location)
        if not candidate_prices:
            continue

        ratio = compute_ratio(source_prices, candidate_prices)
        if ratio is not None and ratio < 1.0:
            if best_ratio is None or ratio < best_ratio:
                best_ratio = ratio
                best_region = candidate_id

    return best_region, best_ratio


def main():
    print(f"Reading regions data from {REGIONS_FILENAME}...")
    with open(REGIONS_FILENAME) as f:
        regions = json.load(f)

    # Only resolve ARM regions that actually participate in comparisons.
    needed_arm_regions = set(r["region"] for r in regions if r["region"] in AZURE_GEO_GROUPS)

    print(f"Building ARM region name -> pricing location mapping "
          f"for {len(needed_arm_regions)} region(s)...")
    arm_to_location = build_arm_to_location_mapping(needed_arm_regions)

    print(f"Reading pricing data from {PRICING_FILENAME}...")
    with open(PRICING_FILENAME) as f:
        pricing = json.load(f)

    updated = 0
    cleared = 0
    unchanged = 0

    print("Computing cheapest in-group region for each region...")
    for entry in regions:
        region_id = entry["region"]
        geo_group = AZURE_GEO_GROUPS.get(region_id)

        if geo_group is None:
            # Staging/aggregate region — always null; no comparison possible.
            new_cheaper, new_ratio = None, None
        else:
            new_cheaper, new_ratio = find_cheapest_in_group(
                region_id, geo_group, pricing, arm_to_location, regions
            )

        old_cheaper = entry.get("cheaper")
        old_ratio = entry.get("cheaper_ratio")

        entry["cheaper"] = new_cheaper
        entry["cheaper_ratio"] = new_ratio

        if new_cheaper == old_cheaper and new_ratio == old_ratio:
            unchanged += 1
            tag = "unchanged"
        elif new_cheaper is None:
            cleared += 1
            tag = f"cleared (was cheaper={old_cheaper}, ratio={old_ratio})"
        else:
            updated += 1
            parts = []
            if new_cheaper != old_cheaper:
                parts.append(f"cheaper: {old_cheaper} -> {new_cheaper}")
            if new_ratio != old_ratio:
                parts.append(f"ratio: {old_ratio} -> {new_ratio}")
            tag = ", ".join(parts)

        if new_cheaper:
            print(f"  [{geo_group}] {region_id} -> {new_cheaper} (ratio={new_ratio}, {tag})")
        elif geo_group:
            print(f"  [{geo_group}] {region_id}: no cheaper region in group ({tag})")

    print(f"\nResults: {updated} updated, {cleared} cleared, {unchanged} unchanged.")
    print(f"Writing updated data to {REGIONS_FILENAME}...")

    with open(REGIONS_FILENAME, "w") as f:
        f.write(json.dumps(regions, indent=2, ensure_ascii=False))
        f.write("\n")

    print("DONE!")


if __name__ == "__main__":
    main()
