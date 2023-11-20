#!/usr/bin/env python3

import json


MANAGED_DISK_TIER_LIST_FILENAME = "managed_disk_types.json"
MANAGED_DISK_DOWNGRADE_LIST_FILENAME = "managed_disk_tier_types.json"


def load_from_json_file(filename):
    with open(filename, "rt", encoding="utf-8") as f:
        content = json.load(f)
    return content


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


def _find_size_downgrade(disk_tier_letter, disk_size, disk_tier_map):
    downgrade_size = round(disk_size / 2)
    return next((d["tier"] for d in disk_tier_map.values() if d["tier"][0] == disk_tier_letter and d["sizeGiB"] == downgrade_size), None)


def find_size_downgrade(disk, disk_tier_map):
    tier_letter = disk["tier"][0]
    tier_number = disk["tier"][1:]
    if tier_letter == "S":
        disk_size = disk["sizeGiB"]
        if disk_size == 32:
            return None
        return _find_size_downgrade(tier_letter, disk_size, disk_tier_map)
    elif tier_letter in ("E", "P"):
        disk_size = disk["sizeGiB"]
        if disk_size == 4:
            return None
        return _find_size_downgrade(tier_letter, disk_size, disk_tier_map)
    else:
        raise ValueError("Unknown disk tier: " + disk["tier"])


def find_disk_downgrades(disk, disk_tier_map):
    return {
        "tier": find_tier_downgrade(disk["tier"]),
        "size": find_size_downgrade(disk, disk_tier_map),
    }


def main():
    disk_map = load_from_json_file(MANAGED_DISK_TIER_LIST_FILENAME)
    for _, disk in disk_map.items():
        disk["downgrades"] = find_disk_downgrades(disk, disk_map)
    dump_to_json_file(MANAGED_DISK_DOWNGRADE_LIST_FILENAME, disk_map, indent=2)
    

if __name__ == "__main__":
    main()
