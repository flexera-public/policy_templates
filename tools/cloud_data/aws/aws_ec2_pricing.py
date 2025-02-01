# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Run this Python script. It should replace aws_ec2_pricing.json with a new updated file.
#       Note: Working directory should be the *root* directory of the repository.
#   (3) Add and commit the new file, push it to the repository, and then make a pull request.
#
# Note: It is recommended that you have at least 10 GB of free disk space to run this script.
#       This is for temporary storage of the price file from Amazon.

import json
import urllib.request
import os

raw_filename = f'aws_ec2_pricing_raw.json'
product_filename = f'aws_ec2_pricing_raw_products.json'
terms_filename = f'aws_ec2_pricing_raw_terms.json'
output_filename = f'data/aws/aws_ec2_pricing.json'
url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/index.json"

print("Gathering data from AWS Price API...")

urllib.request.urlretrieve(url, raw_filename)

print("Removing unnecessary data from AWS Price API output...")

# Store filtered file for product list
product_block = 0

with open(product_filename, 'w') as output_file:
  output_file.write("{\n")

  with open(raw_filename, 'r') as source_file:
    for line in source_file:
      if product_block == 0 and '"products"' in line:
        product_block = 1

      if product_block == 1:
        if line.rstrip() == '  },':
          break
        elif line.rstrip() == '    },':
          output_file.write(line)
        elif line.rstrip().startswith('    "'):
          output_file.write(line)
        elif '"sku"' in line.rstrip() or '"instanceType"' in line.rstrip() or '"operatingSystem"' in line.rstrip() or '"preInstalledSw"' in line.rstrip() or '"attributes"' in line.rstrip():
          output_file.write(line)
        elif '"regionCode"' in line.rstrip():
          output_file.write(line.replace(",", ""))
        elif line.strip() == '}' and line.rstrip() != '  }':
          output_file.write(line)

  output_file.write("}\n")

# Store filtered file for terms list
terms_block = 0

with open(terms_filename, 'w') as output_file:
  output_file.write("{\n")

  with open(raw_filename, 'r') as source_file:
    for line in source_file:
      if terms_block == 0 and '"terms"' in line:
        output_file.write(line)

      if terms_block == 0 and '"OnDemand"' in line.split(":")[0]:
        terms_block = 1

      if terms_block == 1:
        if line.rstrip() == '    },':
          break
        else:
          output_file.write(line)

  output_file.write("    }\n")
  output_file.write("  }\n")
  output_file.write("}\n")


with open(product_filename) as file:
  raw_data_products = json.load(file)

with open(terms_filename) as file:
  raw_data_terms = json.load(file)

print("Processing remaining data from AWS Price API output...")

starting_list = []

for key in raw_data_products:
  if "instanceType" in raw_data_products[key]["attributes"] and "regionCode" in raw_data_products[key]["attributes"]:
    instanceType = raw_data_products[key]["attributes"]["instanceType"]
    regionCode = raw_data_products[key]["attributes"]["regionCode"]
    sku = raw_data_products[key]["sku"]
    operatingSystem = raw_data_products[key]["attributes"]["operatingSystem"]
    preInstalledSw = raw_data_products[key]["attributes"]["preInstalledSw"]
    prices = []

    if key in raw_data_terms["terms"]["OnDemand"] and preInstalledSw == "NA":
      for pricing_key in raw_data_terms["terms"]["OnDemand"][key]:
        offerTermCode = raw_data_terms["terms"]["OnDemand"][key][pricing_key]["offerTermCode"]
        priceDimensions = []

        for dimension_key in raw_data_terms["terms"]["OnDemand"][key][pricing_key]["priceDimensions"]:
          rateCode = raw_data_terms["terms"]["OnDemand"][key][pricing_key]["priceDimensions"][dimension_key]["rateCode"]
          pricePerUnit = raw_data_terms["terms"]["OnDemand"][key][pricing_key]["priceDimensions"][dimension_key]["pricePerUnit"]["USD"]

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

print("Writing final output to file...")

price_file = open(output_filename, "w")
price_file.write(json.dumps(final_list, sort_keys=True, indent=2))
price_file.close()

print("Cleaning up temporary files...")

os.remove(raw_filename)
os.remove(product_filename)
os.remove(terms_filename)

print("DONE!")
