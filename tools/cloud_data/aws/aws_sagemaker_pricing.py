#!/usr/bin/env python3
"""
Downloads and processes SageMaker real-time inference hosting prices from the AWS Price List API.

Produces: data/aws/aws_sagemaker_pricing.json
Usage: python3 aws_sagemaker_pricing.py [--regions REGION [REGION ...]]
  (Run from the root of the policy_templates repository.)

Note: Requires AWS credentials with the pricing:GetProducts permission.
      The AWS Price List API is only available in us-east-1; this script always
      connects to us-east-1 regardless of which regions' prices are being fetched.
"""

import argparse
import json
import os
import sys
import time
import boto3

OUTPUT_FILENAME = "data/aws/aws_sagemaker_pricing.json"

# The AWS Price List API is only available in us-east-1.
PRICING_REGION = "us-east-1"
PRICING_SERVICE_CODE = "AmazonSageMaker"

# Operations that identify real-time inference endpoint hosting.
# This excludes training, batch transform, processing, notebook, and Studio usage.
REALTIME_HOSTING_OPERATIONS = {"SageMaker:Hosting"}

# Map AWS usagetype region prefixes to canonical AWS region codes.
# SageMaker usagetype values follow the pattern '{PREFIX}Hosting:{instance_type}',
# where PREFIX is a short region code followed by a dash (e.g. 'USE1-', 'USW2-').
# Entries with no prefix (e.g. "Hosting:ml.m5.xlarge") belong to us-east-1.
# This map is used as a fallback when the product's 'regionCode' attribute is absent.
USAGETYPE_PREFIX_MAP = {
    # US
    "": "us-east-1",
    "USE1-": "us-east-1",
    "USE2-": "us-east-2",
    "USW1-": "us-west-1",
    "USW2-": "us-west-2",
    # Europe
    "EU-": "eu-west-1",
    "EUW1-": "eu-west-1",
    "EUW2-": "eu-west-2",
    "EUW3-": "eu-west-3",
    "EUC1-": "eu-central-1",
    "EUC2-": "eu-central-2",
    "EUN1-": "eu-north-1",
    "EUS1-": "eu-south-1",
    "EUS2-": "eu-south-2",
    # Asia Pacific
    "APN1-": "ap-northeast-1",
    "APN2-": "ap-northeast-2",
    "APN3-": "ap-northeast-3",
    "APS1-": "ap-southeast-1",
    "APS2-": "ap-southeast-2",
    "APS3-": "ap-southeast-3",
    "APS4-": "ap-southeast-4",
    "AP1-": "ap-east-1",
    "AP2-": "ap-south-1",
    "AP3-": "ap-south-2",
    "AP4-": "ap-southeast-5",
    # Canada
    "CAC1-": "ca-central-1",
    "CAN1-": "ca-west-1",
    # South America
    "SAE1-": "sa-east-1",
    # Middle East
    "ME1-": "me-south-1",
    "MEC1-": "me-central-1",
    # Africa
    "AF1-": "af-south-1",
    # Israel
    "IL1-": "il-central-1",
    # AWS GovCloud
    "UGW1-": "us-gov-west-1",
    "UGE1-": "us-gov-east-1",
    "PDT-": "us-gov-west-1",
    # China
    "CN1-": "cn-north-1",
    "CNN1-": "cn-northwest-1",
}


def region_from_usagetype(usagetype):
    """Extract the AWS region code from a SageMaker usagetype string.

    SageMaker usagetype values follow the pattern '{PREFIX}Hosting:{instance_type}'.
    The prefix is a short region code followed by a dash, or absent for us-east-1.
    Returns None if the prefix is not in USAGETYPE_PREFIX_MAP.
    """
    hosting_pos = usagetype.find("Hosting")
    if hosting_pos < 0:
        return None
    prefix = usagetype[:hosting_pos]
    return USAGETYPE_PREFIX_MAP.get(prefix)


def get_products_with_retry(client, max_retries=3, backoff=5, **kwargs):
    """Call pricing.get_products with exponential backoff on failure."""
    for attempt in range(max_retries):
        try:
            return client.get_products(**kwargs)
        except Exception as e:
            if attempt < max_retries - 1:
                wait = backoff * (2 ** attempt)
                print(f"API call attempt {attempt + 1} failed: {e}. Retrying in {wait}s...", file=sys.stderr)
                time.sleep(wait)
            else:
                raise


