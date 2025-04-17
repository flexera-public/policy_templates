"""
This script retrieves pricing data from Google Cloud's Cloud Billing Catalog API
and lists Compute Engine machine types along with an approximate per-hour list price.
The cost is calculated as:
    cost = (number of vCPUs * vCPU price) + (memory in GB * memory price)

Instead of printing the information to the console, the script collects the data into
a dictionary where each key is the machine type (e.g., 'n4-standard-2') and the value is
the computed cost per hour. The dictionary is then saved as a nicely formatted JSON file at:
    tools/cloud_data/google/google_vm_pricing.json

Prices are specific to the zone us-central1-a
"""

import os
import json
from google.cloud import billing_v1
from google.cloud import compute_v1

def money_to_float(money):
    """Converts a Money object to a float."""
    return money.units + money.nanos / 1e9

def get_pricing_for_component(billing_client, component_keyword):
    """
    Retrieves the list price and the associated SKU for a pricing component (e.g., 'vCPU' or 'Memory').
    It searches the SKU descriptions for the specified keyword.
    """
    service_name = "services/6F81-5844-456A"  # Compute Engine service id
    for sku in billing_client.list_skus(parent=service_name):
        # Consider only on-demand (list price) SKUs.
        if sku.category.usage_type != "OnDemand":
            continue
        # Search the description for the desired component.
        if component_keyword.lower() in sku.description.lower():
            if not sku.pricing_info:
                continue
            pricing_expression = sku.pricing_info[0].pricing_expression
            if not pricing_expression.tiered_rates:
                continue
            # Using the first tiered rate as the list price.
            rate = pricing_expression.tiered_rates[0]
            price = money_to_float(rate.unit_price)
            return price, sku.name  # Return both the unit price and the internal SKU id
    return None, None

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
    # Initialize the Cloud Billing Catalog client.
    billing_client = billing_v1.CloudCatalogClient()

    # Retrieve pricing information for vCPU and Memory.
    vcpu_price, vcpu_sku = get_pricing_for_component(billing_client, "vCPU")
    mem_price, mem_sku = get_pricing_for_component(billing_client, "Memory")

    if vcpu_price is None or mem_price is None:
        print("Could not retrieve pricing for vCPU and/or Memory.")
        return

    # Specify your project and zone.
    project = "sales-engineering-buyer"  # Replace with your actual project id
    zone = "us-central1-a"       # Change if needed

    # Retrieve machine types from Compute Engine.
    machine_types = list_machine_types(project, zone)
    if not machine_types:
        print("No machine types found for the specified zone.")
        return

    # Build dictionary where key is machine type and value is its approximate cost per hour.
    pricing_dict = {}
    for machine in machine_types:
        name = machine["name"]
        vcpus = machine["vcpus"]
        memory_gb = machine["memory_gb"]
        cost = (vcpus * vcpu_price) + (memory_gb * mem_price)
        pricing_dict[name] = round(cost, 4)  # rounded to 4 decimal places

    # Define file path and ensure the directory exists.
    output_path = "data/google/google_vm_pricing.json"
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    # Write the pricing dictionary to the JSON file with nice formatting.
    with open(output_path, "w") as json_file:
        json.dump(pricing_dict, json_file, indent=2)

    print(f"Pricing information saved to {output_path}")

if __name__ == "__main__":
    main()
