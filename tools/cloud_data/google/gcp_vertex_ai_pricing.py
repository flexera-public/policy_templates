#!/usr/bin/env python3
"""
Fetches Vertex AI online prediction pricing from the Google Cloud Billing
Catalog API and produces a region → machine_type → price mapping.

Produces: data/gcp/gcp_vertex_ai_pricing.json
Usage: python3 gcp_vertex_ai_pricing.py
  (Run from the root of the policy_templates repository.)

Requires Google Application Default Credentials to be configured:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account.json
See: https://cloud.google.com/docs/authentication/application-default-credentials

Per-machine-type hourly prices are derived by combining per-vCPU and per-GB-RAM
component rates from the Billing Catalog with known machine type specifications.
GPU machine types (a2-highgpu-*) include A100 GPU node costs where available.
Free-tier and $0 SKUs are excluded.
"""

import json
import os

from google.cloud import billing_v1

OUTPUT_FILENAME = "data/gcp/gcp_vertex_ai_pricing.json"

# Vertex AI online prediction supported machine types and their resource specs.
# Source: https://cloud.google.com/vertex-ai/docs/predictions/configure-compute
# gpus: number of A100 GPUs (a2-highgpu-* types only)
MACHINE_TYPE_SPECS = {
    "n1-standard-2":  {"vcpus": 2,  "memory_gb": 7.5},
    "n1-standard-4":  {"vcpus": 4,  "memory_gb": 15.0},
    "n1-standard-8":  {"vcpus": 8,  "memory_gb": 30.0},
    "n1-standard-16": {"vcpus": 16, "memory_gb": 60.0},
    "n1-standard-32": {"vcpus": 32, "memory_gb": 120.0},
    "n1-standard-64": {"vcpus": 64, "memory_gb": 240.0},
    "n1-standard-96": {"vcpus": 96, "memory_gb": 360.0},
    "n1-highmem-2":   {"vcpus": 2,  "memory_gb": 13.0},
    "n1-highmem-4":   {"vcpus": 4,  "memory_gb": 26.0},
    "n1-highmem-8":   {"vcpus": 8,  "memory_gb": 52.0},
    "n1-highmem-16":  {"vcpus": 16, "memory_gb": 104.0},
    "n1-highmem-32":  {"vcpus": 32, "memory_gb": 208.0},
    "n1-highmem-64":  {"vcpus": 64, "memory_gb": 416.0},
    "n1-highmem-96":  {"vcpus": 96, "memory_gb": 624.0},
    "n1-highcpu-2":   {"vcpus": 2,  "memory_gb": 1.8},
    "n1-highcpu-4":   {"vcpus": 4,  "memory_gb": 3.6},
    "n1-highcpu-8":   {"vcpus": 8,  "memory_gb": 7.2},
    "n1-highcpu-16":  {"vcpus": 16, "memory_gb": 14.4},
    "n1-highcpu-32":  {"vcpus": 32, "memory_gb": 28.8},
    "n1-highcpu-64":  {"vcpus": 64, "memory_gb": 57.6},
    "n1-highcpu-96":  {"vcpus": 96, "memory_gb": 86.4},
    "a2-highgpu-1g":  {"vcpus": 12, "memory_gb": 85.0,  "gpus": 1},
    "a2-highgpu-2g":  {"vcpus": 24, "memory_gb": 170.0, "gpus": 2},
    "a2-highgpu-4g":  {"vcpus": 48, "memory_gb": 340.0, "gpus": 4},
    "a2-highgpu-8g":  {"vcpus": 96, "memory_gb": 680.0, "gpus": 8},
}

# Substrings (case-insensitive) that identify non-prediction Vertex AI SKUs to exclude.
EXCLUDE_TERMS = [
    "training", "automl", "batch", "pipeline", "feature store",
    "metadata", "tensorboard", "dataset", "hyperparameter", "nas",
    "experiment", "model monitoring", "custom job", "data labeling", "tuning",
]


def get_sku_price(sku):
    """Extract the USD price per unit from a SKU's first tier (startUsageAmount == 0)."""
    try:
        expr = sku.pricing_info[0].pricing_expression
        for rate in expr.tiered_rates:
            if rate.start_usage_amount == 0:
                up = rate.unit_price
                return float(up.units) + up.nanos / 1e9
    except (IndexError, AttributeError):
        pass
    return 0.0


