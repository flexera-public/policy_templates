import requests
import json
import xmltodict
import os
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest


def remove_duplicates(data):
    """Remove duplicate instance types based on name."""
    seen = set()
    unique_data = []
    for entry in data:
        name = entry.get('name')
        if name not in seen:
            unique_data.append(entry)
            seen.add(name)
    return unique_data


def ensure_list(item):
    """Convert single dict items to list for consistent processing."""
    if isinstance(item, dict):
        return [item]
    return item if item else []


def safe_int(value):
    """Safely convert value to int, return None if conversion fails."""
    try:
        return int(value) if value is not None else None
    except (ValueError, TypeError):
        return None


def safe_float(value):
    """Safely convert value to float, return None if conversion fails."""
    try:
        return float(value) if value is not None else None
    except (ValueError, TypeError):
        return None


def fetch_instance_types(region='us-east-1', max_retries=3):
    """Fetch all EC2 instance types from AWS API with pagination."""
    session = boto3.Session()
    credentials = session.get_credentials()
    auth = SigV4Auth(credentials, 'ec2', region)
    
    base_url = f'https://ec2.{region}.amazonaws.com'
    base_params = {
        "Action": "DescribeInstanceTypes",
        "Version": "2016-11-15"
    }
    
    instance_list = []
    next_token = None
    
    while True:
        params = base_params.copy()
        if next_token:
            params["NextToken"] = next_token
        
        request = AWSRequest(method="GET", url=base_url, params=params)
        auth.add_auth(request)
        
        # Retry logic
        response = None
        for attempt in range(max_retries):
            response = requests.get(base_url, headers=dict(request.headers), params=params)
            if response.status_code == 200:
                break
            print(f"Attempt {attempt+1}/{max_retries} failed with status {response.status_code}. Retrying...")
        
        if response.status_code != 200:
            print(f"Failed after {max_retries} attempts. Exiting pagination loop.")
            break
        
        response_dict = xmltodict.parse(response.content)
        resp_data = response_dict.get("DescribeInstanceTypesResponse", {})
        items = resp_data.get("instanceTypeSet", {}).get("item", [])
        instance_list.extend(ensure_list(items))
        
        next_token = resp_data.get("nextToken")
        if not next_token:
            break
    
    return instance_list


def extract_cpu_info(item, nfu_table):
    """Extract CPU information from instance type data."""
    cpu = {
        "cores": safe_int(item.get("vCpuInfo", {}).get("defaultCores")),
        "vcpus": safe_int(item.get("vCpuInfo", {}).get("defaultVCpus")),
        "nfus": None,
        "manufacturer": item.get("processorInfo", {}).get("manufacturer"),
        "architectures": None,
        "clockSpeedInGhz": None
    }
    
    # Calculate NFUs based on instance size
    parts = item["instanceType"].split('.')
    if len(parts) > 1:
        size = parts[1]
        cpu["nfus"] = nfu_table.get(size)
    
    # Extract architecture information
    proc_info = item.get("processorInfo", {})
    if "supportedArchitectures" in proc_info:
        arch = proc_info["supportedArchitectures"].get("item")
        cpu["architectures"] = [arch] if isinstance(arch, str) else arch
    
    # Extract clock speed
    if "sustainedClockSpeedInGhz" in proc_info:
        cpu["clockSpeedInGhz"] = safe_float(proc_info["sustainedClockSpeedInGhz"])
    
    return cpu


def extract_gpu_info(item):
    """Extract GPU information from instance type data."""
    gpu_info = item.get("gpuInfo")
    if not gpu_info:
        return None
    
    gpu_data = {
        "totalGpuMemoryInMiB": safe_int(gpu_info.get("totalGpuMemoryInMiB")),
        "gpus": []
    }
    
    gpus = gpu_info.get("gpus", {}).get("item", [])
    for gpu in ensure_list(gpus):
        gpu_entry = {
            "name": gpu.get("name"),
            "manufacturer": gpu.get("manufacturer"),
            "count": safe_int(gpu.get("count")),
            "memoryInMiB": safe_int(gpu.get("memoryInfo", {}).get("sizeInMiB"))
        }
        gpu_data["gpus"].append(gpu_entry)
    
    return gpu_data if gpu_data["gpus"] else None


def extract_memory_info(item):
    """Extract memory information from instance type data."""
    return {
        "sizeInMiB": safe_int(item.get("memoryInfo", {}).get("sizeInMiB"))
    }


def extract_network_info(item):
    """Extract network information from instance type data."""
    network = {
        "baselineBandwidthInGbps": None,
        "peakBandwidthInGbps": None,
        "maximumNetworkInterfaces": None
    }
    
    network_cards = item.get("networkInfo", {}).get("networkCards", {}).get("item", [])
    cards_list = ensure_list(network_cards)
    
    if cards_list:
        first_card = cards_list[0]
        network["baselineBandwidthInGbps"] = safe_float(first_card.get("baselineBandwidthInGbps"))
        network["peakBandwidthInGbps"] = safe_float(first_card.get("peakBandwidthInGbps"))
        network["maximumNetworkInterfaces"] = safe_int(first_card.get("maximumNetworkInterfaces"))
    
    return network


