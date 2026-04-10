#!/usr/bin/env python3
"""
Downloads and processes RDS on-demand pricing data from the AWS Price List API.

Produces: data/aws/aws_rds_pricing.json
Usage: python3 aws_rds_pricing.py
  (Run from the root of the policy_templates repository.)

Note: Requires ~10 GB of free disk space for the temporary raw price file.
"""

import json
import urllib.request
import os
import time

PRICING_URL = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/index.json"
OUTPUT_FILENAME = "data/aws/aws_rds_pricing.json"
RAW_FILENAME = "aws_rds_pricing_raw.json"


def download_with_retry(url, dest, max_retries=3, backoff=5):
    """Download a file from url to dest with exponential backoff on failure."""
    for attempt in range(max_retries):
        try:
            urllib.request.urlretrieve(url, dest)
            return
        except Exception as e:
            if attempt < max_retries - 1:
                wait = backoff * (2 ** attempt)
                print(f"Download attempt {attempt + 1} failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise


def main():
    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)

    print("Gathering data from AWS Price API...")
    download_with_retry(PRICING_URL, RAW_FILENAME)

    with open(RAW_FILENAME) as file:
        raw_data = json.load(file)

    raw_data_products = raw_data["products"]
    raw_data_terms = raw_data["terms"]["OnDemand"]
    del raw_data

    print("Processing data from AWS Price API output...")

    starting_list = []

    for key in raw_data_products:
        if "instanceType" in raw_data_products[key]["attributes"] and "regionCode" in raw_data_products[key]["attributes"]:
            instanceType = raw_data_products[key]["attributes"]["instanceType"]
            regionCode = raw_data_products[key]["attributes"]["regionCode"]
            databaseEngine = raw_data_products[key]["attributes"]["databaseEngine"]
            deploymentOption = raw_data_products[key]["attributes"]["deploymentOption"]
            sku = raw_data_products[key]["sku"]

            prices = []

            if key in raw_data_terms:
                for pricing_key in raw_data_terms[key]:
                    offerTermCode = raw_data_terms[key][pricing_key]["offerTermCode"]
                    priceDimensions = []

                    for dimension_key in raw_data_terms[key][pricing_key]["priceDimensions"]:
                        dim = raw_data_terms[key][pricing_key]["priceDimensions"][dimension_key]
                        priceDimensions.append({
                            "rateCode": dim["rateCode"],
                            "pricePerUnit": dim["pricePerUnit"]["USD"]
                        })

                    prices.append({
                        "offerTermCode": offerTermCode,
                        "priceDimensions": priceDimensions
                    })

                starting_list.append({
                    "instanceType": instanceType,
                    "regionCode": regionCode,
                    "sku": sku,
                    "databaseEngine": databaseEngine,
                    "deploymentOption": deploymentOption,
                    "prices": prices
                })

    final_list = {}

    for item in starting_list:
        instanceType = item["instanceType"]
        regionCode = item["regionCode"]
        sku = item["sku"]
        databaseEngine = item["databaseEngine"]
        deploymentOption = item["deploymentOption"]
        pricePerUnit = -1

        if regionCode == "":
            regionCode = "None"

        # Find the highest positive price across all dimensions
        for price in item["prices"]:
            for dimension in price["priceDimensions"]:
                if float(dimension["pricePerUnit"]) > pricePerUnit and float(dimension["pricePerUnit"]) > 0:
                    pricePerUnit = float(dimension["pricePerUnit"])

        if not regionCode in final_list:
            final_list[regionCode] = {}

        if not instanceType in final_list[regionCode]:
            final_list[regionCode][instanceType] = {}

        if not databaseEngine in final_list[regionCode][instanceType]:
            final_list[regionCode][instanceType][databaseEngine] = {}

        if pricePerUnit != -1:
            final_list[regionCode][instanceType][databaseEngine][deploymentOption] = {
                "sku": sku,
                "pricePerUnit": pricePerUnit
            }

    print("Writing final output to file...")

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(final_list, sort_keys=True, indent=2))

    print("Cleaning up temporary files...")
    os.remove(RAW_FILENAME)

    print("DONE!")


if __name__ == "__main__":
    main()
