import google.auth
from googleapiclient.discovery import build
import json

def list_all_machine_types():
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

    return machine_types_list

if __name__ == '__main__':
    machine_types = list_all_machine_types()
    print(f"Retrieved {len(machine_types)} machine types.")
    # Optionally, print the detailed metadata in JSON format.
    print(json.dumps(machine_types, indent=2))
