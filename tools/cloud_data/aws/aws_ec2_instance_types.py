import requests
import json
import xmltodict
import os
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

# File names for reading/writing
output_filename = f'data/aws/aws_ec2_instance_types.json'

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
      "cores": int(item["vCpuInfo"]["defaultCores"]),
      "vcpus": int(item["vCpuInfo"]["defaultVCpus"]),
      "nfus": None,
      "manufacturer": item["processorInfo"]["manufacturer"],
      "architectures": None,
      "clockSpeedInGhz": None
    }

    size = item["instanceType"].split('.')[1]

    if size in nfu_table:
      cpu["nfus"] = nfu_table[size]

    if "processorInfo" in item:
      if "supportedArchitectures" in item["processorInfo"]:
        if isinstance(item["processorInfo"]["supportedArchitectures"]["item"], str):
          cpu["architectures"] = [ item["processorInfo"]["supportedArchitectures"]["item"] ]
        else:
          cpu["architectures"] = item["processorInfo"]["supportedArchitectures"]["item"]

      if "sustainedClockSpeedInGhz" in item["processorInfo"]:
        cpu["clockSpeedInGhz"] = float(item["processorInfo"]["sustainedClockSpeedInGhz"])

    memory = {
      "sizeInMiB": int(item["memoryInfo"]["sizeInMiB"])
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
          network["baselineBandwidthInGbps"] = float(networkCards["baselineBandwidthInGbps"])
          network["peakBandwidthInGbps"] = float(networkCards["peakBandwidthInGbps"])

          if "maximumNetworkInterfaces" in networkCards:
            network["maximumNetworkInterfaces"] = int(networkCards["maximumNetworkInterfaces"])

        if isinstance(networkCards, list):
          network["baselineBandwidthInGbps"] = float(networkCards[0]["baselineBandwidthInGbps"])
          network["peakBandwidthInGbps"] = float(networkCards[0]["peakBandwidthInGbps"])

          if "maximumNetworkInterfaces" in networkCards[0]:
            network["maximumNetworkInterfaces"] = int(networkCards[0]["maximumNetworkInterfaces"])

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

    if "ebsInfo" in item:
      if "ebsOptimizedInfo" in item["ebsInfo"]:
        storage["baseline"]["bandwidthInMbps"] = float(item["ebsInfo"]["ebsOptimizedInfo"]["baselineBandwidthInMbps"])
        storage["baseline"]["iops"] = int(item["ebsInfo"]["ebsOptimizedInfo"]["baselineIops"])
        storage["baseline"]["throughputInMBps"] = float(item["ebsInfo"]["ebsOptimizedInfo"]["baselineThroughputInMBps"])
        storage["maximum"]["bandwidthInMbps"] = float(item["ebsInfo"]["ebsOptimizedInfo"]["maximumBandwidthInMbps"])
        storage["maximum"]["iops"] = int(item["ebsInfo"]["ebsOptimizedInfo"]["maximumIops"])
        storage["maximum"]["throughputInMBps"] = float(item["ebsInfo"]["ebsOptimizedInfo"]["maximumThroughputInMBps"])

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
type_file.write(json.dumps(data, sort_keys=True, indent=2).replace(': "none",', ': null,').replace(': "true",', ': true,').replace(': "false",', ': false,'))
type_file.close()

print("DONE!")
