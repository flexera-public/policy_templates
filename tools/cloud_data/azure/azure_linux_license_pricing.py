#!/usr/bin/env python3
"""
Fetches Azure Linux VM license pricing (RHEL and SUSE) from the Azure Price API.

Produces: data/azure/azure_linux_license_pricing.json
Usage: python3 azure_linux_license_pricing.py
  (Run from the root of the policy_templates repository.)
"""

import requests
import json
import os
import re

OUTPUT_FILENAME = "data/azure/azure_linux_license_pricing.json"
API_URL = "https://prices.azure.com/api/retail/prices"


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

    print("Gathering Linux license data from Azure Price API...")
    license_items = fetch_all_prices(
        API_URL,
        "serviceName eq 'Virtual Machines Licenses' and priceType eq 'Consumption' and (contains(productName, 'SUSE') or contains(productName, 'Red Hat Enterprise Linux'))"
    )

    final_list = {}

    print("Processing Linux license data from Azure Price API...")
    for item in license_items:
        retailPrice = item['retailPrice']
        unitOfMeasure = item['unitOfMeasure']
        meterName = item['meterName']
        productName = item['productName']
        skuName = item['skuName']

        # Skip free tiers and non-hourly meters
        if retailPrice == 0:
            continue
        if unitOfMeasure != "1 Hour":
            continue
        if "BYOS" in meterName or "-Free" in meterName or "BYOS License" in meterName:
            continue

        # Determine OS family
        if "SUSE" in productName:
            osFamily = "SUSE"
        elif "Red Hat Enterprise Linux" in productName:
            osFamily = "RHEL"
        else:
            continue

        # Extract tier key
        if osFamily == "SUSE":
            tierKey = skuName.replace(" vCPU VM", "").replace(" vCPU", "").strip()
        else:
            # RHEL: extract exact vCPU count from meterName
            match = re.match(r'^(\d+)[\s\-]+vCPU[\s\-]*VM[\s\-]*License$', meterName, re.IGNORECASE)
            if not match:
                continue
            tierKey = match.group(1)

        # Build nested structure, keeping the minimum price for duplicate entries
        if osFamily not in final_list:
            final_list[osFamily] = {}

        if productName not in final_list[osFamily]:
            final_list[osFamily][productName] = {}

        if tierKey not in final_list[osFamily][productName]:
            final_list[osFamily][productName][tierKey] = retailPrice
        else:
            # Keep the minimum price as a conservative savings estimate
            if retailPrice < final_list[osFamily][productName][tierKey]:
                final_list[osFamily][productName][tierKey] = retailPrice

    print("Writing results to file...")

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(final_list, sort_keys=True, indent=2))

    print("DONE!")


if __name__ == "__main__":
    main()
