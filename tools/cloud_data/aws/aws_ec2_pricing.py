#!/usr/bin/env python3
"""
Downloads and processes EC2 on-demand pricing data from the AWS Price List API.

Produces: data/aws/aws_ec2_pricing.json
Usage: python3 aws_ec2_pricing.py
  (Run from the root of the policy_templates repository.)

Note: Requires ~10 GB of free disk space for the temporary raw price file.
"""

import json
import urllib.request
import os
import time

PRICING_URL = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json"
OUTPUT_FILENAME = "data/aws/aws_ec2_pricing.json"
RAW_FILENAME = "aws_ec2_pricing_raw.json"
PRODUCT_FILENAME = "aws_ec2_pricing_raw_products.json"
TERMS_FILENAME = "aws_ec2_pricing_raw_terms.json"


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


def extract_intermediate_files(raw_filename, product_filename, terms_filename):
    """Parse the raw pricing file in a single pass, writing both intermediate files.

    This avoids reading the 3+ GB raw file twice.  A state machine tracks which
    section of the JSON we are currently in:
      before_products -> in_products -> after_products -> in_terms
    """
    state = "before_products"
    with open(raw_filename, 'r') as source, \
         open(product_filename, 'w') as pf, \
         open(terms_filename, 'w') as tf:

        pf.write("{\n")
        tf.write("{\n")

        for line in source:
            stripped = line.rstrip()

            if state == "before_products":
                if '"products"' in line:
                    state = "in_products"

            elif state == "in_products":
                if stripped == '  },':
                    state = "after_products"
                elif stripped == '    },':
                    pf.write(line)
                elif stripped.startswith('    "'):
                    pf.write(line)
                elif ('"sku"' in stripped or '"instanceType"' in stripped or
                      '"operatingSystem"' in stripped or '"preInstalledSw"' in stripped or
                      '"attributes"' in stripped):
                    pf.write(line)
                elif '"regionCode"' in stripped:
                    # Remove trailing comma so regionCode is valid JSON without a following key
                    pf.write(line.replace(",", ""))
                elif line.strip() == '}' and stripped != '  }':
                    pf.write(line)

            elif state == "after_products":
                if '"terms"' in line:
                    tf.write(line)
                if '"OnDemand"' in line.split(":")[0]:
                    state = "in_terms"
                    # The OnDemand header line is included in the block
                    if stripped != '    },':
                        tf.write(line)
                    else:
                        break

            elif state == "in_terms":
                if stripped == '    },':
                    break
                tf.write(line)

        pf.write("}\n")
        tf.write("    }\n")
        tf.write("  }\n")
        tf.write("}\n")


def build_starting_list(raw_data_products, raw_data_terms):
    """Join product entries with their OnDemand pricing terms."""
    starting_list = []

    for key in raw_data_products:
        if "instanceType" in raw_data_products[key]["attributes"] and "regionCode" in raw_data_products[key]["attributes"]:
            instanceType = raw_data_products[key]["attributes"]["instanceType"]
            regionCode = raw_data_products[key]["attributes"]["regionCode"]
            sku = raw_data_products[key]["sku"]
            operatingSystem = raw_data_products[key]["attributes"]["operatingSystem"]
            preInstalledSw = raw_data_products[key]["attributes"]["preInstalledSw"]
            prices = []

            # Only process entries with no pre-installed software (NA) that have OnDemand terms
            if key in raw_data_terms["terms"]["OnDemand"] and preInstalledSw == "NA":
                for pricing_key in raw_data_terms["terms"]["OnDemand"][key]:
                    offerTermCode = raw_data_terms["terms"]["OnDemand"][key][pricing_key]["offerTermCode"]
                    priceDimensions = []

                    for dimension_key in raw_data_terms["terms"]["OnDemand"][key][pricing_key]["priceDimensions"]:
                        dim = raw_data_terms["terms"]["OnDemand"][key][pricing_key]["priceDimensions"][dimension_key]
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
                    "operatingSystem": operatingSystem,
                    "prices": prices
                })

    return starting_list


def build_final_pricing(starting_list):
    """Aggregate pricing into a nested dict keyed by region, instance type, and OS."""
    final_list = {}

    for item in starting_list:
        instanceType = item["instanceType"]
        regionCode = item["regionCode"]
        sku = item["sku"]
        operatingSystem = item["operatingSystem"]
        pricePerUnit = -1

        # Find the highest positive price across all dimensions
        for price in item["prices"]:
            for dimension in price["priceDimensions"]:
                if float(dimension["pricePerUnit"]) > pricePerUnit and float(dimension["pricePerUnit"]) > 0:
                    pricePerUnit = float(dimension["pricePerUnit"])

        # Always create the nested dicts even when no valid price is found
        if not regionCode in final_list:
            final_list[regionCode] = {}

        if not instanceType in final_list[regionCode]:
            final_list[regionCode][instanceType] = {}

        if pricePerUnit != -1:
            final_list[regionCode][instanceType][operatingSystem] = {
                "sku": sku,
                "pricePerUnit": pricePerUnit
            }

    return final_list


def main():
    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)

    print("Gathering data from AWS Price API...")
    download_with_retry(PRICING_URL, RAW_FILENAME)

    print("Removing unnecessary data from AWS Price API output...")
    extract_intermediate_files(RAW_FILENAME, PRODUCT_FILENAME, TERMS_FILENAME)

    with open(PRODUCT_FILENAME) as file:
        raw_data_products = json.load(file)

    with open(TERMS_FILENAME) as file:
        raw_data_terms = json.load(file)

    print("Processing remaining data from AWS Price API output...")
    starting_list = build_starting_list(raw_data_products, raw_data_terms)
    final_list = build_final_pricing(starting_list)

    print("Writing final output to file...")
    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(final_list, sort_keys=True, indent=2))

    print("Cleaning up temporary files...")
    os.remove(RAW_FILENAME)
    os.remove(PRODUCT_FILENAME)
    os.remove(TERMS_FILENAME)

    print("DONE!")


if __name__ == "__main__":
    main()
