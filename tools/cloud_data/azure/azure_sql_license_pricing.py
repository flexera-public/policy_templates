#!/usr/bin/env python3
"""
Fetches Azure SQL Server VM license pricing from the Azure Price API.

Produces: data/azure/azure_sql_license_pricing.json
Usage: python3 azure_sql_license_pricing.py
  (Run from the root of the policy_templates repository.)
"""

import requests
import json
import os
import re

OUTPUT_FILENAME = "data/azure/azure_sql_license_pricing.json"
API_URL = "https://prices.azure.com/api/retail/prices"

# SQL Server editions tracked in the output. Developer is always free (0).
EDITIONS = ["Enterprise", "Standard", "Web"]

# Maps exact Azure Retail Prices API productName values to output edition keys.
PRODUCT_NAME_MAP = {
    "SQL Server Enterprise": "Enterprise",
    "SQL Server Standard": "Standard",
    "SQL Server Web": "Web",
}


def fetch_all_prices(api_url, query):
    """Fetch all pages of results for the given OData filter query.

    Returns a flat list of all items across all pages.
    """
    response = requests.get(api_url, params={'$filter': query})
    json_data = response.json()

    price_list = json_data['Items']
    next_page = json_data['NextPageLink']

    # Follow pagination links until exhausted
    while next_page:
        response = requests.get(next_page)
        json_data = response.json()
        next_page = json_data['NextPageLink']
        price_list.extend(json_data['Items'])

    return price_list


def main():
    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)

    print("Gathering SQL Server license data from Azure Price API...")
    license_items = fetch_all_prices(
        API_URL,
        "serviceName eq 'Virtual Machines Licenses' and priceType eq 'Consumption' and "
        "(productName eq 'SQL Server Enterprise' or productName eq 'SQL Server Standard' or productName eq 'SQL Server Web')"
    )

    # Accumulate per-vCPU rates per edition to verify linearity and compute the rate.
    # The Azure API exposes prices as total cost for N vCPUs; we normalise to per-vCPU.
    per_vcpu_rates = {}

    print("Processing SQL Server license data from Azure Price API...")
    for item in license_items:
        retailPrice = item['retailPrice']
        unitOfMeasure = item['unitOfMeasure']
        meterName = item['meterName']
        productName = item['productName']

        # Only process hourly consumption meters
        if unitOfMeasure != "1 Hour":
            continue

        edition = PRODUCT_NAME_MAP.get(productName)
        if edition is None:
            continue

        # Extract vCPU count from meterName patterns such as "64 vCPU VM License"
        match = re.match(r'^(\d+)\s+vCPU\s+VM\s+License$', meterName, re.IGNORECASE)
        if not match:
            continue

        vcpu_count = int(match.group(1))
        if vcpu_count == 0:
            continue

        price_per_vcpu = retailPrice / vcpu_count

        if edition not in per_vcpu_rates:
            per_vcpu_rates[edition] = []
        per_vcpu_rates[edition].append(price_per_vcpu)

    # Build the final output. Use the minimum observed per-vCPU rate as a conservative
    # savings estimate (in practice all entries are perfectly linear so min == max).
    final_list = {}

    for edition in EDITIONS:
        rates = per_vcpu_rates.get(edition, [])
        if rates:
            final_list[edition] = round(min(rates), 6)
        else:
            final_list[edition] = 0

    # Developer edition is always free; include it explicitly so consumers can rely
    # on all four standard edition keys being present in the file.
    final_list["Developer"] = 0

    # Sort keys alphabetically for stable diffs
    final_list = dict(sorted(final_list.items()))

    print("Writing results to file...")

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(final_list, indent=2))
        f.write("\n")

    print("DONE!")
    for edition, rate in final_list.items():
        print(f"  {edition}: ${rate}/vCPU/hr")


if __name__ == "__main__":
    main()
