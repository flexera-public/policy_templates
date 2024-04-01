#!/usr/bin/env python3

# Instructions for updating the tier list:
#   (1) Download the flexera-public/policy_templates repository locally.
#   (2) Create a new local branch of the repository.
#   (3) In case there is a new disk type added by Azure, add that disk to the MANAGED_DISK_TIER_MAP.
#   (4) Run this Python script. It should replace managed_disk_tier_types.json with a new updated file.
#       Note: Working directory should be the *root* directory of the repository.
#   (5) Add and commit the new file, push it to the repository, and then make a pull request.

import json

OUTPUT_FILENAME = f'data/azure/azure_md_tier_types.json'

MANAGED_DISK_TIER_MAP = {
    "S4": {
        "sizeGiB": 32,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": -1,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S6": {
        "sizeGiB": 64,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": -1,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S10": {
        "sizeGiB": 128,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": -1,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S15": {
        "sizeGiB": 256,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": -1,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S20": {
        "sizeGiB": 512,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 2,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S30": {
        "sizeGiB": 1024,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S40": {
        "sizeGiB": 2048,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S50": {
        "sizeGiB": 4096,
        "tier": "Standard",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S60": {
        "sizeGiB": 8192,
        "tier": "Standard",
        "IOPS": 1300,
        "throughput": 300,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S70": {
        "sizeGiB": 16384,
        "tier": "Standard",
        "IOPS": 2000,
        "throughput": 500,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "S80": {
        "sizeGiB": 32767,
        "tier": "Standard",
        "IOPS": 2000,
        "throughput": 500,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "E1": {
        "sizeGiB": 4,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E2": {
        "sizeGiB": 8,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E3": {
        "sizeGiB": 16,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E4": {
        "sizeGiB": 32,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E6": {
        "sizeGiB": 64,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E10": {
        "sizeGiB": 128,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E15": {
        "sizeGiB": 256,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E20": {
        "sizeGiB": 512,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 3,
        "maxBurstIOPS": 600,
        "maxBurstThroughput": 150,
    },
    "E30": {
        "sizeGiB": 1024,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 5,
        "maxBurstIOPS": 1000,
        "maxBurstThroughput": 250,
    },
    "E40": {
        "sizeGiB": 2048,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "E50": {
        "sizeGiB": 4096,
        "tier": "StandardSSD",
        "IOPS": 500,
        "throughput": 60,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "E60": {
        "sizeGiB": 8192,
        "tier": "StandardSSD",
        "IOPS": 2000,
        "throughput": 400,
        "maxShares": 10,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "E70": {
        "sizeGiB": 16384,
        "tier": "StandardSSD",
        "IOPS": 4000,
        "throughput": 600,
        "maxShares": 10,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "E80": {
        "sizeGiB": 32767,
        "tier": "StandardSSD",
        "IOPS": 6000,
        "throughput": 750,
        "maxShares": 10,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "P1": {
        "sizeGiB": 4,
        "tier": "Premium",
        "IOPS": 120,
        "throughput": 25,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P2": {
        "sizeGiB": 8,
        "tier": "Premium",
        "IOPS": 120,
        "throughput": 25,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P3": {
        "sizeGiB": 16,
        "tier": "Premium",
        "IOPS": 120,
        "throughput": 25,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P4": {
        "sizeGiB": 32,
        "tier": "Premium",
        "IOPS": 120,
        "throughput": 25,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P6": {
        "sizeGiB": 64,
        "tier": "Premium",
        "IOPS": 240,
        "throughput": 50,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P10": {
        "sizeGiB": 128,
        "tier": "Premium",
        "IOPS": 500,
        "throughput": 100,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P15": {
        "sizeGiB": 256,
        "tier": "Premium",
        "IOPS": 1100,
        "throughput": 125,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P20": {
        "sizeGiB": 512,
        "tier": "Premium",
        "IOPS": 2300,
        "throughput": 150,
        "maxShares": 3,
        "maxBurstIOPS": 3500,
        "maxBurstThroughput": 170,
    },
    "P30": {
        "sizeGiB": 1024,
        "tier": "Premium",
        "IOPS": 5000,
        "throughput": 200,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "P40": {
        "sizeGiB": 2048,
        "tier": "Premium",
        "IOPS": 7500,
        "throughput": 250,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "P50": {
        "sizeGiB": 4096,
        "tier": "Premium",
        "IOPS": 7500,
        "throughput": 250,
        "maxShares": 5,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "P60": {
        "sizeGiB": 8192,
        "tier": "Premium",
        "IOPS": 16000,
        "throughput": 500,
        "maxShares": 10,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "P70": {
        "sizeGiB": 16384,
        "tier": "Premium",
        "IOPS": 18000,
        "throughput": 750,
        "maxShares": 10,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
    "P80": {
        "sizeGiB": 32767,
        "tier": "Premium",
        "IOPS": 20000,
        "throughput": 900,
        "maxShares": 10,
        "maxBurstIOPS": -1,
        "maxBurstThroughput": -1,
    },
}


def dump_to_json_file(filename, content, indent=None):
    with open(filename, "wt", encoding="utf-8") as f:
        json.dump(content, f, indent=indent)


def find_tier_downgrade(disk_tier):
    tier_letter = disk_tier[0]
    tier_number = disk_tier[1:]
    if tier_letter == "S":
        return None
    elif tier_letter == "E":
        return "S4" if tier_number in ("1", "2", "3", "4") else f"S{tier_number}"
    elif tier_letter == "P":
        return f"E{tier_number}"
    else:
        raise ValueError(f"Unknown disk tier: {disk_tier}")


def _find_size_downgrade(disk_tier_letter, disk_size_gib, disk_tier_map):
    downgrade_size = round(disk_size_gib / 2)
    return next(
        (
            disk_name
            for disk_name, disk_data in disk_tier_map.items()
            if disk_name[0] == disk_tier_letter
            and disk_data["sizeGiB"] == downgrade_size
        ),
        None,
    )


def find_size_downgrade(disk_name, disk_size_gib, disk_tier_map):
    tier_letter = disk_name[0]
    tier_number = disk_name[1:]
    if tier_letter == "S":
        if disk_size_gib == 32:
            return None
        return _find_size_downgrade(tier_letter, disk_size_gib, disk_tier_map)
    elif tier_letter in ("E", "P"):
        if disk_size_gib == 4:
            return None
        return _find_size_downgrade(tier_letter, disk_size_gib, disk_tier_map)
    else:
        raise ValueError("Unknown disk tier: " + disk["tier"])


def find_disk_downgrades(disk_name, disk_size_gib, disk_tier_map):
    return {
        "tier": find_tier_downgrade(disk_name),
        "size": find_size_downgrade(disk_name, disk_size_gib, disk_tier_map),
    }


def main():
    for disk_name, disk_data in MANAGED_DISK_TIER_MAP.items():
        disk_data["downgrades"] = find_disk_downgrades(
            disk_name, disk_data["sizeGiB"], MANAGED_DISK_TIER_MAP
        )
    dump_to_json_file(OUTPUT_FILENAME, MANAGED_DISK_TIER_MAP, indent=2)


if __name__ == "__main__":
    main()
