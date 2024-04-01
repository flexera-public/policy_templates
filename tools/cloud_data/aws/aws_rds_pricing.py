# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Run this Python script. It should replace aws_rds_pricing.json with a new updated file.
#       Note: Working directory should be the *root* directory of the repository.
#   (3) Add and commit the new file, push it to the repository, and then make a pull request.
#
# Note: It is recommended that you have at least 10 GB of free disk space to run this script.
#       This is for temporary storage of the price file from Amazon.

import json
import urllib.request
import os

raw_filename = "aws_rds_pricing_raw.json"
output_filename = "data/aws/aws_rds_pricing.json"
url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonRDS/current/index.json"

print("Gathering data from AWS Price API...")

urllib.request.urlretrieve(url, raw_filename)

with open(raw_filename) as file:
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
          rateCode = raw_data_terms[key][pricing_key]["priceDimensions"][dimension_key]["rateCode"]
          pricePerUnit = raw_data_terms[key][pricing_key]["priceDimensions"][dimension_key]["pricePerUnit"]["USD"]

          dimension_object = {
            "rateCode": rateCode,
            "pricePerUnit": pricePerUnit
          }

          priceDimensions.append(dimension_object)

        price_object = {
          "offerTermCode": offerTermCode,
          "priceDimensions": priceDimensions
        }

        prices.append(price_object)

      item_object = {
        "instanceType": instanceType,
        "regionCode": regionCode,
        "sku": sku,
        "databaseEngine": databaseEngine,
        "deploymentOption": deploymentOption,
        "prices": prices
      }

      starting_list.append(item_object)

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

price_file = open(output_filename, "w")
price_file.write(json.dumps(final_list, sort_keys=True, indent=2))
price_file.close()

print("Cleaning up temporary files...")

os.remove(raw_filename)

print("DONE!")
