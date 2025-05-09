import os
import json
import google.auth
from googleapiclient.discovery import build

# File names for reading/writing
output_filename = 'data/google/google_compute_instance_types.json'
os.makedirs(os.path.dirname(output_filename), exist_ok=True)

def list_all_machine_types():
    print("Gathering data from Google API...")

    # Get default credentials and project from the environment.
    credentials, project = google.auth.default()

    # Build the Compute Engine API client.
    compute_service = build('compute', 'v1', credentials=credentials)

    # Array to hold the machine types metadata.
    machine_types_list = []

    # Use aggregatedList to retrieve machine types from all zones.
    request = compute_service.machineTypes().aggregatedList(project=project)

    while request is not None:
        response = request.execute()
        items = response.get('items', {})

        # Iterate over all zones in the aggregated response.
        for zone, zone_data in items.items():
            if 'machineTypes' in zone_data:
                machine_types_list.extend(zone_data['machineTypes'])

        # Get the next page of results if available.
        request = compute_service.machineTypes().aggregatedList_next(
            previous_request=request, previous_response=response)

    print(f"Retrieved {len(machine_types_list)} instance types.")

    return machine_types_list

machine_types = list_all_machine_types()

data = {}

for item in machine_types:
    name = item.get("name", "None")
    zone = item.get("zone", "None")

    if len(name.split('-')) > 1:
        family = name.split('-')[0]
        variant = "-".join(name.split('-')[1:])

    else:
        family = name
        variant = "None"

    if name in data:
        if zone != "None" and zone not in data[name]["zones"]:
            data[name]["zones"].append(zone)
    else:
        memoryMb = item.get("memoryMb", "None")
        memoryGb = "None"

        if memoryMb != "None":
            memoryGb = memoryMb / 1024

        maximumPersistentDisksSizeGb = item.get("maximumPersistentDisksSizeGb", "None")

        if maximumPersistentDisksSizeGb != "None":
            maximumPersistentDisksSizeGb = int(maximumPersistentDisksSizeGb)

        data[name] = {
            "name": name,
            "family": family,
            "variant": variant,
            "description": item.get("description", "None"),
            "zones": [ zone ],
            "specs": {
                "guestCpus": item.get("guestCpus", "None"),
                "memoryMb": memoryMb,
                "memoryGb": memoryGb,
                "imageSpaceGb": item.get("imageSpaceGb", "None"),
                "maximumPersistentDisks": item.get("maximumPersistentDisks", "None"),
                "maximumPersistentDisksSizeGb": maximumPersistentDisksSizeGb,
                "isSharedCpu": item.get("isSharedCpu", "None"),
                "architecture": item.get("architecture", "None"),
                "accelerators": item.get("accelerators", "None"),
                "scratchDisks": item.get("scratchDisks", "None")
            }
        }

final_data = list(data.values())

print("Writing final output to file...")

with open(output_filename, "w") as type_file:
    type_file.write(
        json.dumps(final_data, sort_keys=False, indent=2)
            .replace(': ""', ': null')
            .replace(': "none"', ': null')
            .replace(': "None"', ': null')
            .replace(': "true"', ': true')
            .replace(': "True"', ': true')
            .replace(': "false"', ': false')
            .replace(': "False"', ': false')
    )

print("DONE!")
