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
data["instanceTypes"] = {}

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
    data["instanceTypes"][item["instanceType"]] = item

print("Writing final output to file...")

type_file = open(output_filename, "w")
type_file.write(json.dumps(data, sort_keys=False, indent=2).replace(': "true",', ': true,').replace(': "false",', ': false,'))
type_file.close()

print("DONE!")