def extract_storage_info(item):
    """Extract storage information from instance type data."""
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
        "maximumEbsAttachments": safe_int(item.get("ebsInfo", {}).get("maximumEbsAttachments"))
    }
    
    ebs_info = item.get("ebsInfo", {}).get("ebsOptimizedInfo", {})
    if ebs_info:
        storage["baseline"]["bandwidthInMbps"] = safe_float(ebs_info.get("baselineBandwidthInMbps"))
        storage["baseline"]["iops"] = safe_int(ebs_info.get("baselineIops"))
        storage["baseline"]["throughputInMBps"] = safe_float(ebs_info.get("baselineThroughputInMBps"))
        storage["maximum"]["bandwidthInMbps"] = safe_float(ebs_info.get("maximumBandwidthInMbps"))
        storage["maximum"]["iops"] = safe_int(ebs_info.get("maximumIops"))
        storage["maximum"]["throughputInMBps"] = safe_float(ebs_info.get("maximumThroughputInMBps"))
    
    return storage


def extract_properties(item):
    """Extract instance properties."""
    return {
        "autoRecoverySupported": item.get("autoRecoverySupported"),
        "bareMetal": item.get("bareMetal"),
        "cpuBurstModel": item.get("cpuBurstModel"),
        "currentGeneration": item.get("currentGeneration"),
        "dedicatedHostsSupported": item.get("dedicatedHostsSupported"),
        "freeTierEligible": item.get("freeTierEligible"),
        "hibernationSupported": item.get("hibernationSupported"),
        "hypervisor": item.get("hypervisor"),
        "instanceType": item.get("instanceType"),
        "instanceStorageSupported": item.get("instanceStorageSupported"),
        "phcSupport": item.get("phcSupport") == "supported"
    }


def calculate_size_rank(size):
    """Calculate size rank based on instance size."""
    sizes = {
        "nano": 1, "micro": 2, "small": 4, "medium": 8,
        "large": 16, "xlarge": 32
    }
    # Add computed sizes for 2xlarge through 512xlarge
    for i in range(2, 513):
        sizes[f"{i}xlarge"] = i * 32
    
    return sizes.get(size, "None")


def load_manual_data(filepath='./data/aws/instance_types.json'):
    """Load manual instance type data from JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Manual data file not found at {filepath}")
        return {}


def process_instance_types(instance_list, manual_data, nfu_table):
    """Process raw instance type data into structured format."""
    data = []
    
    for item in instance_list:
        instance_type = item["instanceType"]
        family, size = instance_type.split('.', 1)
        
        entry = {
            "name": instance_type,
            "family": family,
            "size": size,
            "size_rank": calculate_size_rank(size),
            "cpu": extract_cpu_info(item, nfu_table),
            "memory": extract_memory_info(item),
            "network": extract_network_info(item),
            "storage": extract_storage_info(item),
            "properties": extract_properties(item),
            "burst_info": manual_data.get(instance_type, {}).get("burst_info"),
            "superseded": manual_data.get(instance_type, {}).get("superseded"),
            "ec2_classic": manual_data.get(instance_type, {}).get("ec2_classic", "none")
        }
        
        # Add GPU info if available
        gpu_info = extract_gpu_info(item)
        if gpu_info:
            entry["gpu"] = gpu_info
        
        data.append(entry)
    
    return data


def write_json_output(data, filename):
    """Write data to JSON file with proper formatting."""
    with open(filename, "w") as f:
        f.write(
            json.dumps(data, sort_keys=False, indent=2)
                .replace(': ""', ': null')
                .replace(': "none"', ': null')
                .replace(': "None"', ': null')
                .replace(': "true"', ': true')
                .replace(': "True"', ': true')
                .replace(': "false"', ': false')
                .replace(': "False"', ': false')
        )

def main():
    """Main execution function."""
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
    
    # Setup output file
    output_filename = 'data/aws/aws_ec2_instance_types.json'
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    print("Gathering data from AWS API...")
    instance_list = fetch_instance_types()
    print(f"Retrieved {len(instance_list)} instance types.")
    
    print("Loading manual data...")
    manual_data = load_manual_data()
    
    print("Processing instance types...")
    data = process_instance_types(instance_list, manual_data, nfu_table)
    
    print("Removing duplicates...")
    unique_data = remove_duplicates(data)
    
    print("Writing final output to file...")
    write_json_output(unique_data, output_filename)
    
    print("DONE!")


if __name__ == "__main__":
    main()
