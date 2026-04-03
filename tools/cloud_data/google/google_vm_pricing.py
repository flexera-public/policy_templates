#!/usr/bin/env python3
"""
Retrieves Google Cloud Compute Engine VM pricing from the Cloud Billing Catalog API
and computes approximate per-hour list prices for each machine type in us-central1-a.

Cost formula: (vCPUs * vCPU_price) + (memory_GB * memory_price)

Produces: data/google/google_vm_pricing.json
Usage: python3 google_vm_pricing.py
  (Run from the root of the policy_templates repository.)

Requires Google Application Default Credentials to be configured.
"""

import os
import json
import google.auth
from google.cloud import billing_v1
from google.cloud import compute_v1

OUTPUT_FILENAME = "data/google/google_vm_pricing.json"


def money_to_float(money):
    """Converts a Money protobuf object to a Python float."""
    return money.units + money.nanos / 1e9


def get_component_prices(billing_client):
    """Retrieve vCPU and Memory list prices in a single pass through the SKU catalog."""
    service_name = "services/6F81-5844-456A"  # Compute Engine service ID
    vcpu_price = vcpu_sku = mem_price = mem_sku = None
    for sku in billing_client.list_skus(parent=service_name):
        if sku.category.usage_type != "OnDemand":
            continue
        if not sku.pricing_info or not sku.pricing_info[0].pricing_expression.tiered_rates:
            continue
        desc_lower = sku.description.lower()
        rate = sku.pricing_info[0].pricing_expression.tiered_rates[0]
        price = money_to_float(rate.unit_price)
        if vcpu_price is None and "vcpu" in desc_lower:
            vcpu_price = price
            vcpu_sku = sku.name
        elif mem_price is None and "memory" in desc_lower:
            mem_price = price
            mem_sku = sku.name
        if vcpu_price is not None and mem_price is not None:
            break  # Both found — no need to continue iterating
    return vcpu_price, vcpu_sku, mem_price, mem_sku


def list_machine_types(project, zone):
    """
    Retrieves machine types in the given project and zone.
    Returns a list of dictionaries with machine type details.
    """
    machine_client = compute_v1.MachineTypesClient()
    machine_types = machine_client.list(project=project, zone=zone)
    result = []
    for machine in machine_types:
        result.append({
            "name": machine.name,
            "vcpus": machine.guest_cpus,
            "memory_gb": machine.memory_mb / 1024.0
        })
    return result


def main():
    # Initialize the Cloud Billing Catalog client
    billing_client = billing_v1.CloudCatalogClient()

    # Retrieve pricing information for vCPU and Memory in a single SKU pass
    vcpu_price, vcpu_sku, mem_price, mem_sku = get_component_prices(billing_client)

    if vcpu_price is None or mem_price is None:
        print("Could not retrieve pricing for vCPU and/or Memory.")
        return

    # Derive the GCP project from application default credentials
    credentials, project = google.auth.default()

    zone = "us-central1-a"

    # Retrieve machine types from Compute Engine
    machine_types = list_machine_types(project, zone)
    if not machine_types:
        print("No machine types found for the specified zone.")
        return

    # Build dictionary where key is machine type and value is its approximate cost per hour
    pricing_dict = {}
    for machine in machine_types:
        name = machine["name"]
        vcpus = machine["vcpus"]
        memory_gb = machine["memory_gb"]
        cost = (vcpus * vcpu_price) + (memory_gb * mem_price)
        pricing_dict[name] = round(cost, 4)  # rounded to 4 decimal places

    # Define file path and ensure the directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)

    # Write the pricing dictionary to the JSON file with nice formatting
    with open(OUTPUT_FILENAME, "w") as json_file:
        json.dump(pricing_dict, json_file, indent=2)

    print(f"Pricing information saved to {OUTPUT_FILENAME}")


if __name__ == "__main__":
    main()
