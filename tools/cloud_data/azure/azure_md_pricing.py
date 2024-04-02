#!/usr/bin/env python3

# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Create a new local branch of the repository.
#   (3) Run this Python script. It should replace azure_md_pricing.json with a new updated file.
#       Note: Working directory should be the *root* directory of the repository.
#   (4) Add and commit the new file, push it to the repository, and then make a pull request.

import json
import logging
import urllib.parse
import urllib.request
from collections import OrderedDict

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

OUTPUT_FILENAME = "data/azure/azure_md_pricing.json"
# Below commented regions are presumed to support Premium SSDv2 but the pricing page does not
# return pricing for those regions, that is why I comment them.
PREMIUM_SSD_V2_SUPPORTED_REGIONS = [
    "australiaeast",
    "brazilsouth",
    "canadacentral",
    "centralindia",
    "centralus",
    "eastasia",
    "eastus",
    "eastus2",
    # "eastus2euap",
    "francecentral",
    "germanywestcentral",
    # "israelcentral",
    "japaneast",
    "koreacentral",
    "northeurope",
    "norwayeast",
    "polandcentral",
    "southafricanorth",
    "southcentralus",
    # "southcentralusstg",
    "southeastasia",
    "swedencentral",
    "switzerlandnorth",
    "uaenorth",
    "uksouth",
    "westeurope",
    "westus2",
    "westus3",
]


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
        "$filter": "(productName eq 'Standard HDD Managed Disks' or productName eq 'Standard SSD Managed Disks' or productName eq 'Premium SSD Managed Disks' or productName eq 'Azure Premium SSD v2' or productName eq 'Ultra Disks') and priceType eq 'Consumption' and ((endsWith(meterName, 'Disk') or productName eq 'Azure Premium SSD v2') or (startsWith(meterName, 'Ultra') or productName eq 'Ultra Disks'))",
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
        if (
            item["skuName"] == "Premium LRS"
            and region not in PREMIUM_SSD_V2_SUPPORTED_REGIONS
        ):
            continue

        disk_type = (
            item["skuName"]
            if item["skuName"] not in ("Premium LRS", "Ultra LRS")
            else item["meterName"].replace("(", "").replace(")", "").upper()
        )
        if not region in region_price_map:
            region_price_map[region] = OrderedDict()

        region_price_map[region][disk_type.replace(" ", "_")] = {
            "currencyCode": item["currencyCode"],
            "sku": item["skuName"],
            "pricePerUnit": item["retailPrice"],
            "unitOfMeasure": item["unitOfMeasure"],
            "productName": item["productName"],
        }

    def sort_by_tier(disk_type):
        if "PROVISIONED" in disk_type:
            return disk_type
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
