import requests
import json
import os
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

# Set your AWS credentials and region
aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_KEY")
output_filename = f'data/aws/aws_instance_types.json'

with open(file_path, 'r') as file:
  region_json = json.load(f'data/aws/regions.json')

regions = [item["region"] for item in region_json]

print("Gathering data from AWS API...")

data = {}

for region in regions:
  data[region] = {}

  # Create a session
  session = boto3.Session(aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region)

  # Create a SigV4Auth object
  credentials = session.get_credentials()
  auth = SigV4Auth(credentials, 'ec2', region)

  # Prepare the request
  request = AWSRequest(method='GET', url='https://ec2.amazonaws.com', params={'Action': 'DescribeInstanceTypes', 'Version': '2016-11-15'})
  auth.add_auth(request)

  # Send the request
  response = requests.get(request.url, headers=dict(request.headers))

  # Check if the request was successful
  if response.status_code == 200:
    instance_types = response.json()["instanceTypeSet"]

    for item in instance_types:
      data[region][item["instanceType"]] = item

print("Writing final output to file...")

type_file = open(output_filename, "w")
type_file.write(json.dumps(data, sort_keys=True, indent=2))
type_file.close()

print("DONE!")
