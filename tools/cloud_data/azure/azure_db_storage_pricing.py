# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Create a new local branch of the repository.
#   (3) Run this Python script. It should replace azure_db_storage_pricing.json with a new updated file.
#       Note: Working directory should be the *root* directory of the repository.
#   (4) Add and commit the new file, push it to the repository, and then make a pull request.

import requests
import json
import os

print("Gathering data from Azure Price API...")

output_filename = f'data/azure/azure_db_storage_pricing.json'

api_url = "https://prices.azure.com/api/retail/prices"
query = "unitOfMeasure eq '1 GB/Month' and serviceName eq 'SQL Database' and type eq 'Consumption' and (skuName eq 'General Purpose' or skuName eq 'Business Critical' or skuName eq 'Hyperscale')"
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

print("Processing data from Azure Price API...")

for item in price_list:
  region = item['armRegionName']
  skuName = item['skuName']
  skuId = item['skuId']
  unitPrice = item['unitPrice']
  productName = item['productName']
  meterName = item['meterName']

  # This is so the values match what other Azure APIs return for these sku names
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

price_file = open(output_filename, "w")
price_file.write(json.dumps(final_list, sort_keys=True, indent=2))
price_file.close()

print("DONE!")
