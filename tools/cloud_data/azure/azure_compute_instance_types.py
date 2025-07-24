import requests
import csv
import json
import os
import re
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from io import StringIO

def remove_duplicates(data):
    seen = set()
    unique_data = []
    for entry in data:
        name = entry.get('name')
        if name not in seen:
            unique_data.append(entry)
            seen.add(name)
    return unique_data

# File names for reading/writing
output_filename = 'data/azure/azure_compute_instance_types.json'
os.makedirs(os.path.dirname(output_filename), exist_ok=True)

# Retrieve environment variables
tenant_id = os.environ.get("AZURE_TENANT_ID")
subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
client_id = os.environ.get("AZURE_CLIENT_ID")
client_secret = os.environ.get("AZURE_CLIENT_SECRET")

print("Gathering data from Azure API...")

# Create a credential using the client secret
credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

# Initialize the ComputeManagementClient with the credentials and subscription ID
compute_client = ComputeManagementClient(credential, subscription_id)

# Make the Resource SKUs - List request and store the results in the variable 'skus'
skus = list(compute_client.resource_skus.list())

# Convert the SKUs to a list of dictionaries
sku_dicts = [sku.as_dict() for sku in skus]

print(f"Retrieved {len(sku_dicts)} instance types.")

# Retrieve the instance size flexibility ratio table from Azure
isf_url = 'https://aka.ms/isf'
def create_instance_size_flexibility_ratio_table(url):
    isf_table = {}
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        csv_content = StringIO(response.text)
        reader = csv.DictReader(csv_content)

        for row in reader:
            key = row['ArmSkuName']
            value = row['Ratio']
            isf_table[key] = float(value)

        return isf_table

    except Exception as e:
        print(f"Error creating instance size flexibility table: {e}")
        return {}

isf_table = create_instance_size_flexibility_table(isf_url)
if isf_table:
    print(f"Retrieved instance size flexibility table for {len(isf_table)} instance types.")

with open("./data/azure/instance_types.json", 'r') as f:
    manual_data = json.load(f)

data = []

for item in sku_dicts:
    if item.get("name", "None") != "None" and item.get("tier", "None") != "None":
        # Extract the relevant fields from the SKU
        details = {
            "name": item.get("name", "None"),
            "tier": item.get("tier", "None"),
            "size": item.get("size", "None"),
            "family": item.get("family", "None"),
            "superseded": "None",
            "specs": { "nfu": isf_table.get(item.get("name"), "None") }
        }

        for capability in item.get("capabilities", []):
            details["specs"][capability.get("name")] = capability.get("value", "None")

        if details["name"] in manual_data and "superseded" in manual_data[details["name"]]:
            details["superseded"] = manual_data[details["name"]]["superseded"]

        if details["name"] in manual_data and "nfu" in manual_data[details["name"]]:
            details["specs"]["nfu"] = manual_data[details["name"]]["nfu"]

        data.append(details)

print("Writing final output to file...")

with open(output_filename, "w") as type_file:
    type_file.write(
        json.dumps(remove_duplicates(data), sort_keys=False, indent=2)
            .replace(': ""', ': null')
            .replace(': "none"', ': null')
            .replace(': "None"', ': null')
            .replace(': "true"', ': true')
            .replace(': "True"', ': true')
            .replace(': "false"', ': false')
            .replace(': "False"', ': false')
    )

print("DONE!")
