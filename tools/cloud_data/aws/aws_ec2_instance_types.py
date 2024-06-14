import requests
import json
import xmltodict
import os
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

region_filename = f'data/aws/regions.json'
output_filename = f'data/aws/aws_ec2_instance_types.json'

with open(region_filename, 'r') as file:
  region_list = json.load(file)

print("Gathering data from AWS API...")

data = {}

# Create a session
region = 'us-east-1'
session = boto3.Session()

# Create a SigV4Auth object
credentials = session.get_credentials()
auth = SigV4Auth(credentials, 'ec2', region)

# Prepare the request
request = AWSRequest(method='GET', url='https://ec2.' + region + '.amazonaws.com?Action=DescribeInstanceTypes&Version=2016-11-15')
auth.add_auth(request)

# Send the request
response = requests.get(request.url, headers=dict(request.headers))

# Check if the request was successful
if response.status_code == 200:
  instance_list = xmltodict.parse(response.content)["DescribeInstanceTypesResponse"]["instanceTypeSet"]["item"]

  for item in instance_list:
    cpu = {
      "cores": item["vCpuInfo"]["defaultCores"],
      "vcpus": item["vCpuInfo"]["defaultVCpus"],
      "manufacturer": item["processorInfo"]["manufacturer"],
      "architecture": None,
      "clockSpeedInGhz": None
    }

    if "processorInfo" in item:
      if "supportedArchitectures" in item["processorInfo"]:
        cpu["architecture"] = item["processorInfo"]["supportedArchitectures"]["item"]

      if "sustainedClockSpeedInGhz" in item["processorInfo"]:
        cpu["clockSpeedInGhz"] = item["processorInfo"]["sustainedClockSpeedInGhz"]

    memory = {
      "sizeInMiB": item["memoryInfo"]["sizeInMiB"]
    }

    network = {
      "baselineBandwidthInGbps": None,
      "peakBandwidthInGbps": None,
      "maximumNetworkInterfaces": None
    }

    if "networkInfo" in item:
      if "networkCards" in item["networkInfo"]:
        networkCards = item["networkInfo"]["networkCards"]["item"]

        if isinstance(networkCards, dict):
          network["baselineBandwidthInGbps"] = networkCards["baselineBandwidthInGbps"]
          network["peakBandwidthInGbps"] = networkCards["peakBandwidthInGbps"]

          if "maximumNetworkInterfaces" in networkCards:
            network["maximumNetworkInterfaces"] = networkCards["maximumNetworkInterfaces"]

        if isinstance(networkCards, list):
          network["baselineBandwidthInGbps"] = networkCards[0]["baselineBandwidthInGbps"]
          network["peakBandwidthInGbps"] = networkCards[0]["peakBandwidthInGbps"]

          if "maximumNetworkInterfaces" in networkCards[0]:
            network["maximumNetworkInterfaces"] = networkCards[0]["maximumNetworkInterfaces"]

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
      "maximumEbsAttachments": item["ebsInfo"]["maximumEbsAttachments"]
    }

    if "ebsInfo" in item:
      if "ebsOptimizedInfo" in item["ebsInfo"]:
        storage["baseline"]["bandwidthInMbps"] = item["ebsInfo"]["ebsOptimizedInfo"]["baselineBandwidthInMbps"]
        storage["baseline"]["iops"] = item["ebsInfo"]["ebsOptimizedInfo"]["baselineIops"]
        storage["baseline"]["throughputInMBps"] = item["ebsInfo"]["ebsOptimizedInfo"]["baselineThroughputInMBps"]
        storage["maximum"]["bandwidthInMbps"] = item["ebsInfo"]["ebsOptimizedInfo"]["maximumBandwidthInMbps"]
        storage["maximum"]["iops"] = item["ebsInfo"]["ebsOptimizedInfo"]["maximumIops"]
        storage["maximum"]["throughputInMBps"] = item["ebsInfo"]["ebsOptimizedInfo"]["maximumThroughputInMBps"]

    properties = {
      "autoRecoverySupported": item["autoRecoverySupported"],
      "bareMetal": item["bareMetal"],
      "cpuBurstModel": item["cpuBurstModel"],
      "currentGeneration": item["currentGeneration"],
      "dedicatedHostsSupported": item["dedicatedHostsSupported"],
      "freeTierEligible": item["freeTierEligible"],
      "hibernationSupported": item["hibernationSupported"],
      "hypervisor": None,
      "instanceType": item["instanceType"],
      "instanceStorageSupported": item["instanceStorageSupported"],
      "phcSupport": False
    }

    if "hypervisor" in item:
      properties["hypervisor"] = item["hypervisor"]

    if item["phcSupport"] == "supported":
      properties["phcSupport"] = True

    data[item["instanceType"]] = {
      "cpu": cpu,
      "memory": memory,
      "network": network,
      "storage": storage,
      "properties": properties
    }

print("Writing final output to file...")

type_file = open(output_filename, "w")
type_file.write(json.dumps(data, sort_keys=False, indent=2).replace(': "none",', ': null,').replace(': "true",', ': true,').replace(': "false",', ': false,'))
type_file.close()

print("DONE!")
