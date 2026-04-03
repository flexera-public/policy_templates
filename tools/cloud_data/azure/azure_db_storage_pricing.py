#!/usr/bin/env python3
"""
Fetches Azure SQL Database managed disk storage pricing from the Azure Retail Price API.

Produces: data/azure/azure_db_storage_pricing.json
Usage: python3 azure_db_storage_pricing.py
  (Run from the root of the policy_templates repository.)
"""

import requests
import json

OUTPUT_FILENAME = "data/azure/azure_db_storage_pricing.json"
API_URL = "https://prices.azure.com/api/retail/prices"
QUERY = (
    "unitOfMeasure eq '1 GB/Month' and serviceName eq 'SQL Database' "
    "and type eq 'Consumption' and (skuName eq 'General Purpose' "
    "or skuName eq 'Business Critical' or skuName eq 'Hyperscale')"
)


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
    print("Gathering data from Azure Price API...")
    price_list = fetch_all_prices(API_URL, QUERY)

    final_list = {}

    print("Processing data from Azure Price API...")
    for item in price_list:
        region = item['armRegionName']
        skuName = item['skuName']
        skuId = item['skuId']
        unitPrice = item['unitPrice']
        productName = item['productName']
        meterName = item['meterName']

        # Normalize sku names to match what other Azure APIs return
        if skuName == "Business Critical":
            skuName = "BusinessCritical"

        if skuName == "General Purpose":
            skuName = "GeneralPurpose"

        if "Free" not in meterName and "SingleDB" not in productName and "Storage" in productName and unitPrice != 0.0:
            if region not in final_list:
                final_list[region] = {}

            final_list[region][skuName] = {
                "sku": skuId,
                "unitPrice": unitPrice
            }

    print("Writing results to file...")

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(final_list, sort_keys=True, indent=2))

    print("DONE!")


if __name__ == "__main__":
    main()