def fetch_sagemaker_products(client):
    """Fetch all SageMaker product entries from the AWS Price List API.

    Returns a list of parsed product dicts. Paginates automatically using NextToken.
    """
    products = []
    kwargs = {
        "ServiceCode": PRICING_SERVICE_CODE,
        "MaxResults": 100,
    }

    page_num = 0
    while True:
        page_num += 1
        print(f"Fetching page {page_num} from AWS Price List API...", file=sys.stderr)
        response = get_products_with_retry(client, **kwargs)

        for price_str in response.get("PriceList", []):
            products.append(json.loads(price_str))

        next_token = response.get("NextToken")
        if not next_token:
            break
        kwargs["NextToken"] = next_token

    print(f"Fetched {len(products)} total product entries.", file=sys.stderr)
    return products


def is_realtime_hosting(attrs):
    """Return True if the product represents a real-time inference hosting instance.

    Filters to usagetype containing 'Hosting' and operation in REALTIME_HOSTING_OPERATIONS.
    This excludes training, batch transform, processing, notebook, and Studio usage types.
    """
    usagetype = attrs.get("usagetype", "")
    operation = attrs.get("operation", "")
    return "Hosting" in usagetype and operation in REALTIME_HOSTING_OPERATIONS


def extract_hourly_price(terms):
    """Extract the on-demand hourly USD price from a product's terms block.

    Navigates: terms > OnDemand > {offerTermCode} > priceDimensions > {rateCode} > pricePerUnit > USD
    Returns the highest positive price found, or None if no valid price exists.
    """
    on_demand = terms.get("OnDemand", {})
    best_price = None

    for offer_term in on_demand.values():
        for dimension in offer_term.get("priceDimensions", {}).values():
            usd_str = dimension.get("pricePerUnit", {}).get("USD", "0")
            try:
                price = float(usd_str)
            except (ValueError, TypeError):
                continue
            if price > 0 and (best_price is None or price > best_price):
                best_price = price

    return best_price


def build_pricing(products, regions_filter=None):
    """Build the final pricing dict keyed by region and instance type.

    Output structure: { "us-east-1": { "ml.m5.xlarge": 0.269, ... }, ... }

    Skips entries where the region cannot be determined or the price is zero or missing.
    If regions_filter is a set of region codes, only those regions are included.
    """
    pricing = {}
    skipped = 0
    included = 0

    for product in products:
        attrs = product.get("product", {}).get("attributes", {})

        if not is_realtime_hosting(attrs):
            continue

        instance_type = attrs.get("instanceType", "")
        if not instance_type:
            continue

        # Prefer the explicit 'regionCode' attribute; fall back to usagetype prefix parsing.
        region = attrs.get("regionCode", "")
        if not region:
            region = region_from_usagetype(attrs.get("usagetype", "")) or ""

        if not region:
            skipped += 1
            continue

        if regions_filter and region not in regions_filter:
            continue

        price = extract_hourly_price(product.get("terms", {}))
        if price is None:
            skipped += 1
            continue

        if region not in pricing:
            pricing[region] = {}

        # Keep the highest price for this (region, instance_type) pair.
        # Multiple SKUs can exist for the same instance; the highest positive
        # price is the standard on-demand rate.
        existing = pricing[region].get(instance_type)
        if existing is None or price > existing:
            pricing[region][instance_type] = price

        included += 1

    print(f"Included {included} pricing entries, skipped {skipped} (no region or zero/missing price).", file=sys.stderr)
    return pricing


def main():
    parser = argparse.ArgumentParser(
        description="Fetch SageMaker real-time inference hosting prices from the AWS Price List API."
    )
    parser.add_argument(
        "--regions",
        nargs="+",
        metavar="REGION",
        help="Limit output to these AWS region codes (e.g. us-east-1 us-west-2). Default: all regions.",
    )
    args = parser.parse_args()

    regions_filter = set(args.regions) if args.regions else None

    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)

    print("Connecting to AWS Price List API (us-east-1)...", file=sys.stderr)
    client = boto3.client("pricing", region_name=PRICING_REGION)

    print("Fetching SageMaker pricing data...", file=sys.stderr)
    products = fetch_sagemaker_products(client)

    print("Processing pricing data...", file=sys.stderr)
    pricing = build_pricing(products, regions_filter=regions_filter)

    print(f"Writing output to {OUTPUT_FILENAME}...", file=sys.stderr)
    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(pricing, sort_keys=True, indent=2))

    print("DONE!", file=sys.stderr)


if __name__ == "__main__":
    main()
