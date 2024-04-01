# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Run this Python script. It should replace aws_ec2_pricing.json with a new updated file.
#   (3) Add and commit the new file, push it to the repository, and then make a pull request.
#
# Note: It is recommended that you have at least 10 GB of free disk space to run this script.
#       This is for temporary storage of the price file from Amazon.

import json
import urllib.request
import os

raw_filename = "aws_ec2_pricing_raw.json"
output_filename = "data/azure/aws_ec2_pricing.json"
url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json"

urllib.request.urlretrieve(url, raw_filename)

with open(raw_filename) as file:
  raw_data = json.load(file)

starting_list = []

for key in raw_data["products"]:
  if "instanceType" in raw_data["products"][key]["attributes"] and "regionCode" in raw_data["products"][key]["attributes"]:
    instanceType = raw_data["products"][key]["attributes"]["instanceType"]
    regionCode = raw_data["products"][key]["attributes"]["regionCode"]
    sku = raw_data["products"][key]["sku"]
    operatingSystem = raw_data["products"][key]["attributes"]["operatingSystem"]
    preInstalledSw = raw_data["products"][key]["attributes"]["preInstalledSw"]
    prices = []

    if key in raw_data["terms"]["OnDemand"] and preInstalledSw == "NA":
      for pricing_key in raw_data["terms"]["OnDemand"][key]:
        offerTermCode = raw_data["terms"]["OnDemand"][key][pricing_key]["offerTermCode"]
        priceDimensions = []

        for dimension_key in raw_data["terms"]["OnDemand"][key][pricing_key]["priceDimensions"]:
          rateCode = raw_data["terms"]["OnDemand"][key][pricing_key]["priceDimensions"][dimension_key]["rateCode"]
          pricePerUnit = raw_data["terms"]["OnDemand"][key][pricing_key]["priceDimensions"][dimension_key]["pricePerUnit"]["USD"]

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
        "operatingSystem": operatingSystem,
        "prices": prices
      }

      starting_list.append(item_object)

final_list = {}

for item in starting_list:
  instanceType = item["instanceType"]
  regionCode = item["regionCode"]
  sku = item["sku"]
  operatingSystem = item["operatingSystem"]
  pricePerUnit = -1

  for price in item["prices"]:
    for dimension in price["priceDimensions"]:
      if float(dimension["pricePerUnit"]) > pricePerUnit and float(dimension["pricePerUnit"]) > 0:
        pricePerUnit = float(dimension["pricePerUnit"])

  if not regionCode in final_list:
    final_list[regionCode] = {}

  if not instanceType in final_list[regionCode]:
    final_list[regionCode][instanceType] = {}

  if pricePerUnit != -1:
    final_list[regionCode][instanceType][operatingSystem] = {
      "sku": sku,
      "pricePerUnit": pricePerUnit
    }

price_file = open(output_filename, "w")
price_file.write(json.dumps(final_list, sort_keys=True, indent=2))
price_file.close()

os.remove(raw_filename)
