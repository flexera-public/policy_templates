#!/usr/bin/env python3

# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Create a new local branch of the repository.
#   (3) Run this Python script. It should replace azure_md_pricing.json with a new updated file.
#   (4) Add and commit the new file, push it to the repository, and then make a pull request.

import json
import logging
import urllib.parse
import urllib.request
from collections import OrderedDict

logging.basicConfig(level=logging.INFO)

OUTPUT_FILENAME = "azure_md_pricing.json"


def build_url(base_url, params=None):
    return (
        f"{base_url}?{urllib.parse.urlencode(params)}"
        if params is not None
        else base_url
    )


def fetch_json_api(url, timeout=15):
    try:
        response = urllib.request.urlopen(url, timeout=timeout)
        json_data = json.loads(response.read().decode("utf-8"))
        return json_data
    except urllib.error.URLError as e:
        print(f"Error fetching data from {url}: {e}")


def main():
    logging.info("Gathering consumption data for managed disks from Azure Price API...")
    items = []
    base_url = "https://prices.azure.com/api/retail/prices"
    params = {
        "api-version": "2021-10-01-preview",
        "$filter": "(productName eq 'Standard HDD Managed Disks' or productName eq 'Standard SSD Managed Disks' or productName eq 'Premium SSD Managed Disks') and priceType eq 'Consumption' and endsWith(meterName, 'Disk')",
    }
    api_url = build_url(base_url, params)
    while api_url is not None:
        logging.info("Fetching %s...", api_url)
        body = fetch_json_api(api_url)
        items += body["Items"]
        api_url = body["NextPageLink"]

    logging.info(
        "Processing consumption data for managed disks from Azure Price API..."
    )
    region_price_map = OrderedDict()
    for item in items:
        region = item["armRegionName"]
        disk_type = item["skuName"]

        if not region in region_price_map:
            region_price_map[region] = OrderedDict()

        region_price_map[region][disk_type.replace(" ", "_")] = {
            "currencyCode": item["currencyCode"],
            "sku": disk_type,
            "pricePerUnit": item["retailPrice"],
            "unitOfMeasure": item["unitOfMeasure"],
            "productName": item["productName"],
            "armSkuName": item["armSkuName"],
        }

    def sort_by_tier(disk_type):
        tier, rep = disk_type.split("_")
        tier_num = int(tier[1:])
        return tier[0] + "{:02d}".format(tier_num) + "_" + rep

    for region_name in sorted(region_price_map):
        disk_map = region_price_map[region_name]
        for disk_name in sorted(disk_map, key=sort_by_tier):
            disk_map.move_to_end(disk_name)
        region_price_map.move_to_end(region_name)

    logging.info("Writing results to file %s", OUTPUT_FILENAME)
    with open(OUTPUT_FILENAME, "wt", encoding="utf-8") as file:
        json.dump(region_price_map, file, indent=2)

    logging.info("Done!")


if __name__ == "__main__":
    main()
