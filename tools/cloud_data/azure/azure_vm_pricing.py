#!/usr/bin/env python3
"""
Fetches Azure VM on-demand and DevTest (AHUB) retail prices from the Azure Price API.

Produces: data/azure/azure_vm_pricing.json
Usage: python3 azure_vm_pricing.py
  (Run from the root of the policy_templates repository.)
"""

import requests
import json
import os

OUTPUT_FILENAME = "data/azure/azure_vm_pricing.json"
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

    print("Gathering Consumption data from Azure Price API...")
    consumption_items = fetch_all_prices(
        API_URL,
        "serviceName eq 'Virtual Machines' and priceType eq 'Consumption'"
    )

    final_list = {}

    print("Processing Consumption data from Azure Price API...")
    for item in consumption_items:
        region = item['location']
        instanceType = item['armSkuName']
        sku = item['productId']
        pricePerUnit = item['retailPrice']
        productName = item['productName']
        meterName = item['meterName']
        operatingSystem = ""

        if "Windows" in productName:
            operatingSystem = "Windows"
        else:
            operatingSystem = "Linux"

        if region != "" and instanceType != "" and operatingSystem != "" and sku != "":
            if not ("Spot" in meterName or "Low Priority" in meterName or "Expired" in meterName or
                    "Free" in meterName or "Promo" in meterName or "SPECIAL" in meterName):
                if not region in final_list:
                    final_list[region] = {}

                if not instanceType in final_list[region]:
                    final_list[region][instanceType] = {}

                final_list[region][instanceType][operatingSystem] = {
                    "sku": sku,
                    "pricePerUnit": pricePerUnit,
                    "pricePerUnitAHUB": None
                }

    print("Gathering DevTestConsumption (AHUB) data from Azure Price API...")
    dev_test_items = fetch_all_prices(
        API_URL,
        "serviceName eq 'Virtual Machines' and priceType eq 'DevTestConsumption'"
    )

    print("Processing DevTestConsumption (AHUB) data from Azure Price API...")
    for item in dev_test_items:
        region = item['location']
        instanceType = item['armSkuName']
        sku = item['productId']
        pricePerUnit = item['retailPrice']
        productName = item['productName']
        meterName = item['meterName']
        operatingSystem = ""

        if "Windows" in productName:
            operatingSystem = "Windows"
        else:
            operatingSystem = "Linux"

        if region != "" and instanceType != "" and operatingSystem != "" and sku != "":
            if not ("Spot" in meterName or "Low Priority" in meterName or "Expired" in meterName or
                    "Free" in meterName or "Promo" in meterName or "SPECIAL" in meterName):
                # Only update AHUB price if the entry was already created from Consumption data
                if region in final_list:
                    if instanceType in final_list[region]:
                        if operatingSystem in final_list[region][instanceType]:
                            final_list[region][instanceType][operatingSystem]["pricePerUnitAHUB"] = pricePerUnit

    print("Writing results to file...")

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(final_list, sort_keys=True, indent=2))

    print("DONE!")


if __name__ == "__main__":
    main()