def make_description(machine_type, vcpus, gpus):
    """Build a human-readable description string for the machine type."""
    parts = machine_type.split("-")
    series = parts[0].upper()
    family_map = {
        "standard": "Standard",
        "highmem": "High Memory",
        "highcpu": "High CPU",
        "highgpu": "High GPU",
    }
    family_label = family_map.get(parts[1], parts[1].capitalize()) if len(parts) > 1 else ""
    if gpus:
        return "Vertex AI online prediction - {} {} - {} GPU".format(series, family_label, gpus)
    return "Vertex AI online prediction - {} {} - {} vCPU".format(series, family_label, vcpus)


def main():
    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)

    print("Gathering data from Google Cloud Billing Catalog API...")

    client = billing_v1.CloudCatalogClient()

    # Find the Vertex AI billing service
    vertex_service_name = None
    for service in client.list_services():
        if "Vertex AI" in service.display_name or "AI Platform" in service.display_name:
            vertex_service_name = service.name
            print(f"  Found service: {service.display_name} ({service.name})")
            break

    if not vertex_service_name:
        raise RuntimeError(
            "Could not find Vertex AI service in the Cloud Billing catalog. "
            "Ensure credentials are valid and have billing catalog read access."
        )

    all_skus = list(client.list_skus(parent=vertex_service_name, currency_code="USD"))
    print(f"  Downloaded {len(all_skus)} SKUs.")

    print("Processing data...")

    vcpu_prices = {}  # {region: price_per_vcpu_hour}
    ram_prices = {}   # {region: price_per_gib_ram_hour}
    gpu_prices = {}   # {region: price_per_a100_gpu_hour}

    for sku in all_skus:
        desc = sku.description.lower()

        # Only include online prediction SKUs
        if "predict" not in desc:
            continue

        # Skip non-online-prediction SKUs
        if any(term in desc for term in EXCLUDE_TERMS):
            continue

        try:
            price = get_sku_price(sku)
        except Exception as e:
            print(f"Warning: could not parse price for SKU '{sku.description}': {e}")
            continue

        if price <= 0:
            continue

        regions = list(sku.service_regions)
        if not regions:
            continue

        # Classify as CPU, RAM, or GPU component based on description keywords
        if "vcpu" in desc or (
            "cpu" in desc
            and "ram" not in desc
            and "memory" not in desc
            and "gpu" not in desc
        ):
            for region in regions:
                vcpu_prices[region] = min(vcpu_prices.get(region, price), price)
        elif "ram" in desc or "memory" in desc:
            for region in regions:
                ram_prices[region] = min(ram_prices.get(region, price), price)
        elif "gpu" in desc or "a100" in desc:
            for region in regions:
                gpu_prices[region] = min(gpu_prices.get(region, price), price)

    if not vcpu_prices:
        print("Warning: No Vertex AI vCPU prediction pricing found. Output may be empty.")
    if not ram_prices:
        print("Warning: No Vertex AI RAM prediction pricing found. Output may be empty.")

    fallback_vcpu = vcpu_prices.get("us-central1", 0)
    fallback_ram = ram_prices.get("us-central1", 0)
    fallback_gpu = gpu_prices.get("us-central1", 0)

    final_output = {}
    all_regions = set(vcpu_prices.keys()) | set(ram_prices.keys())

    for region in sorted(all_regions):
        vcpu_price = vcpu_prices.get(region, fallback_vcpu)
        ram_price = ram_prices.get(region, fallback_ram)
        gpu_price = gpu_prices.get(region, fallback_gpu)

        if vcpu_price == 0 and ram_price == 0:
            continue

        for machine_type, specs in MACHINE_TYPE_SPECS.items():
            vcpus = specs["vcpus"]
            memory_gb = specs["memory_gb"]
            gpus = specs.get("gpus", 0)

            price_per_hour = (vcpus * vcpu_price) + (memory_gb * ram_price)
            if gpus and gpu_price:
                price_per_hour += gpus * gpu_price

            price_per_hour = round(price_per_hour, 4)
            if price_per_hour <= 0:
                continue

            if region not in final_output:
                final_output[region] = {}
            final_output[region][machine_type] = {
                "description": make_description(machine_type, vcpus, gpus),
                "pricePerHour": price_per_hour,
            }

    print("Writing final output to file...")

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(final_output, sort_keys=True, indent=2))

    machine_types_found = set()
    for region_data in final_output.values():
        machine_types_found.update(region_data.keys())
    print(f"Found pricing for {len(final_output)} region(s) and {len(machine_types_found)} machine type(s).")

    print("DONE!")


if __name__ == "__main__":
    main()
