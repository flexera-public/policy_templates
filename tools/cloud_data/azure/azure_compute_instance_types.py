#!/usr/bin/env python3
"""
Fetches Azure Compute VM SKU data from the Azure Management API and merges it
with the instance size flexibility (ISF) ratio table and manual override data.

Produces: data/azure/azure_compute_instance_types.json
Usage: python3 azure_compute_instance_types.py
  (Run from the root of the policy_templates repository.)

Required environment variables:
  AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET
"""

import requests
import csv
import json
import os
import re
import sys
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from io import StringIO

OUTPUT_FILENAME = "data/azure/azure_compute_instance_types.json"
ISF_URL = "https://aka.ms/isf"


def remove_duplicates(data):
    """Remove duplicate instance types based on name, keeping first occurrence."""
    seen = set()
    unique_data = []
    for entry in data:
        name = entry.get('name')
        if name not in seen:
            unique_data.append(entry)
            seen.add(name)
    return unique_data


def create_instance_size_flexibility_ratio_table(url):
    """Fetch the ISF ratio CSV from Azure and return a dict mapping ArmSkuName to Ratio."""
    isf_table = {}
    try:
        response = requests.get(url)
        response.raise_for_status()

        csv_content = StringIO(response.text)
        reader = csv.DictReader(csv_content)

        for row in reader:
            key = row['ArmSkuName']
            value = row['Ratio']
            isf_table[key] = value

        return isf_table

    except Exception as e:
        print(f"Error creating instance size flexibility table: {e}")
        return {}


def main():
    # Validate required environment variables before making any API calls
    tenant_id = os.environ.get("AZURE_TENANT_ID")
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    client_id = os.environ.get("AZURE_CLIENT_ID")
    client_secret = os.environ.get("AZURE_CLIENT_SECRET")

    missing = [
        name for name, val in [
            ("AZURE_TENANT_ID", tenant_id),
            ("AZURE_SUBSCRIPTION_ID", subscription_id),
            ("AZURE_CLIENT_ID", client_id),
            ("AZURE_CLIENT_SECRET", client_secret),
        ] if not val
    ]
    if missing:
        print(f"ERROR: Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)

    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)

    print("Gathering data from Azure API...")

    # Authenticate using client secret credentials
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
    isf_table = create_instance_size_flexibility_ratio_table(ISF_URL)
    if isf_table:
        print(f"Retrieved instance size flexibility table for {len(isf_table)} instance types.")

    with open("./data/azure/instance_types.json", 'r') as f:
        manual_data = json.load(f)

    data = []

    for item in sku_dicts:
        if item.get("resource_type") != "virtualMachines":
            continue

        if item.get("name", "None") != "None" and item.get("tier", "None") != "None":
            # Extract the relevant fields from the SKU
            details = {
                "name": item.get("name", "None"),
                "tier": item.get("tier", "None"),
                "size": item.get("size", "None"),
                "family": item.get("family", "None"),
                "superseded": "None",
                "localDisk": None,
                "specs": { "nfu": isf_table.get(item.get("name"), None) }
            }

            for capability in item.get("capabilities", []):
                details["specs"][capability.get("name")] = capability.get("value", "None")

            # Derive localDisk from MaxResourceVolumeMB: true if > 0, false if == 0, null if absent
            max_resource_volume = details["specs"].get("MaxResourceVolumeMB")
            if max_resource_volume is not None:
                try:
                    details["localDisk"] = int(max_resource_volume) > 0
                except (ValueError, TypeError):
                    details["localDisk"] = None

            if details["name"] in manual_data and "superseded" in manual_data[details["name"]]:
                details["superseded"] = manual_data[details["name"]]["superseded"]

            if details["name"] in manual_data and "nfu" in manual_data[details["name"]]:
                details["specs"]["nfu"] = manual_data[details["name"]]["nfu"]

            data.append(details)

    print("Writing final output to file...")

    with open(OUTPUT_FILENAME, "w") as type_file:
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


if __name__ == "__main__":
    main()
