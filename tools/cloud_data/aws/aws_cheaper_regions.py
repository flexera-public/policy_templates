#!/usr/bin/env python3
"""
Calculates and updates the cheaper and cheaper_ratio fields for AWS regions in
data/aws/regions.json.

For each region, every other region sharing the same geographic prefix is compared
using the median Linux on-demand EC2 price ratio (candidate / source) across all
instance types available in both regions. The cheapest in-prefix candidate becomes
the new value of the 'cheaper' field; the ratio becomes cheaper_ratio. If no
in-prefix region is strictly cheaper (ratio < 1.0), both fields are set to null.

Geographic prefixes are derived from the first dash-separated segment of the region
ID (e.g. us-east-1 → "us", ap-southeast-1 → "ap"). The us-gov-* regions form their
own "us-gov" group separate from commercial us-* regions.

Example: a cheaper_ratio of 0.85 means the recommended region is typically 15% cheaper.

Prerequisite: data/aws/aws_ec2_pricing.json must be present and up to date.
Produces:     data/aws/regions.json (cheaper and cheaper_ratio updated in place)
Usage:        python3 tools/cloud_data/aws/aws_cheaper_regions.py
              (Run from the root of the policy_templates repository.)
"""

import json
import statistics

PRICING_FILENAME = "data/aws/aws_ec2_pricing.json"
REGIONS_FILENAME = "data/aws/regions.json"


def get_prefix(region_id):
    """Return the geographic prefix for an AWS region ID.

    Returns "us-gov" for GovCloud regions, otherwise the first dash-separated
    segment (e.g. "us", "ap", "eu", "ca", "sa", "af", "me", "il", "mx").
    """
    if region_id.startswith("us-gov"):
        return "us-gov"
    return region_id.split("-")[0]


def compute_ratio(source_prices, candidate_prices):
    """Return the median Linux price ratio (candidate / source) for common instance types.

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


def find_cheapest_in_prefix(region_id, prefix, pricing, all_regions):
    """Return (cheapest_region_id, ratio) for the cheapest same-prefix candidate.

    Compares source_region against every other region that shares the same prefix
    and has pricing data. Returns (None, None) when the source has no pricing data
    or when no in-prefix candidate has a ratio strictly below 1.0.
    """
    source_prices = pricing.get(region_id)
    if not source_prices:
        return None, None

    best_region = None
    best_ratio = None

    for entry in all_regions:
        candidate_id = entry["region"]
        if candidate_id == region_id:
            continue
        if get_prefix(candidate_id) != prefix:
            continue
        candidate_prices = pricing.get(candidate_id)
        if not candidate_prices:
            continue

        ratio = compute_ratio(source_prices, candidate_prices)
        if ratio is not None and ratio < 1.0:
            if best_ratio is None or ratio < best_ratio:
                best_ratio = ratio
                best_region = candidate_id

    return best_region, best_ratio


def main():
    print(f"Reading pricing data from {PRICING_FILENAME}...")
    with open(PRICING_FILENAME) as f:
        pricing = json.load(f)

    print(f"Reading regions data from {REGIONS_FILENAME}...")
    with open(REGIONS_FILENAME) as f:
        regions = json.load(f)

    updated = 0
    cleared = 0
    unchanged = 0

    print("Computing cheapest in-prefix region for each region...")
    for entry in regions:
        region_id = entry["region"]
        prefix = get_prefix(region_id)

        new_cheaper, new_ratio = find_cheapest_in_prefix(region_id, prefix, pricing, regions)

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
            print(f"  [{prefix}] {region_id} -> {new_cheaper} (ratio={new_ratio}, {tag})")
        else:
            print(f"  [{prefix}] {region_id}: no cheaper region in prefix ({tag})")

    print(f"\nResults: {updated} updated, {cleared} cleared, {unchanged} unchanged.")
    print(f"Writing updated data to {REGIONS_FILENAME}...")

    with open(REGIONS_FILENAME, "w") as f:
        f.write(json.dumps(regions, indent=2, ensure_ascii=False))
        f.write("\n")

    print("DONE!")


if __name__ == "__main__":
    main()
