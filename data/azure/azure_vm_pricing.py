# Instructions for updating the price list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Run this Python script. It should replace azure_vm_pricing.json with a new updated file.
#   (3) Add and commit the new file, push it to the repository, and then make a pull request.

import requests
import json
import os

output_filename = "azure_vm_pricing.json"

api_url = "https://prices.azure.com/api/retail/prices"
query = "serviceName eq 'Virtual Machines' and priceType eq 'Consumption'"
response = requests.get(api_url, params={'$filter': query})
json_data = json.loads(response.text)

price_list = json_data['Items']
nextPage = json_data['NextPageLink']

while(nextPage):
  response = requests.get(nextPage)
  json_data = json.loads(response.text)
  nextPage = json_data['NextPageLink']
  price_list.extend(json_data['Items'])

final_list = {}

for item in price_list:
  region = item['location']
  instanceType = item['armSkuName']
  sku = item['productId']
  pricePerUnit = item['retailPrice']
  operatingSystem = ""

  if "Windows" in item['productName']:
    operatingSystem = "Windows"
<<<<<<< HEAD
  else:
    operatingSystem = "Linux"

  if region != "" and instanceType != "" and operatingSystem != "" and sku != "":
=======

  if "Linux" in item['productName']:
    operatingSystem = "Linux"

  if operatingSystem != "":
>>>>>>> b4b4366650e033b6e3d9c719576937a0d726543d
    if not region in final_list:
      final_list[region] = {}

    if not instanceType in final_list[region]:
      final_list[region][instanceType] = {}

    final_list[region][instanceType][operatingSystem] = {
      "sku": sku,
      "pricePerUnit": pricePerUnit
    }

price_file = open(output_filename, "w")
price_file.write(json.dumps(final_list, sort_keys=True, indent=2))
price_file.close()
