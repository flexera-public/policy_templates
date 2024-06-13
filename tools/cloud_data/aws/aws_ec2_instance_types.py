import requests
import json
import xmltodict
import os
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

def calculate_normalized_units(instance_type_info):
  vcpus = instance_type_info['VCpuInfo']['DefaultVCpus']
  memory = instance_type_info['MemoryInfo']['SizeInMiB']
  # Example multipliers for CPU and Memory
  cpu_multiplier = 1
  memory_multiplier = 0.1
  normalized_units = (vcpus * cpu_multiplier) + (memory * memory_multiplier)
  return normalized_units

output_filename = f'data/aws/aws_ec2_instance_types.json'

print("Gathering data from AWS API...")

data = {}

# Create a session
session = boto3.Session()

# Create a SigV4Auth object
credentials = session.get_credentials()
auth = SigV4Auth(credentials, 'ec2', 'us-east-1')

# Prepare the request
request = AWSRequest(method='GET', url='https://ec2.us-east-1.amazonaws.com?Action=DescribeInstanceTypes&Version=2016-11-15', params={'Action': 'DescribeInstanceTypes', 'Version': '2016-11-15'})
auth.add_auth(request)

# Send the request
response = requests.get(request.url, headers=dict(request.headers))

# Check if the request was successful
if response.status_code == 200:
  instance_list = xmltodict.parse(response.content)["DescribeInstanceTypesResponse"]["instanceTypeSet"]["item"]

  for item in instance_list:
    data[item["instanceType"]] = item

print("Writing final output to file...")

type_file = open(output_filename, "w")
type_file.write(json.dumps(data, sort_keys=False, indent=2))
type_file.close()

print("DONE!")
