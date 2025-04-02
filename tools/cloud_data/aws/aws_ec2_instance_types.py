import requests
import json
import xmltodict
import os
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

# File names for reading/writing
output_filename = 'data/aws/aws_ec2_instance_types.json'
os.makedirs(os.path.dirname(output_filename), exist_ok=True)

# NFU table for calculating NFUs
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/apply_ri.html
nfu_table = {
    "nano": 0.25,
    "micro": 0.5,
    "small": 1,
    "medium": 2,
    "large": 4,
    "xlarge": 8,
    "2xlarge": 16,
    "3xlarge": 24,
    "4xlarge": 32,
    "6xlarge": 48,
    "8xlarge": 64,
    "9xlarge": 72,
    "10xlarge": 80,
    "12xlarge": 96,
    "16xlarge": 128,
    "18xlarge": 144,
    "24xlarge": 192,
    "32xlarge": 256,
    "56xlarge": 448,
    "112xlarge": 896
}

print("Gathering data from AWS API...")

data = {}

# AWS region and session setup
region = 'us-east-1'
session = boto3.Session()
credentials = session.get_credentials()  # If using temporary credentials, consider freezing them.
auth = SigV4Auth(credentials, 'ec2', region)

# Base URL and query parameters
base_url = f'https://ec2.{region}.amazonaws.com'
base_params = {
    "Action": "DescribeInstanceTypes",
    "Version": "2016-11-15"
}

instance_list = []
next_token = None

while True:
    # Build request parameters; add NextToken if available
    params = base_params.copy()
    if next_token:
        params["NextToken"] = next_token

    # Create and sign the AWS request
    request = AWSRequest(method="GET", url=base_url, params=params)
    auth.add_auth(request)

    # Retry logic: try up to 3 times for each request
    max_attempts = 3
    for attempt in range(max_attempts):
        response = requests.get(base_url, headers=dict(request.headers), params=params)
        if response.status_code == 200:
            break
        else:
            print(f"Attempt {attempt+1}/{max_attempts} failed with status code {response.status_code}. Retrying...")
    if response.status_code != 200:
        print(f"Failed after {max_attempts} attempts. Exiting pagination loop.")
        break

    # Parse the XML response into a dictionary
    response_dict = xmltodict.parse(response.content)
    resp_data = response_dict.get("DescribeInstanceTypesResponse", {})
    items = resp_data.get("instanceTypeSet", {}).get("item", [])
    if isinstance(items, dict):
        items = [items]
    instance_list.extend(items)

    # Check for NextToken to determine if there are more pages
    next_token = resp_data.get("nextToken")
    if not next_token:
        break

print(f"Retrieved {len(instance_list)} instance types.")

# Process each instance item and build the final data dictionary
for item in instance_list:
    cpu = {
        "cores": int(item["vCpuInfo"]["defaultCores"]),
        "vcpus": int(item["vCpuInfo"]["defaultVCpus"]),
        "nfus": None,
        "manufacturer": item["processorInfo"]["manufacturer"],
        "architectures": None,
        "clockSpeedInGhz": None
    }

    # Extract the instance size from the instanceType string (e.g., "t2.micro")
    parts = item["instanceType"].split('.')
    if len(parts) > 1:
        size = parts[1]
        if size in nfu_table:
            cpu["nfus"] = nfu_table[size]

    if "processorInfo" in item:
        proc_info = item["processorInfo"]
        if "supportedArchitectures" in proc_info:
            arch = proc_info["supportedArchitectures"]["item"]
            if isinstance(arch, str):
                cpu["architectures"] = [arch]
            else:
                cpu["architectures"] = arch

        if "sustainedClockSpeedInGhz" in proc_info:
            cpu["clockSpeedInGhz"] = float(proc_info["sustainedClockSpeedInGhz"])

    memory = {
        "sizeInMiB": int(item["memoryInfo"]["sizeInMiB"])
    }

    network = {
        "baselineBandwidthInGbps": None,
        "peakBandwidthInGbps": None,
        "maximumNetworkInterfaces": None
    }

    if "networkInfo" in item and "networkCards" in item["networkInfo"]:
        networkCards = item["networkInfo"]["networkCards"]["item"]
        if isinstance(networkCards, dict):
            network["baselineBandwidthInGbps"] = float(networkCards["baselineBandwidthInGbps"])
            network["peakBandwidthInGbps"] = float(networkCards["peakBandwidthInGbps"])
            if "maximumNetworkInterfaces" in networkCards:
                network["maximumNetworkInterfaces"] = int(networkCards["maximumNetworkInterfaces"])
        elif isinstance(networkCards, list):
            first_card = networkCards[0]
            network["baselineBandwidthInGbps"] = float(first_card["baselineBandwidthInGbps"])
            network["peakBandwidthInGbps"] = float(first_card["peakBandwidthInGbps"])
            if "maximumNetworkInterfaces" in first_card:
                network["maximumNetworkInterfaces"] = int(first_card["maximumNetworkInterfaces"])

    storage = {
        "baseline": {
            "bandwidthInMbps": None,
            "iops": None,
            "throughputInMBps": None
        },
        "maximum": {
            "bandwidthInMbps": None,
            "iops": None,
            "throughputInMBps": None
        },
        "maximumEbsAttachments": int(item["ebsInfo"]["maximumEbsAttachments"])
    }

    if "ebsInfo" in item and "ebsOptimizedInfo" in item["ebsInfo"]:
        ebs_info = item["ebsInfo"]["ebsOptimizedInfo"]
        storage["baseline"]["bandwidthInMbps"] = float(ebs_info["baselineBandwidthInMbps"])
        storage["baseline"]["iops"] = int(ebs_info["baselineIops"])
        storage["baseline"]["throughputInMBps"] = float(ebs_info["baselineThroughputInMBps"])
        storage["maximum"]["bandwidthInMbps"] = float(ebs_info["maximumBandwidthInMbps"])
        storage["maximum"]["iops"] = int(ebs_info["maximumIops"])
        storage["maximum"]["throughputInMBps"] = float(ebs_info["maximumThroughputInMBps"])

    properties = {
        "autoRecoverySupported": item["autoRecoverySupported"],
        "bareMetal": item["bareMetal"],
        "cpuBurstModel": item["cpuBurstModel"],
        "currentGeneration": item["currentGeneration"],
        "dedicatedHostsSupported": item["dedicatedHostsSupported"],
        "freeTierEligible": item["freeTierEligible"],
        "hibernationSupported": item["hibernationSupported"],
        "hypervisor": item.get("hypervisor"),
        "instanceType": item["instanceType"],
        "instanceStorageSupported": item["instanceStorageSupported"],
        "phcSupport": item["phcSupport"] == "supported"
    }

    data[item["instanceType"]] = {
        "cpu": cpu,
        "memory": memory,
        "network": network,
        "storage": storage,
        "properties": properties
    }

print("Writing final output to file...")

with open(output_filename, "w") as type_file:
    type_file.write(
        json.dumps(data, sort_keys=True, indent=2)
               .replace(': "none",', ': null,')
               .replace(': "true",', ': true,')
               .replace(': "false",', ': false,')
    )

print("DONE!")
