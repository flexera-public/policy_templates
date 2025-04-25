import requests
import json
import os
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient

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
            "specs": {}
        }

        for capability in item.get("capabilities", []):
            details["specs"][capability.get("name")] = capability.get("value", "None")

        if details["name"] in manual_data and "superseded" in manual_data[details["name"]]:
            details["superseded"] = manual_data[details["name"]]["superseded"]

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
