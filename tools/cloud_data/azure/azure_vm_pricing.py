# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Create a new local branch of the repository.
#   (3) Run this Python script. It should replace azure_vm_pricing.json with a new updated file.
#       Note: Working directory should be the *root* directory of the repository.
#   (4) Add and commit the new file, push it to the repository, and then make a pull request.

import requests
import json
import os

print("Gathering Consumption data from Azure Price API...")

output_filename = "data/azure/azure_vm_pricing.json"

api_url = "https://prices.azure.com/api/retail/prices"
query = "serviceName eq 'Virtual Machines' and priceType eq 'Consumption'"
response = requests.get(api_url, params={'$filter': query})
json_data = response.json()

price_list = json_data['Items']
nextPage = json_data['NextPageLink']

while(nextPage):
  response = requests.get(nextPage)
  json_data = response.json()
  nextPage = json_data['NextPageLink']
  price_list.extend(json_data['Items'])

final_list = {}

print("Processing Consumption data from Azure Price API...")

for item in price_list:
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

query = "serviceName eq 'Virtual Machines' and priceType eq 'DevTestConsumption'"
response = requests.get(api_url, params={'$filter': query})
json_data = json.loads(response.text)

price_list = json_data['Items']
nextPage = json_data['NextPageLink']

while(nextPage):
  response = requests.get(nextPage)
  json_data = json.loads(response.text)
  nextPage = json_data['NextPageLink']
  price_list.extend(json_data['Items'])

print("Processing DevTestConsumption (AHUB) data from Azure Price API...")

for item in price_list:
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
      if region in final_list:
        if instanceType in final_list[region]:
          if operatingSystem in final_list[region][instanceType]:
            final_list[region][instanceType][operatingSystem]["pricePerUnitAHUB"] = pricePerUnit

print("Writing results to file...")

price_file = open(output_filename, "w")
price_file.write(json.dumps(final_list, sort_keys=True, indent=2))
price_file.close()

print("DONE!")
