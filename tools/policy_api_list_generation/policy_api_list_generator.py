"""
Extract REST API calls from Flexera Policy Templates.

This script parses Flexera policy template (.pt) files and extracts information about
all REST API calls, including the HTTP method, endpoint URL, target service (AWS, Azure,
GCP, Oracle, Flexera, etc.), fields extracted from the response, and the cloud provider
IAM permission required to make each call.

Usage:
    python policy_api_list_generator.py [--output-dir DIR]

    --output-dir DIR  Write output files to DIR instead of the default
                      data/policy_api_list/ directory. Useful for writing to
                      a temporary location (e.g. /tmp) in CI pipelines.

The script will process all policies listed in data/active_policy_list/active_policy_list.json
and output results to:
    - <output-dir>/policy_api_list.json
    - <output-dir>/policy_api_list.csv
"""

import sys
import re
import csv
import json
import argparse
import urllib.parse
from pathlib import Path


class PolicyTemplateParser:
    """Parser for Flexera Policy Template files."""
    
    # Service patterns to identify which service/cloud the API call targets
    # Order matters - more specific patterns should come first
    SERVICE_PATTERNS = {
        'Turbonomic': [
            r'turbonomic',  # Turbonomic (IBM) instances
            r'^flexera$',  # Turbonomic API with flexera as placeholder host
        ],
        'AWS': [
            r'\.amazonaws\.com',
        ],
        'Azure': [
            r'management\.azure\.com',
            r'management\.chinacloudapi\.cn',
            r'\.azure\.com',
            r'\.azure\.cn',
            r'\.windows\.net',  # Azure Storage (blob, queue, table, file)
            r'monitor\.azure\.',  # Azure Monitor (handles malformed URLs missing .com)
        ],
        'GCP': [
            r'\.googleapis\.com',
        ],
        'Oracle': [
            r'\.oraclecloud\.com',
        ],
        'Flexera': [
            r'api\.flexera\.(com|eu|jp)',
            r'optima\.flexeraeng\.com',
            r'governance\.rightscale\.com',
            r'us-3\.rightscale\.com',
            r'us-4\.rightscale\.com',
            r'api\.rsc\.flexeraeng\.com',
            r'rs_optima_host',  # Flexera built-in variable
            r'rs_governance_host',  # Flexera built-in variable
            r'flexera_api_host',  # Common pattern for Flexera API hosts
            r'flexnetmanager',  # FlexNet Manager
            r'fnms',  # FlexNet Manager Service abbreviation
            r'FlexNet Manager',  # FlexNet Manager full name
            r'api\.app\.',  # Flexera API endpoints (partial domains)
            r'Entire Estate',  # Flexera internal estate references
            r'ComplianceAPIService',  # FlexNet Compliance API
            r'flexeraeng\.com',  # Flexera engineering domain
            r'^false/',  # Placeholder URLs that are actually Flexera internal
            r'^Monthly/',  # Flexera reporting URLs
        ],
        'Spot by NetApp': [
            r'api\.spotinst\.io',
        ],
        'GitHub': [
            r'api\.github\.com',
            r'raw\.githubusercontent\.com',
        ],
        'Okta': [
            r'\.okta\.com',
        ],
        'ServiceNow': [
            r'\.service-now\.com',
        ],
        'Microsoft Graph': [
            r'graph\.microsoft\.com',
        ],
    }

    # Class-level permission lookup table storage (loaded once per run via set_repo_root)
    _aws_service_prefixes_data = None
    _gcp_permission_data = None
    _repo_root = None

    @classmethod
    def set_repo_root(cls, repo_root):
        """Set the repository root path used to locate permission data tables."""
        cls._repo_root = Path(repo_root)

    @classmethod
    def _get_aws_service_prefixes(cls):
        """Lazily load and return the AWS IAM service prefix lookup table."""
        if cls._aws_service_prefixes_data is None:
            cls._aws_service_prefixes_data = {}
            if cls._repo_root:
                data_file = cls._repo_root / 'data' / 'aws' / 'aws_iam_service_prefixes.json'
                if data_file.exists():
                    with open(data_file) as f:
                        cls._aws_service_prefixes_data = json.load(f).get('host_prefix_to_iam_prefix', {})
        return cls._aws_service_prefixes_data

    @classmethod
    def _get_gcp_permission_data_table(cls):
        """Lazily load the full GCP IAM permission data file."""
        if cls._gcp_permission_data is None:
            cls._gcp_permission_data = {}
            if cls._repo_root:
                data_file = cls._repo_root / 'data' / 'google' / 'gcp_iam_permission_service_prefixes.json'
                if data_file.exists():
                    with open(data_file) as f:
                        cls._gcp_permission_data = json.load(f)
        return cls._gcp_permission_data

    @classmethod
    def _get_gcp_service_prefixes(cls):
        """Return the GCP host-prefix-to-IAM-service-prefix mapping."""
        return cls._get_gcp_permission_data_table().get('host_prefix_to_iam_prefix', {})

    @classmethod
    def _get_gcp_resource_abbreviations(cls):
        """Return the GCP API resource abbreviation mapping (e.g., 'b' -> 'buckets')."""
        return cls._get_gcp_permission_data_table().get('resource_abbreviations', {})

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.content = self.file_path.read_text()
        self.policy_name = self._extract_policy_name()
        
    def _extract_policy_name(self):
        """Extract the policy template name from the file."""
        match = re.search(r'^name\s+"([^"]+)"', self.content, re.MULTILINE)
        return match.group(1) if match else self.file_path.stem
    
    def _get_semantic_placeholder(self, var_name):
        """Map a variable name to a semantic placeholder.
        
        Args:
            var_name: Variable name (e.g., 'region', 'account_id', 'subscription')
            
        Returns:
            Semantic placeholder string (e.g., '{region}', '{account}', '{subscription}')
        """
        var_lower = var_name.lower()
        
        # Map common variable names to placeholders
        if 'region' in var_lower or 'homeregion' in var_lower:
            return '{region}'
        elif 'subscription' in var_lower:
            return '{subscription}'
        elif 'account' in var_lower:
            return '{account}'
        elif 'bucket' in var_lower:
            return '{bucket}'
        elif 'org' in var_lower:
            return '{org}'
        elif 'project' in var_lower:
            return '{project}'
        elif 'zone' in var_lower:
            return '{zone}'
        else:
            return '{id}'
    
    def _extract_host_from_param(self, host_pattern):
        """
        Extract actual host from parameter references.
        E.g., $param_azure_endpoint -> management.azure.com
        """
        if not host_pattern or not isinstance(host_pattern, str):
            return None
        
        # Check for parameter reference pattern
        param_match = re.search(r'\$param_(\w+)', host_pattern)
        if param_match:
            param_name = param_match.group(1)
            # Escape special characters in parameter name (should be safe with \w+ but defensive)
            escaped_param_name = re.escape(param_name)
            # Find the parameter definition and extract its default value
            param_pattern = rf'parameter\s+"param_{escaped_param_name}".*?default\s+"([^"]+)"'
            param_def = re.search(param_pattern, self.content, re.DOTALL)
            if param_def:
                return param_def.group(1)
        
        # Check for val() function pattern - e.g., val($ds_flexera_api_hosts, "flexera")
        # These typically resolve to Flexera endpoints - try to extract them
        if 'val(' in host_pattern:
            # Try to extract the datasource name and look up its value
            # For now, return the pattern as-is for further processing
            pass
        
        # For Flexera endpoints, we want to capture them now
        # No need to return None for rs_optima_host or rs_governance_host
        
        return None
    
    def _resolve_parameter_from_content(self, var_name):
        """
        Resolve a variable reference to its default value from parameter definitions.
        E.g., param_azure_endpoint -> management.azure.com
        """
        if not var_name:
            return None
        
        # Escape special regex characters in the variable name
        escaped_var_name = re.escape(var_name)
        
        # Try to match parameter definition
        # Pattern: parameter "var_name" do ... default "value" ... end
        param_pattern = rf'parameter\s+"{escaped_var_name}".*?default\s+"([^"]+)"'
        param_match = re.search(param_pattern, self.content, re.DOTALL)
        
        if param_match:
            return param_match.group(1)
        
        return None
    
    def _determine_api_service(self, host):
        """Determine which service/cloud the API call is targeting based on the host.
        
        Returns:
            str: The service name (e.g., 'AWS', 'Azure', 'Flexera') or 'Unknown' if not recognized.
        """
        if not host:
            return 'Unknown'
        
        for service, patterns in self.SERVICE_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, host, re.IGNORECASE):
                    return service
        
        return 'Unknown'
    
    def _extract_datasources(self):
        """Extract all datasource blocks from the policy template."""
        datasources = []
        lines = self.content.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if this line starts a datasource
            ds_match = re.match(r'datasource\s+"([^"]+)"\s+do\s*$', line)
            if ds_match:
                datasource_name = ds_match.group(1)
                datasource_lines = []
                i += 1
                depth = 1  # Track nesting depth
                
                # Collect lines until we find the matching 'end'
                while i < len(lines) and depth > 0:
                    current_line = lines[i]
                    
                    # Ignore commented lines for depth tracking
                    if not re.match(r'^\s*#', current_line):
                        # Check for nested 'do' statements
                        if re.search(r'\bdo\s*$', current_line):
                            depth += 1
                        # Check for 'end' statements
                        elif re.match(r'^\s*end\s*$', current_line):
                            depth -= 1
                            if depth == 0:
                                break
                    
                    datasource_lines.append(current_line)
                    i += 1
                
                datasources.append({
                    'name': datasource_name,
                    'body': '\n'.join(datasource_lines)
                })
            
            i += 1
        
        return datasources
    
    def _extract_request_info(self, datasource_body):
        """Extract request information from a datasource body."""
        request_info = {
            'has_request': False,
            'method': 'GET',  # Default method
            'host': None,
            'path': None,
            'script_name': None,
            'query_params': {},
            'body_params': {},
            'headers': {}
        }
        
        # Check if datasource has a request block OR uses run_script directly
        has_request_block = 'request do' in datasource_body
        has_direct_script = re.search(r'^\s*run_script\s+\$', datasource_body, re.MULTILINE)
        
        if not has_request_block and not has_direct_script:
            return request_info
        
        request_info['has_request'] = True
        
        # Extract HTTP verb/method
        verb_match = re.search(r'verb\s+"([^"]+)"', datasource_body, re.IGNORECASE)
        if verb_match:
            request_info['method'] = verb_match.group(1).upper()
        
        # Extract host (including join pattern)
        host_match = re.search(r'host\s+join\(\[([^\]]+)\]\)', datasource_body)
        if host_match:
            join_content = host_match.group(1)
            
            try:
                # Extract quoted strings from the join array, but exclude strings inside function calls
                # First, temporarily replace val() calls with placeholders
                temp_content = re.sub(r'val\([^)]+\)', 'VAL_PLACEHOLDER', join_content)
                # Now extract string literals (these are the actual hostname parts)
                host_parts = re.findall(r'["\']([^"\']+)["\']', temp_content)
            except re.error as e:
                # If regex fails, skip this datasource
                return request_info
            
            # Extract variable names from the join array
            # Look for variable patterns: $param_region, val(iter_item, 'region'), etc.
            variables = []
            
            # Extract $param_xxx variables
            param_vars = re.findall(r'\$param_(\w+)', join_content)
            variables.extend(param_vars)
            
            # Extract val(iter_item, 'xxx') patterns
            val_vars = re.findall(r'val\(iter_item,\s*["\']([^"\']+)["\']', join_content)
            variables.extend(val_vars)
            
            # Extract other $variable patterns
            other_vars = re.findall(r'\$(\w+)', join_content)
            variables.extend([v for v in other_vars if not v.startswith('param_')])
            
            has_dynamic = len(variables) > 0 or 'iter_item' in join_content
            
            if has_dynamic:
                # Build host with semantic placeholders based on variable names
                if len(host_parts) > 1:
                    # Multiple parts - join with placeholders between them
                    host_with_vars = ''
                    var_idx = 0
                    for i, part in enumerate(host_parts):
                        host_with_vars += part
                        # Add placeholder between parts (except after last part)
                        if i < len(host_parts) - 1:
                            if var_idx < len(variables):
                                var_name = variables[var_idx]
                                # Map variable name to semantic placeholder
                                placeholder = self._get_semantic_placeholder(var_name)
                                var_idx += 1
                            else:
                                placeholder = '{dynamic}'
                            host_with_vars += placeholder
                    request_info['host'] = host_with_vars
                elif len(host_parts) == 1:
                    # Single part with dynamic variable
                    items = [x.strip() for x in join_content.split(',')]
                    if len(items) > len(host_parts):
                        # Has variables - add placeholders
                        if variables:
                            placeholder = self._get_semantic_placeholder(variables[0])
                        else:
                            placeholder = '{dynamic}'
                            
                        if join_content.startswith('"') or join_content.startswith("'"):
                            # Starts with string: "ec2." + region + ... 
                            request_info['host'] = host_parts[0] + placeholder
                        elif join_content.endswith('"') or join_content.endswith("'"):
                            # Ends with string: ... + region + ".amazonaws.com"
                            request_info['host'] = placeholder + host_parts[0]
                        else:
                            request_info['host'] = placeholder + '.' + host_parts[0]
                    else:
                        request_info['host'] = host_parts[0]
                else:
                    # No string parts found but has dynamic content
                    request_info['host'] = None
            else:
                # Static join - just concatenate
                request_info['host'] = ''.join(host_parts)
        else:
            # Try simple host pattern
            host_match = re.search(r'host\s+["\']([^"\']+)["\']', datasource_body)
            if host_match:
                request_info['host'] = host_match.group(1)
            else:
                # Try val() function pattern - e.g., host val($ds_flexera_api_hosts, "flexera")
                val_match = re.search(r'host\s+val\([^)]+\)', datasource_body)
                if val_match:
                    val_content = val_match.group(0)
                    # Check if it's val(iter_item, ...) - this means dynamic host from iteration
                    if 'iter_item' in val_content:
                        # This is iterating over data from previous datasource
                        # Try to infer the service from auth or other context
                        if 'auth $auth_aws' in datasource_body:
                            # AWS authentication - likely S3 bucket host
                            request_info['host'] = '{bucket}.s3.amazonaws.com'
                        elif 'auth $auth_azure' in datasource_body or 'auth $auth_google' in datasource_body:
                            # Other cloud - use generic placeholder
                            request_info['host'] = '{dynamic_host}'
                        else:
                            # Unknown - use generic placeholder
                            request_info['host'] = '{dynamic_host}'
                    else:
                        # This is a Flexera API call using dynamic host lookup
                        request_info['host'] = 'flexera_api_host'
                else:
                    # Try bare variable pattern (e.g., host rs_optima_host, host rs_governance_host)
                    bare_var_match = re.search(r'host\s+(rs_\w+)', datasource_body)
                    if bare_var_match:
                        request_info['host'] = bare_var_match.group(1)
                    else:
                        # Try parameter reference pattern (e.g., host $param_azure_endpoint)
                        host_param_match = re.search(r'host\s+(\$\w+)', datasource_body)
                        if host_param_match:
                            param_ref = host_param_match.group(1)
                            resolved_host = self._extract_host_from_param(param_ref)
                            if resolved_host:
                                request_info['host'] = resolved_host
        
        # Extract path (including join pattern and simple quotes)
        path_match = re.search(r'path\s+join\(\[([^\]]+)\]\)', datasource_body)
        if path_match:
            try:
                join_content = path_match.group(1)
                
                # Parse the join array to maintain proper order of strings and val() calls
                # Split by comma but be careful with nested function calls
                parts = []
                current_part = ''
                depth = 0
                
                for char in join_content + ',':
                    if char in '([':
                        depth += 1
                        current_part += char
                    elif char in ')]':
                        depth -= 1
                        current_part += char
                    elif char == ',' and depth == 0:
                        part = current_part.strip()
                        if part:
                            parts.append(part)
                        current_part = ''
                    else:
                        current_part += char
                
                # Now process each part to extract strings or val() placeholders
                path_result = ''
                for part in parts:
                    part = part.strip()
                    # Check if it's a val(iter_item, "xxx") call
                    val_match = re.search(r'val\(iter_item,\s*["\']([^"\']+)["\']\)', part)
                    if val_match:
                        path_result += '{' + val_match.group(1) + '}'
                    else:
                        # Check if it's a quoted string
                        string_match = re.search(r'^["\']([^"\']+)["\']$', part)
                        if string_match:
                            path_result += string_match.group(1)
                        elif 'val(' in part:
                            # Other val() patterns (not iter_item) - use generic placeholder
                            path_result += '{dynamic}'
                        # Skip other patterns (variables, etc.)
                
                request_info['path'] = path_result
            except Exception as e:
                # If parsing fails, use placeholder
                request_info['path'] = '/{dynamic}'
        else:
            # Try simple path pattern with single or double quotes
            path_match = re.search(r'path\s+["\']([^"\']+)["\']', datasource_body)
            if path_match:
                request_info['path'] = path_match.group(1)
            else:
                # Check for val() or other dynamic expressions - use placeholder
                path_val_match = re.search(r'path\s+(val\(|iter_item)', datasource_body)
                if path_val_match:
                    request_info['path'] = '/{dynamic}'
                else:
                    request_info['path'] = '/'
        
        # Check for run_script in request
        script_match = re.search(r'run_script\s+\$([^,\s]+)', datasource_body)
        if script_match:
            request_info['script_name'] = script_match.group(1)
        
        # Extract query parameters (with double or single quotes, allow empty values).
        # Values may be string literals ("foo") or runtime expressions (val(...), $var).
        # For non-string values we record '{dynamic}' so the key is still visible for
        # operation derivation (e.g., ?uploadId=... signalling a multipart operation).
        for query_match in re.finditer(r'query\s+["\']([^"\']+)["\']\s*,\s*(?:["\']([^"\']*)["\']|(\S[^,\n]*))', datasource_body):
            param_name = query_match.group(1)
            if query_match.group(2) is not None:
                param_value = query_match.group(2)
            else:
                param_value = '{dynamic}'
            request_info['query_params'][param_name] = param_value
        
        # Extract headers (with double or single quotes)
        for header_match in re.finditer(r'header\s+["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', datasource_body):
            header_name = header_match.group(1)
            header_value = header_match.group(2)
            request_info['headers'][header_name] = header_value
        
        return request_info
    
    def _extract_request_from_script(self, script_name):
        """Extract request information from a JavaScript script block."""
        # Find the script definition
        script_pattern = rf'script\s+"{script_name}".*?do\s+(.*?)\nend'
        script_match = re.search(script_pattern, self.content, re.DOTALL)
        
        if not script_match:
            return None
        
        script_body = script_match.group(1)
        
        # Extract the JavaScript code
        code_pattern = r'code\s+<<-[\'"]?EOS[\'"]?\s+(.*?)EOS'
        code_match = re.search(code_pattern, script_body, re.DOTALL)
        
        if not code_match:
            return None
        
        js_code = code_match.group(1)
        
        request_info = {
            'method': 'GET',
            'host': None,
            'path': None,
            'query_params': {},
            'body_params': {},
            'headers': {}
        }
        
        # Extract verb from JavaScript
        verb_match = re.search(r'verb:\s*["\']([^"\']+)["\']', js_code)
        if verb_match:
            request_info['method'] = verb_match.group(1).upper()
        
        # Extract host from JavaScript
        # Look for the entire host line first
        # Handle array.join() pattern: [ "tagging.", region, ".amazonaws.com" ].join('')
        host_array_join_match = re.search(r'host:\s*\[\s*([^\]]+)\]\s*\.join\([^\)]*\)', js_code)
        if host_array_join_match:
            array_content = host_array_join_match.group(1)
            # Extract string literals
            strings = re.findall(r'["\']([^"\']+)["\']', array_content)
            # Extract variable names  
            variables = re.findall(r'(?:,\s*)(\w+)(?:\s*,|\s*$)', array_content)
            
            if strings:
                # Build host with semantic placeholders
                host_with_vars = ''
                var_idx = 0
                for i, s in enumerate(strings):
                    # Don't strip dots from strings, just use as-is
                    host_with_vars += s
                    # Add placeholder between parts
                    if i < len(strings) - 1:
                        if var_idx < len(variables):
                            placeholder = self._get_semantic_placeholder(variables[var_idx])
                            var_idx += 1
                        else:
                            placeholder = '{dynamic}'
                        host_with_vars += placeholder
                request_info['host'] = host_with_vars
        else:
            # Fall back to simpler patterns
            host_line_match = re.search(r'host:\s*([^,\n]+)', js_code)
            if host_line_match:
                host_line = host_line_match.group(1).strip()
                
                # Check if this is a function call (e.g., get_host_by_region)
                if '(' in host_line and ')' in host_line:
                    # This is a function call - try to trace the function
                    func_match = re.search(r'function\s+(\w+)\s*\([^)]*\)\s*\{([^}]+)\}', js_code, re.DOTALL)
                    if func_match:
                        func_body = func_match.group(2)
                        # Look for return statements with string patterns
                        return_match = re.search(r'return\s+([^;]+)', func_body)
                        if return_match:
                            return_expr = return_match.group(1).strip()
                            # Extract string literals from the return expression
                            strings = re.findall(r'["\']([^"\']+)["\']', return_expr)
                            # Extract variable names
                            variables = re.findall(r'\b(\w+)\s*\+', return_expr)
                            
                            if strings:
                                # Build host with semantic placeholders
                                host_with_vars = ''
                                var_idx = 0
                                for i, s in enumerate(strings):
                                    s_clean = s.lstrip('.')
                                    host_with_vars += s_clean
                                    # Add placeholder between parts
                                    if i < len(strings) - 1:
                                        if var_idx < len(variables):
                                            placeholder = self._get_semantic_placeholder(variables[var_idx])
                                            var_idx += 1
                                        else:
                                            placeholder = '{dynamic}'
                                        host_with_vars += placeholder
                                request_info['host'] = host_with_vars
                            else:
                                # No strings found, use a generic pattern
                                request_info['host'] = '{region}.monitor.azure.com' if 'azure' in func_body.lower() else None
                # Check if this is a concatenated string (contains +)
                elif '+' in host_line:
                    # Extract all string literals from the concatenation
                    strings = re.findall(r'["\']([^"\']+)["\']', host_line)
                    # Extract variable names
                    variables = re.findall(r'\+\s*(\w+)\s*\+', host_line)
                    
                    if strings and len(strings) > 1:
                        # Join them with semantic placeholders between
                        parts = []
                        var_idx = 0
                        for i, s in enumerate(strings):
                            if i == 0:
                                parts.append(s.rstrip('.'))
                            elif i == len(strings) - 1:
                                parts.append(s.lstrip('.'))
                            else:
                                parts.append(s.strip('.'))
                            
                            # Add placeholder between parts (except after last)
                            if i < len(strings) - 1:
                                if var_idx < len(variables):
                                    placeholder = self._get_semantic_placeholder(variables[var_idx])
                                    var_idx += 1
                                else:
                                    placeholder = '{dynamic}'
                                parts.append(placeholder)
                        
                        request_info['host'] = '.'.join(parts)
                    elif strings:
                        request_info['host'] = strings[0]
                else:
                    # Check if it's an object/array access pattern first (e.g., ds_flexera_api_hosts["flexera"])
                    if '[' in host_line and ']' in host_line:
                        # Extract the key being accessed
                        key_match = re.search(r'\["?([^"\]]+)"?\]', host_line)
                        if key_match:
                            key = key_match.group(1)
                            # If accessing with "flexera" key or similar, it's a Flexera API
                            if 'flexera' in key.lower() or 'flexera' in host_line.lower():
                                request_info['host'] = 'flexera_api_host'
                    # Check if it's a simple string literal
                    elif re.search(r'^["\'][^"\']+["\']$', host_line):
                        # Only match if the ENTIRE line is a quoted string
                        host_match = re.search(r'["\']([^"\']+)["\']', host_line)
                        if host_match:
                            request_info['host'] = host_match.group(1)
                    else:
                        # It's a variable reference - check if it's a Flexera built-in
                        var_name = host_line.strip()
                        if var_name in ['rs_optima_host', 'rs_governance_host']:
                            # These are Flexera built-in variables
                            request_info['host'] = var_name
                        else:
                            # Try to resolve it from script parameters or policy file
                            param_resolved = self._resolve_parameter_from_content(var_name)
                            if param_resolved:
                                request_info['host'] = param_resolved
                            else:
                                # Infer service from the parameter name itself when no
                                # default value is available (e.g. param_turbonomic_host).
                                var_lower = var_name.lower()
                                if 'turbonomic' in var_lower:
                                    # Use a host value that matches the Turbonomic service pattern
                                    request_info['host'] = 'turbonomic'
        
        # Extract path from JavaScript - handle both simple strings and array joins
        # Try array join pattern first: [ "/v3/projects/", projectId, "/timeSeries:query" ].join('')
        path_join_match = re.search(r'path:\s*\[\s*([^\]]+)\]\s*\.join\([^\)]*\)', js_code)
        if path_join_match:
            path_parts_str = path_join_match.group(1)
            # Extract string literals from the array
            strings = re.findall(r'["\']([^"\']+)["\']', path_parts_str)
            # Extract variable names from the array
            variables = re.findall(r'(?:,\s*)(\w+)(?:\s*,|\s*\])', path_parts_str)
            
            if strings:
                # Join them but replace variables with placeholders
                # Count commas to determine if there are variables
                parts_count = len(path_parts_str.split(','))
                strings_count = len(strings)
                if parts_count > strings_count:
                    # Has variables - insert semantic placeholders
                    path_with_vars = ''
                    var_idx = 0
                    
                    for i, s in enumerate(strings):
                        path_with_vars += s
                        # Add placeholder for variable between this and next string
                        if i < len(strings) - 1 or not (path_parts_str.strip().endswith('"') or path_parts_str.strip().endswith("'")):
                            # Determine the placeholder based on variable name if available
                            if var_idx < len(variables):
                                var_name = variables[var_idx]
                                # Map common variable names to semantic placeholders
                                if 'org' in var_name.lower():
                                    placeholder = '{org}'
                                elif 'project' in var_name.lower():
                                    placeholder = '{project}'
                                elif 'subscription' in var_name.lower():
                                    placeholder = '{subscription}'
                                elif 'billing' in var_name.lower() or 'bc' in var_name.lower():
                                    placeholder = '{billing_center}'
                                elif 'region' in var_name.lower():
                                    placeholder = '{region}'
                                else:
                                    placeholder = '{id}'
                                var_idx += 1
                            else:
                                placeholder = '{id}'
                            path_with_vars += placeholder
                    
                    request_info['path'] = path_with_vars
                else:
                    request_info['path'] = ''.join(strings)
        else:
            # No array-join: check for concatenation or simple string literal
            path_line_match = re.search(r'path:\s*([^,\n]+)', js_code)
            if path_line_match:
                path_line = path_line_match.group(1).strip()
                if '+' in path_line:
                    # Extract all string literals from the concatenation
                    strings = re.findall(r'["\']([^"\']+)["\']', path_line)
                    # Variables that sit BETWEEN two string parts: "a" + var + "b"
                    mid_vars = re.findall(r'\+\s*(\w+)\s*\+', path_line)

                    if strings:
                        # Check if path starts with a variable (e.g. var + "/sub")
                        path_starts_with_var = not (
                            path_line.startswith('"') or path_line.startswith("'")
                        )
                        # Check if path ends with a variable (e.g. "/sub/" + var)
                        path_ends_with_var = not (
                            path_line.rstrip().endswith('"') or path_line.rstrip().endswith("'")
                        )

                        path_with_vars = ''
                        # Leading variable placeholder
                        if path_starts_with_var:
                            leading_match = re.match(r'(\w+)\s*\+', path_line)
                            if leading_match:
                                path_with_vars += self._get_semantic_placeholder(
                                    leading_match.group(1)
                                )

                        var_idx = 0
                        for i, s in enumerate(strings):
                            path_with_vars += s
                            if i < len(strings) - 1:
                                # Mid variable between two string parts
                                if var_idx < len(mid_vars):
                                    path_with_vars += self._get_semantic_placeholder(mid_vars[var_idx])
                                    var_idx += 1
                                else:
                                    path_with_vars += '{id}'

                        # Trailing variable placeholder
                        if path_ends_with_var:
                            trailing_match = re.search(r'\+\s*(\w+)\s*$', path_line)
                            if trailing_match:
                                path_with_vars += self._get_semantic_placeholder(
                                    trailing_match.group(1)
                                )

                        request_info['path'] = path_with_vars
                else:
                    # Simple string literal
                    path_match = re.search(r'["\']([^"\']+)["\']', path_line)
                    if path_match:
                        request_info['path'] = path_match.group(1)

        
        # Extract query_params object from JavaScript.
        # Key may be quoted ("query_params") or unquoted (query_params).
        # Value may be an inline object { ... } OR a variable name whose definition
        # appears earlier in the same script (e.g. `query_params = { "Action": "..." }`).
        query_params_match = re.search(r'["\']?query_params["\']?\s*:\s*(\{[^}]+\}|[A-Za-z_]\w*)', js_code, re.DOTALL)
        if query_params_match:
            raw_val = query_params_match.group(1).strip()
            if raw_val.startswith('{'):
                params_str = raw_val[1:raw_val.rfind('}')]
            else:
                # Variable reference — look up assignment in same script
                var_name = raw_val
                var_assign = re.search(
                    rf'{re.escape(var_name)}\s*=\s*\{{([^}}]+)\}}', js_code, re.DOTALL
                )
                params_str = var_assign.group(1) if var_assign else None
            if params_str:
                for param_match in re.finditer(r'["\']([^"\']+)["\']\s*:\s*(?:["\']([^"\']*)["\']|(\S[^,\n]*))', params_str):
                    key = param_match.group(1)
                    value = param_match.group(2) if param_match.group(2) is not None else '{dynamic}'
                    request_info['query_params'][key] = value

        # Extract body_fields object from JavaScript
        body_fields_match = re.search(r'body_fields:\s*\{([^}]+)\}', js_code, re.DOTALL)
        if body_fields_match:
            params_str = body_fields_match.group(1)
            # Extract key-value pairs
            param_pattern = r'["\']([^"\']+)["\']'
            keys = re.findall(param_pattern, params_str)
            if keys:
                for key in keys:
                    request_info['body_params'][key] = '{dynamic}'
        
        # Extract body with JSON.stringify
        body_match = re.search(r'body:\s*JSON\.stringify\(\{([^}]+)\}\)', js_code)
        if body_match:
            params_str = body_match.group(1)
            # Extract key-value pairs
            param_pattern = r'["\']([^"\']+)["\']'
            keys = re.findall(param_pattern, params_str)
            if keys:
                for key in keys:
                    request_info['body_params'][key] = '{dynamic}'
        
        # Extract headers from JavaScript (e.g., headers: { "X-Amz-Target": "..." })
        headers_match = re.search(r'headers:\s*\{([^}]+)\}', js_code, re.DOTALL)
        if headers_match:
            headers_str = headers_match.group(1)
            # Extract key-value pairs from headers object
            header_pairs = re.findall(r'["\']([^"\']+)["\']\s*:\s*["\']([^"\']+)["\']', headers_str)
            for key, value in header_pairs:
                request_info['headers'][key] = value
        
        return request_info
    
    def _extract_fields_from_processing_script(self, datasource_body):
        """
        Extract fields that are accessed from the API response in subsequent processing scripts.
        These are fields accessed in scripts that process datasources.
        """
        fields = []
        
        # Look for patterns where the datasource is passed to a run_script after the request
        # This indicates the response is being processed
        # Pattern: datasource "ds_name" do ... end followed by another datasource that processes it
        
        # Find scripts that reference this datasource's output
        # Common patterns:
        # - entry['field_name'] or entry["field_name"]
        # - item['field_name'] or item["field_name"]
        # - result['field_name'] or result["field_name"]
        # - .pluck('field_name')
        
        # Look for JavaScript field access patterns in associated scripts
        script_refs = re.findall(r'run_script\s+\$(\w+)', datasource_body)
        
        for script_ref in script_refs:
            script_fields = self._extract_fields_from_script(script_ref)
            fields.extend(script_fields)
        
        return fields
    
    def _extract_fields_from_script(self, script_name):
        """Extract fields accessed in a JavaScript processing script."""
        fields = []
        
        # Find the script definition
        script_pattern = rf'script\s+"{script_name}".*?do\s+(.*?)\nend'
        script_match = re.search(script_pattern, self.content, re.DOTALL)
        
        if not script_match:
            return fields
        
        script_body = script_match.group(1)
        
        # Extract the JavaScript code
        code_pattern = r'code\s+<<-[\'"]?EOS[\'"]?\s+(.*?)EOS'
        code_match = re.search(code_pattern, script_body, re.DOTALL)
        
        if not code_match:
            return fields
        
        js_code = code_match.group(1)
        
        # Extract field access patterns
        # Patterns like: entry['fieldName'], item["fieldName"], result['fieldName']
        field_patterns = [
            r'(?:entry|item|result|metric|instance|data|col_item|response|obj)\[["\']([^"\']+)["\']\]',
            r'\.pluck\(["\']([^"\']+)["\']\)',
            # Also catch dot notation for nested objects
            r'(?:entry|item|result|metric|instance|data)\.(\w+)',
        ]
        
        seen_fields = set()
        for pattern in field_patterns:
            for match in re.finditer(pattern, js_code):
                field_name = match.group(1)
                # Filter out common programming keywords and loop variables
                if field_name not in ['i', 'j', 'k', 'index', 'length', 'key', 'value', 'each', 'map', 'forEach']:
                    if field_name not in seen_fields:
                        fields.append(field_name)
                        seen_fields.add(field_name)
        
        return fields
    
    def _extract_fields(self, datasource_body):
        """Extract fields from the result block of a datasource."""
        fields = []
        
        # Find result block - need to handle nested do/end
        result_start = datasource_body.find('result do')
        if result_start == -1:
            return fields
        
        # Extract the result block with proper nesting
        lines = datasource_body[result_start:].split('\n')
        result_lines = []
        depth = 0
        started = False
        
        for line in lines:
            if not started and 'result do' in line:
                started = True
                depth = 1
                continue
            
            if started:
                if re.search(r'\bdo\s*$', line):
                    depth += 1
                elif re.match(r'^\s*end\s*$', line):
                    depth -= 1
                    if depth == 0:
                        break
                result_lines.append(line)
        
        result_body = '\n'.join(result_lines)
        
        # Extract field definitions with xpath
        # Pattern: field "fieldName", xpath(col_item, "XPathValue")
        xpath_pattern = r'field\s+"([^"]+)",\s+xpath\([^,]+,\s+"([^"]+)"\)'
        for match in re.finditer(xpath_pattern, result_body):
            field_name = match.group(1)
            xpath_value = match.group(2)
            # Clean up XPath notation - remove leading // and convert paths to field names
            # Examples: 
            #   //LocationConstraint -> LocationConstraint
            #   //PublicAccessBlockConfiguration/BlockPublicAcls -> BlockPublicAcls
            #   //VersioningConfiguration/Status -> Status
            clean_field = xpath_value.lstrip('/')
            # If it's a path with /, take the last segment (the actual field name)
            if '/' in clean_field:
                clean_field = clean_field.split('/')[-1]
            fields.append(clean_field)  # Use the cleaned field name
        
        # Extract field definitions with jmes_path
        # Pattern: field "fieldName", jmes_path(col_item, "jmesPath")
        jmes_pattern = r'field\s+"([^"]+)",\s+jmes_path\([^,]+,\s+"([^"]+)"\)'
        for match in re.finditer(jmes_pattern, result_body):
            field_name = match.group(1)
            jmes_path = match.group(2)
            # Extract the actual field name from jmes_path
            # e.g., "dimensions.vendor_account" -> "vendor_account"
            # e.g., "aws.accountId" -> "accountId"
            # e.g., "values[*]" -> "values"
            # Handle array notation
            if '[' in jmes_path:
                # Extract base field before array notation
                base_field = jmes_path.split('[')[0]
                if base_field:
                    fields.append(base_field)
                else:
                    fields.append(jmes_path)
            else:
                path_parts = jmes_path.split('.')
                if len(path_parts) > 1:
                    api_field = path_parts[-1]
                else:
                    api_field = jmes_path
                fields.append(api_field)
        
        # Extract field definitions with val()
        # Pattern: field "fieldName", val(...)
        # These typically reference iterator or parameter values, not API responses
        # We'll skip these as they're not from the API response
        
        return fields
    
    def _build_endpoint_url(self, request_info):
        """Build the full endpoint URL from request information."""
        if not request_info.get('host'):
            return None
        
        host = request_info['host']
        path = request_info.get('path', '/')
        
        # Wrap policy language constructs in curly braces
        policy_variables = ['rs_optima_host', 'rs_governance_host', 'flexera_api_host', 'rs_org_id', 'rs_project_id']
        for var in policy_variables:
            if var in host:
                host = host.replace(var, f'{{{var}}}')
        
        # Ensure path starts with /
        if not path.startswith('/'):
            path = '/' + path
        
        # Replace empty path segments with placeholders
        # Pattern: /orgs// or /orgs/{dynamic}/ -> /orgs/{org}/
        path = re.sub(r'/orgs/(?:\{dynamic\}|)/(?!$)', '/orgs/{org}/', path)
        path = re.sub(r'/projects/(?:\{dynamic\}|)/(?!$)', '/projects/{project}/', path)
        path = re.sub(r'/billing_centers/(?:\{dynamic\}|)/(?!$)', '/billing_centers/{billing_center}/', path)
        path = re.sub(r'/subscriptions/(?:\{dynamic\}|)/(?!$)', '/subscriptions/{subscription}/', path)
        path = re.sub(r'/resourceGroups/(?:\{dynamic\}|)/(?!$)', '/resourceGroups/{resource_group}/', path)
        
        # Replace generic double slashes with {id}
        path = re.sub(r'//+', '/{id}/', path)
        
        # Clean up multiple slashes that might have been created
        path = re.sub(r'/+', '/', path)
        
        # Build URL
        url = f"https://{host}{path}"
        
        # Add query parameters if any
        if request_info.get('query_params'):
            params = []
            for key, value in request_info['query_params'].items():
                params.append(f"{key}={value}")
            if params:
                url += "?" + "&".join(params)
        
        return url
    
    
    def _get_url_path(self, endpoint):
        """Extract the path portion of a URL, handling various edge cases.
        
        Returns:
            The path portion of the URL (empty string if no path or just '/')
        """
        # Parse URL to get just the path component
        parsed = urllib.parse.urlparse(endpoint)
        path = parsed.path
        
        # Normalize: empty or '/' becomes ''
        if not path or path == '/':
            return ''
        
        # Remove trailing slash
        if path.endswith('/'):
            path = path[:-1]
        
        return path
    
    def _format_resource_name(self, name):
        """Format a resource name to be human-readable.
        
        Converts kebab-case, snake_case, camelCase to Title Case.
        """
        import re
        # Convert camelCase to spaces
        name = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
        # Replace separators with spaces
        name = name.replace('-', ' ').replace('_', ' ')
        # Capitalize each word
        words = name.split()
        return ' '.join(word.capitalize() for word in words)
    
    def _get_generic_operation_from_method(self, method):
        """Get a generic operation name based on HTTP method.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH, etc.)
            
        Returns:
            Generic operation name like 'Get Resource', 'Create Resource', etc.
        """
        method_upper = method.upper()
        if method_upper == 'GET':
            return 'Get Resource'
        elif method_upper == 'POST':
            return 'Create Resource'
        elif method_upper in ('PUT', 'PATCH'):
            return 'Update Resource'
        elif method_upper == 'DELETE':
            return 'Delete Resource'
        else:
            return f'{method_upper} Resource'
    
    def _extract_operation_name(self, endpoint, method, api_service, request_info):
        """Extract a human-readable operation name from the endpoint and request information.
        
        Returns the operation being performed (e.g., 'List VirtualNetworkGateways', 'ListAccounts').
        """
        # Known abbreviations and their expansions for various services
        RESOURCE_MAPPINGS = {
            'GCP': {
                'b': 'Buckets',
                'o': 'Objects',
                'iam': 'IAM Policies',
            },
            'AWS': {
                'acls': 'ACLs',
                'cors': 'CORS',
                'encryption': 'Encryption Configuration',
                'lifecycle': 'Lifecycle Configuration',
                'logging': 'Logging Configuration',
                'tagging': 'Tags',
                'versioning': 'Versioning Configuration',
                'location': 'Location',
                'policy': 'Policy',
            },
            'Oracle': {
                'o': 'Object',
                'b': 'Bucket',
            }
        }
        
        # Placeholder names to skip (these are variable placeholders, not resource names)
        SKIP_PLACEHOLDERS = {
            'name', 'id', 'type', 'value', 'key', 'username', 'account',
            'project', 'subscription', 'resource', 'region', 'zone'
        }
        
        # AWS: Extract from X-Amz-Target header
        if api_service == 'AWS':
            if request_info.get('headers'):
                for key, value in request_info['headers'].items():
                    if key.lower() == 'x-amz-target':
                        # Format: "AWSOrganizationsV20161128.ListAccounts"
                        if '.' in value:
                            operation = value.split('.')[-1]
                            return operation
            
            # Check for Action query parameter (common in AWS Query-style APIs).
            # Only apply when the URL path is "/" or empty — Query-style services
            # (EC2, STS, IAM, …) always use the root path.  REST-style services
            # (Access Analyzer, Lambda, …) use path routing and must not be matched
            # here even if a ?Action= parameter accidentally appears in their URL.
            if '?Action=' in endpoint or '&Action=' in endpoint:
                parsed_aa = urllib.parse.urlparse(endpoint)
                if parsed_aa.path in ('', '/'):
                    params = urllib.parse.parse_qs(parsed_aa.query)
                    if 'Action' in params:
                        action = params['Action'][0]
                        return action
            
            # For AWS S3, check for operations in query parameters.
            # Guard against running S3 path/query logic on non-S3 services
            # (e.g. EC2, CloudWatch) that reach here only because their ?Action=
            # was a dynamic variable that couldn't be resolved.
            parsed_url = urllib.parse.urlparse(endpoint)
            path = parsed_url.path
            is_s3 = self._get_aws_service_prefix_from_host(parsed_url.netloc) == 's3'
            if not is_s3:
                return ''

            # Query params can be in the URL or in request_info
            
            # Combine query params from URL and request_info.  urllib.parse.parse_qs
            # silently drops valueless keys (e.g. "?location" with no "=" sign), but
            # S3 REST APIs use exactly this form for sub-resource operations such as
            # /?location, /?acl, /?logging, /?policy, etc.  Split the raw query string
            # manually so that bare keys are captured as empty-string values.
            params_dict = {}
            if parsed_url.query:
                for component in parsed_url.query.split('&'):
                    if not component:
                        continue
                    if '=' in component:
                        k, v = component.split('=', 1)
                        params_dict[k] = [v]
                    else:
                        params_dict[component] = ['']
            if request_info.get('query_params'):
                # Add query params from request_info (these are single values, not lists)
                for k, v in request_info['query_params'].items():
                    params_dict[k] = [v] if v else ['']
            
            # Check if it's an S3 bucket operation (path contains bucket name or is simple)
            # Common S3 query parameters that indicate operations
            s3_ops = RESOURCE_MAPPINGS.get('AWS', {})
            for param_key in params_dict.keys():
                param_lower = param_key.lower()
                # uploadId identifies multipart upload operations regardless of path depth;
                # the HTTP method distinguishes abort (DELETE) from list-parts (GET).
                if param_lower == 'uploadid':
                    if method.upper() == 'DELETE':
                        return 'Abort Multipart Upload'
                    return 'List Multipart Upload Parts'
                if param_lower in s3_ops:
                    resource = s3_ops[param_lower]
                    m_upper = method.upper()
                    if m_upper in ('PUT', 'POST'):
                        return f'Put Bucket {resource}'
                    elif m_upper == 'DELETE':
                        return f'Delete Bucket {resource}'
                    else:
                        return f'Get Bucket {resource}'
                # Handle special S3 operations
                elif param_lower == 'intelligent-tiering':
                    return 'Get Bucket Intelligent Tiering Configuration'
                # If no mapping, use the parameter name itself (but skip common filters)
                elif param_lower not in ['maxkeys', 'prefix', 'delimiter', 'marker', 'api-version', 'view']:
                    return f'Get Bucket {self._format_resource_name(param_key)}'
            
            # If path is just hostname or '/', and no useful query params
            if not path or path == '/' or path == '/{name}':
                # If no useful query params, it's a bucket list operation
                return 'List Buckets'
            
            # Fallback: Try to infer from URL path
            if path.endswith('/'):
                path = path[:-1]
            
            # Check if it's an S3 object operation (path has multiple segments with placeholders)
            path_segments = [s for s in path.split('/') if s]
            placeholder_count = sum(1 for s in path_segments if '{' in s)
            
            # If path has 2+ placeholders (e.g., /{bucket}/{key}), it's likely an object operation
            if placeholder_count >= 2:
                # Check if there's a query parameter that indicates the operation
                if params_dict:
                    for param_key in params_dict.keys():
                        param_lower = param_key.lower()
                        if param_lower == 'uploadid':
                            # DELETE /{bucket}/{key}?uploadId=... -> AbortMultipartUpload
                            # GET    /{bucket}/{key}?uploadId=... -> ListMultipartUploadParts
                            if method.upper() == 'DELETE':
                                return 'Abort Multipart Upload'
                            return 'List Multipart Upload Parts'
                        elif param_lower not in ['maxkeys', 'prefix', 'delimiter', 'marker', 'api-version', 'view']:
                            return f'Get Object {self._format_resource_name(param_key)}'
                # No query params - infer from HTTP method
                if method.upper() == 'DELETE':
                    return 'Delete Object'
                return 'Get Object'
            
            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Check if it's a known abbreviation
                if resource.lower() in RESOURCE_MAPPINGS.get('AWS', {}):
                    resource = RESOURCE_MAPPINGS['AWS'][resource.lower()]
                    return f'Get {resource}'
                return self._format_operation_from_method(method, resource)
            # Path is all placeholders (e.g. /{bucket}) — infer from method for S3
            if placeholder_count == 1 and method.upper() == 'DELETE':
                return 'Delete Bucket'
        
        # Azure: Extract from URL path
        elif api_service == 'Azure':
            # Parse Azure REST API URLs
            # Format: /subscriptions/{id}/providers/Microsoft.Network/virtualNetworkGateways
            path = self._get_url_path(endpoint)
            
            # Check if it's Azure Storage (blob.core.windows.net, etc.)
            if 'blob.core.windows.net' in endpoint or 'file.core.windows.net' in endpoint or 'queue.core.windows.net' in endpoint or 'table.core.windows.net' in endpoint:
                # Azure Storage APIs use 'restype' and 'comp' parameters
                parsed = urllib.parse.urlparse(endpoint)
                params_dict = {}
                if parsed.query:
                    params_dict.update(urllib.parse.parse_qs(parsed.query))
                if request_info.get('query_params'):
                    for k, v in request_info['query_params'].items():
                        params_dict[k] = [v] if v else ['']
                
                if 'restype' in params_dict:
                    restype = params_dict['restype'][0] if params_dict['restype'] else ''
                    comp = params_dict.get('comp', [''])[0]
                    if comp:
                        return f'List {self._format_resource_name(restype)} {self._format_resource_name(comp)}'
                    return f'List {self._format_resource_name(restype)}'
                
                # Infer from path
                if path:
                    # Path like /{container} for blob storage
                    return f'{method.upper()} Storage'
            
            # Handle fully dynamic or empty paths
            if not path or path == '{dynamic}':
                # Check query parameters for operation hints (both in URL and request_info)
                parsed = urllib.parse.urlparse(endpoint)
                params_dict = {}
                if parsed.query:
                    params_dict.update(urllib.parse.parse_qs(parsed.query))
                if request_info.get('query_params'):
                    for k, v in request_info['query_params'].items():
                        params_dict[k] = [v] if v else ['']
                
                # Azure Storage APIs use 'restype' and 'comp' parameters
                if 'restype' in params_dict:
                    restype = params_dict['restype'][0] if params_dict['restype'] else ''
                    comp = params_dict.get('comp', [''])[0]
                    if comp:
                        return f'List {self._format_resource_name(restype)} {self._format_resource_name(comp)}'
                    return f'List {self._format_resource_name(restype)}'
                
                # No useful info, return generic based on method
                method_upper = method.upper()
                if method_upper == 'GET':
                    return 'List Resources'
                elif method_upper == 'POST':
                    return 'Create Resource'
                elif method_upper in ('PUT', 'PATCH'):
                    return 'Update Resource'
                elif method_upper == 'DELETE':
                    return 'Delete Resource'
                else:
                    return f'{method_upper} Resource'
            
            # Look for provider resources
            if '/providers/' in path:
                # Extract everything after the last provider
                after_provider = path.split('/providers/')[-1]
                segments = after_provider.split('/')
                
                # Find the resource type (skip Microsoft.*, get the actual resource)
                for i, seg in enumerate(segments):
                    if '.' in seg:  # Skip Microsoft.Network, etc.
                        continue
                    if seg and '{' not in seg.lower() and seg.lower() not in SKIP_PLACEHOLDERS:
                        # This is the resource type
                        return self._format_operation_from_method(method, seg)
            
            # Fallback: Use last non-variable segment
            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                return self._format_operation_from_method(method, resource)
        
        # GCP: Extract from URL path
        elif api_service == 'GCP':
            path = self._get_url_path(endpoint)
            
            # Handle fully dynamic or empty paths - use HTTP method as fallback
            if not path or path == '{dynamic}':
                return self._get_generic_operation_from_method(method)
            
            # GCP often uses :operation patterns (e.g., /projects:search)
            if path and ':' in path.split('/')[-1]:  # Check only the last segment
                last_segment = path.split('/')[-1]
                resource, operation = last_segment.split(':', 1)
                # Format: "Search Projects"
                operation_name = operation.title().replace('_', ' ')
                resource_name = resource.title().replace('_', ' ')
                return f'{operation_name} {resource_name}'
            
            segments = [s for s in path.split('/') if s and '{' not in s.lower() and s not in ('v1', 'v2', 'v3')]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Check if it's a known GCP abbreviation
                if resource.lower() in RESOURCE_MAPPINGS.get('GCP', {}):
                    resource = RESOURCE_MAPPINGS['GCP'][resource.lower()]
                    # Already in final form (e.g., 'Buckets'), just add method prefix
                    method_upper = method.upper()
                    if method_upper == 'GET':
                        return f'List {resource}'
                    elif method_upper == 'POST':
                        return f'Create {resource}'
                    elif method_upper in ('PUT', 'PATCH'):
                        return f'Update {resource}'
                    elif method_upper == 'DELETE':
                        return f'Delete {resource}'
                    else:
                        return f'{method_upper} {resource}'
                return self._format_operation_from_method(method, resource)
        
        # Flexera: Extract from URL path
        elif api_service == 'Flexera':
            path = self._get_url_path(endpoint)
            
            # Handle fully dynamic or empty paths - use HTTP method as fallback
            if not path or path == '{dynamic}':
                return self._get_generic_operation_from_method(method)
            
            # Special handling for bill-analysis API
            if '/bill-analysis/' in path and '/costs/' in path:
                # Handle /costs/aggregated and /costs/select patterns
                if '/costs/aggregated' in path:
                    return 'Request Aggregated Costs'
                elif '/costs/select' in path:
                    return 'Request Selected Costs'
            
            segments = [s for s in path.split('/') if s and '{' not in s.lower() and s not in ('v1', 'v2', 'v3')]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Clean up common patterns
                resource = resource.replace('-', ' ').replace('_', ' ')
                return self._format_operation_from_method(method, resource)

        
        # Oracle: Extract from URL path
        elif api_service == 'Oracle':
            path = self._get_url_path(endpoint)
            
            if not path:
                return self._get_generic_operation_from_method(method)
            
            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                # Check if it's a known Oracle abbreviation
                if resource.lower() in RESOURCE_MAPPINGS.get('Oracle', {}):
                    resource = RESOURCE_MAPPINGS['Oracle'][resource.lower()]
                return self._format_operation_from_method(method, resource)
        
        # GitHub: Extract from URL path
        elif api_service == 'GitHub':
            if 'raw.githubusercontent.com' in endpoint:
                return 'Get Raw Content'
            
            path = self._get_url_path(endpoint)
            
            if not path:
                return self._get_generic_operation_from_method(method)
            
            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                return self._format_operation_from_method(method, resource)
        
        # Default: Extract from URL path
        else:
            path = self._get_url_path(endpoint)
            
            if not path:
                return self._get_generic_operation_from_method(method)
            
            segments = [s for s in path.split('/') if s and '{' not in s.lower()]
            # Filter out placeholder segments
            segments = [s for s in segments if s.lower() not in SKIP_PLACEHOLDERS]
            if segments:
                resource = segments[-1]
                return self._format_operation_from_method(method, resource)
        
        # Ultimate fallback - use HTTP method to provide generic operation
        return self._get_generic_operation_from_method(method)
    
    def _format_operation_from_method(self, method, resource):
        """Format an operation name from HTTP method and resource type.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            resource: Resource name from URL
            
        Returns:
            Formatted operation name
        """
        # Clean up resource name - handle camelCase, snake_case, and kebab-case
        # Convert camelCase to spaces: virtualNetworkGateways -> virtual Network Gateways
        import re
        # Insert space before capital letters (except at start)
        resource = re.sub(r'([a-z])([A-Z])', r'\1 \2', resource)
        
        # Replace separators with spaces
        resource = resource.replace('-', ' ').replace('_', ' ')
        
        # Capitalize each word
        resource_words = resource.split()
        resource = ' '.join(word.capitalize() for word in resource_words)
        
        # Map method to operation prefix
        method = method.upper()
        if method == 'GET':
            # If plural, use List, otherwise use Get
            if resource.endswith('s') and len(resource) > 1:
                return f'List {resource}'
            else:
                return f'Get {resource}'
        elif method == 'POST':
            return f'Create {resource}'
        elif method == 'PUT':
            return f'Update {resource}'
        elif method == 'PATCH':
            return f'Update {resource}'
        elif method == 'DELETE':
            return f'Delete {resource}'
        else:
            return f'{method} {resource}'

    def _derive_permission(self, endpoint, method, api_service, request_info, operation):
        """Derive the cloud provider IAM permission required to make this API call.

        Returns the permission string (e.g., 'ec2:DescribeInstances',
        'Microsoft.Compute/virtualMachines/read', 'compute.regions.list'),
        or an empty string if the permission cannot be determined or is not
        applicable for the given service.
        """
        if not endpoint:
            return ''
        if api_service == 'AWS':
            return self._derive_aws_permission(endpoint, method, request_info, operation)
        elif api_service == 'Azure':
            return self._derive_azure_permission(endpoint, method)
        elif api_service == 'GCP':
            return self._derive_gcp_permission(endpoint, method)
        return ''

    def _derive_aws_permission(self, endpoint, method, request_info, operation):
        """Derive the AWS IAM permission string (e.g., 'ec2:DescribeInstances')."""
        host = urllib.parse.urlparse(endpoint).netloc
        service_prefix = self._get_aws_service_prefix_from_host(host)
        if not service_prefix:
            return ''
        # API Gateway execute-api endpoints are custom APIs (e.g. Flexera's own),
        # not AWS service APIs that have predictable IAM permissions.
        if service_prefix == 'execute-api':
            return ''
        # REST-based AWS services that use path routing instead of ?Action=
        path = urllib.parse.urlparse(endpoint).path
        rest_perm = self._derive_aws_rest_permission(service_prefix, path, method)
        if rest_perm:
            return rest_perm
        action = self._get_aws_action_name(endpoint, request_info, operation, service_prefix)
        if not action:
            return ''
        return f'{service_prefix}:{action}'

    def _derive_aws_rest_permission(self, service_prefix, path, method):
        """Derive IAM permission for AWS REST-style APIs (path-based routing).

        These services use HTTP path + verb instead of ?Action= query strings.
        Path placeholders like {name}, {arn}, {dynamic} are normalised to '*'
        before matching so patterns stay readable.
        """
        if not path or path in ('/', ''):
            return ''
        # Normalise all {…} placeholders to '*' for pattern matching.
        path_norm = re.sub(r'\{[^}]*\}', '*', path).rstrip('/')
        m = method.upper()

        # Savings Plans — path IS the action name (e.g. /DescribeSavingsPlans)
        if service_prefix == 'savingsplans':
            action = path.strip('/')
            if action and action[0].isupper() and re.match(r'^[A-Za-z]+$', action):
                return f'savingsplans:{action}'

        # Amazon EKS REST API
        if service_prefix == 'eks':
            EKS = {
                ('/clusters',                       'GET'):    'eks:ListClusters',
                ('/clusters/*',                     'GET'):    'eks:DescribeCluster',
                ('/clusters/*',                     'DELETE'): 'eks:DeleteCluster',
                ('/clusters/*/node-groups',         'GET'):    'eks:ListNodegroups',
                ('/clusters/*/node-groups/*',       'GET'):    'eks:DescribeNodegroup',
                ('/clusters/*/node-groups/*',       'POST'):   'eks:UpdateNodegroupConfig',
                ('/clusters/*/node-groups/*',       'DELETE'): 'eks:DeleteNodegroup',
            }
            return EKS.get((path_norm, m), '')

        # AWS Access Analyzer REST API
        if service_prefix == 'access-analyzer':
            AA = {
                ('/analyzer',        'GET'):    'access-analyzer:ListAnalyzers',
                ('/analyzer/*',      'GET'):    'access-analyzer:GetAnalyzer',
                ('/analyzer/*',      'DELETE'): 'access-analyzer:DeleteAnalyzer',
                ('/analyzer/*/finding', 'GET'): 'access-analyzer:ListFindings',
                ('/analyzer/*/finding/*', 'GET'): 'access-analyzer:GetFinding',
                ('/analyzer/*/archive-rule', 'GET'): 'access-analyzer:ListArchiveRules',
            }
            return AA.get((path_norm, m), '')

        # AWS Lambda REST API
        if service_prefix == 'lambda':
            # Strip version prefix /20YY-MM-DD/
            path_no_ver = re.sub(r'^/20\d\d-\d\d-\d\d', '', path_norm)
            LAMBDA = {
                ('/functions',                           'GET'):    'lambda:ListFunctions',
                ('/functions/*',                         'GET'):    'lambda:GetFunction',
                ('/functions/*',                         'DELETE'): 'lambda:DeleteFunction',
                ('/functions/*/versions',                'GET'):    'lambda:ListVersionsByFunction',
                ('/functions/*/provisioned-concurrency', 'GET'):    'lambda:GetProvisionedConcurrencyConfig',
                ('/functions/*/provisioned-concurrency', 'PUT'):    'lambda:PutProvisionedConcurrencyConfig',
                ('/functions/*/provisioned-concurrency', 'DELETE'): 'lambda:DeleteProvisionedConcurrencyConfig',
                ('/tags/*',                              'GET'):    'lambda:ListTags',
                ('/tags/*',                              'POST'):   'lambda:TagResource',
                ('/tags/*',                              'DELETE'): 'lambda:UntagResource',
            }
            return LAMBDA.get((path_no_ver, m), '')

        return ''

    def _get_aws_service_prefix_from_host(self, host):
        """Map an AWS API hostname to its IAM service action prefix."""
        prefixes = self._get_aws_service_prefixes()
        if not host:
            return ''
        # API Gateway execute-api endpoints
        if 'execute-api' in host:
            return 'execute-api'
        # Strip port if present
        if ':' in host and not host.startswith('{'):
            host = host.split(':')[0]
        if not (host.endswith('.amazonaws.com') or '.amazonaws.com' in host):
            return ''
        # Isolate the subdomain portion before .amazonaws.com
        host_inner = re.sub(r'\.amazonaws\.com.*$', '', host)
        parts = host_inner.split('.')
        # {bucket}.s3 or {id}.s3 -> s3
        if len(parts) >= 2 and parts[-1] == 's3':
            return prefixes.get('s3', 's3')
        # s3.{region} -> s3
        if len(parts) >= 2 and parts[0] == 's3':
            return prefixes.get('s3', 's3')
        # General case: first segment is the service name
        service = parts[0].strip('{}')
        return prefixes.get(service, service)

    def _get_aws_action_name(self, endpoint, request_info, operation, service_prefix):
        """Extract the AWS IAM action name for this API call."""
        # X-Amz-Target header (JSON/query API style: Organizations, DynamoDB, etc.)
        if request_info.get('headers'):
            for key, value in request_info['headers'].items():
                if key.lower() == 'x-amz-target' and '.' in value:
                    return value.split('.')[-1]
        # Action query parameter (EC2, IAM, STS, and other Query API-style services).
        # These services encode the action entirely in the query string and always use
        # a root path ("/").  REST API services (e.g. Lambda, Access Analyzer) also run
        # on *.amazonaws.com but use path routing — they must NOT be matched here even
        # if a ?Action= parameter accidentally appears in the URL.
        parsed_url = urllib.parse.urlparse(endpoint)
        if parsed_url.query and parsed_url.path in ('', '/'):
            params = urllib.parse.parse_qs(parsed_url.query)
            if 'Action' in params:
                return params['Action'][0]
        # Operation name already in CamelCase (no spaces) - use directly
        if operation and ' ' not in operation:
            return operation
        # Human-readable operation name - only convert to CamelCase for S3, where
        # path-based routing makes the operation label meaningful.  For other AWS
        # services (EC2, CloudWatch, etc.) the action is conveyed via ?Action= or
        # X-Amz-Target; if neither was found above, the label is just a human-readable
        # datasource name and converting it would produce a nonsensical permission.
        if operation and service_prefix == 's3':
            if service_prefix == 's3':
                # IAM action names follow the s3: permission strings used in IAM policies,
                # which differ from the S3 SDK operation names for some sub-resource
                # operations (e.g. the IAM action is s3:GetLifecycleConfiguration, not
                # s3:GetBucketLifecycleConfiguration).
                S3_ACTION_MAP = {
                    'List Buckets': 'ListAllMyBuckets',
                    # GET sub-resource operations
                    'Get Bucket Tags': 'GetBucketTagging',
                    'Get Bucket Encryption Configuration': 'GetEncryptionConfiguration',
                    'Get Bucket Versioning Configuration': 'GetBucketVersioning',
                    'Get Bucket Lifecycle Configuration': 'GetLifecycleConfiguration',
                    'Get Bucket Logging Configuration': 'GetBucketLogging',
                    'Get Bucket Public Access Block': 'GetBucketPublicAccessBlock',
                    'Get Bucket Policy': 'GetBucketPolicy',
                    'Get Bucket Location': 'GetBucketLocation',
                    'Get Bucket Intelligent Tiering Configuration': 'GetIntelligentTieringConfiguration',
                    'Get Bucket CORS': 'GetBucketCors',
                    'Get Bucket ACLs': 'GetBucketAcl',
                    'Get Bucket Uploads': 'ListBucketMultipartUploads',
                    # PUT/POST sub-resource operations
                    'Put Bucket Tags': 'PutBucketTagging',
                    'Put Bucket Encryption Configuration': 'PutEncryptionConfiguration',
                    'Put Bucket Versioning Configuration': 'PutBucketVersioning',
                    'Put Bucket Lifecycle Configuration': 'PutLifecycleConfiguration',
                    'Put Bucket Logging Configuration': 'PutBucketLogging',
                    'Put Bucket Public Access Block': 'PutPublicAccessBlock',
                    'Put Bucket Policy': 'PutBucketPolicy',
                    'Put Bucket CORS': 'PutBucketCors',
                    'Put Bucket ACLs': 'PutBucketAcl',
                    # DELETE sub-resource operations
                    'Delete Bucket Tags': 'DeleteBucketTagging',
                    'Delete Bucket Encryption Configuration': 'DeleteBucketEncryption',
                    'Delete Bucket Lifecycle Configuration': 'DeleteLifecycleConfiguration',
                    'Delete Bucket Policy': 'DeleteBucketPolicy',
                    'Delete Bucket CORS': 'DeleteBucketCors',
                    # Object operations
                    'Get Object': 'GetObject',
                    'Delete Object': 'DeleteObject',
                    'Delete Bucket': 'DeleteBucket',
                    'List Multipart Upload Parts': 'ListMultipartUploadParts',
                    'Abort Multipart Upload': 'AbortMultipartUpload',
                }
                if operation in S3_ACTION_MAP:
                    return S3_ACTION_MAP[operation]
            # Generic CamelCase conversion: "List Clusters" -> "ListClusters"
            # Skip generic fallback operations ending with "Resource" — they carry
            # no meaningful action information (e.g. "Delete Resource" from an
            # unresolvable path) and would produce nonsensical permissions.
            if operation.endswith('Resource'):
                return ''
            words = operation.split()
            if words:
                return ''.join(word[0].upper() + word[1:] for word in words if word)
        return ''

    def _derive_azure_permission(self, endpoint, method):
        """Derive the Azure RBAC permission string (e.g., 'Microsoft.Compute/virtualMachines/read')."""
        parsed = urllib.parse.urlparse(endpoint)
        host = parsed.netloc
        path = parsed.path
        method_upper = method.upper()
        METHOD_TO_ACTION = {
            'GET': 'read',
            'POST': 'action',
            'PUT': 'write',
            'PATCH': 'write',
            'DELETE': 'delete',
        }
        action = METHOD_TO_ACTION.get(method_upper, 'action')
        # Azure Storage REST APIs served from storage account subdomains.
        # The permissions are path-depth-aware:
        #   GET /?comp=list                         → containers/list (list containers)
        #   GET /{container}                        → containers/read
        #   GET /{container}?restype=container&comp=list → containers/blobs/list (list blobs)
        #   GET /{container}/{blob}[/...]           → containers/blobs/read
        #   PUT / POST on blob path                 → containers/blobs/write
        #   DELETE on blob path                     → containers/blobs/delete
        #   DELETE on container path                → containers/delete
        if 'blob.core.windows.net' in host:
            parsed = urllib.parse.urlparse(f'https://fake{path}' if not path.startswith('/') else f'https://fake{path}')
            path_parts = [p for p in (parsed.path or path).split('/') if p]
            query_str = urllib.parse.urlparse(endpoint).query
            qparams = urllib.parse.parse_qs(query_str) if query_str else {}
            comp = (qparams.get('comp') or [''])[0]
            restype = (qparams.get('restype') or [''])[0]
            base = 'Microsoft.Storage/storageAccounts/blobServices'
            if len(path_parts) == 0:
                # Root: ?comp=list → list containers
                if comp == 'list':
                    return f'{base}/containers/list'
                return f'{base}/{action}'
            elif len(path_parts) == 1:
                # Container-level
                if restype == 'container' and comp == 'list':
                    return f'{base}/containers/blobs/read'
                if method_upper == 'DELETE':
                    return f'{base}/containers/delete'
                return f'{base}/containers/read'
            else:
                # Blob-level (2+ path segments)
                if method_upper in ('PUT', 'POST'):
                    return f'{base}/containers/blobs/write'
                if method_upper == 'DELETE':
                    return f'{base}/containers/blobs/delete'
                return f'{base}/containers/blobs/read'
        if 'queue.core.windows.net' in host:
            return f'Microsoft.Storage/storageAccounts/queueServices/{action}'
        if 'table.core.windows.net' in host:
            return f'Microsoft.Storage/storageAccounts/tableServices/{action}'
        # Azure Monitor metrics batch endpoint
        if 'metrics.monitor.azure' in host:
            return 'Microsoft.Insights/metrics/read'
        # Azure Pricing API has no RBAC requirement
        if 'prices.azure.com' in host:
            return ''
        # Azure Management API
        if 'management.azure' in host or 'management.chinacloudapi' in host:
            return self._derive_azure_management_permission(path, action)
        return ''

    def _derive_azure_management_permission(self, path, action):
        """Derive an Azure RBAC permission from a management.azure.com URL path."""
        path_clean = path.split('?')[0].rstrip('/')
        if not path_clean:
            return ''
        # Azure REST API uses a small set of well-known literal strings as singleton
        # resource IDs (e.g. /tags/default, /securityContacts/current).  These are
        # fixed path components, not runtime values, so they don't appear as {placeholders}
        # in the parsed URL -- but they ARE resource IDs in RBAC terms and must be
        # excluded from the permission path just like placeholder IDs.
        AZURE_SINGLETON_LITERALS = {'default', 'current', 'latest', 'primary', 'live'}
        # Provider-based paths: .../providers/Microsoft.X/resourceType[/{id}/subType...]
        if '/providers/' in path_clean:
            after_provider = path_clean.split('/providers/')[-1]
            segments = [s for s in after_provider.split('/') if s]
            if not segments:
                return ''
            # Azure ARM paths follow a type/name/type/name alternating pattern.
            # Names appear at even positions (0-indexed: 2, 4, 6 …) relative to the
            # namespace (position 0).  Names may be {placeholders} or well-known
            # singleton literals.  Some paths, however, also have short literal name
            # segments (e.g. "web" in /config/web) that are actually sub-resource type
            # specifiers and must be kept.
            #
            # Strategy:
            #   - Always drop {placeholder} segments — they are always names.
            #   - Always drop AZURE_SINGLETON_LITERALS.
            #   - When the path contains any placeholder (has_placeholder=True),
            #     additionally drop even-position literals that look like config/
            #     parameter names (contain underscores or dots), since these are resource
            #     instance identifiers embedded in the path (e.g. connection_throttling,
            #     tls_version, log_retention_days).
            #   - Short single-word literals without underscores at even positions (e.g.
            #     "web" in /sites/{name}/config/web) are kept because they are legitimate
            #     sub-resource type specifiers in ARM RBAC.
            #   - When the path has NO placeholder, keep all non-singleton segments
            #     (compound fixed resource type paths like eventtypes/management/values).
            has_placeholder = any(
                seg.startswith('{') and seg.endswith('}') for seg in segments
            )
            type_segments = []
            for idx, seg in enumerate(segments):
                if seg.startswith('{') and seg.endswith('}'):
                    continue  # placeholder name — always skip
                if seg.lower() in AZURE_SINGLETON_LITERALS:
                    continue  # known singleton identifier — skip
                # For placeholder-containing paths, additionally drop even-position
                # literals that contain underscores or dots (config param names).
                if has_placeholder and idx > 0 and idx % 2 == 0:
                    if '_' in seg or '.' in seg:
                        continue  # config parameter name — skip
                type_segments.append(seg)
            # Normalize provider namespace capitalisation (e.g., microsoft.insights -> Microsoft.Insights)
            if type_segments and '.' in type_segments[0]:
                ns_parts = type_segments[0].split('.')
                type_segments[0] = '.'.join(p[0].upper() + p[1:] if p else p for p in ns_parts)
            resource_path = '/'.join(type_segments)
            return f'{resource_path}/{action}'
        # Non-provider paths: handle common well-known patterns
        segments = [s for s in path_clean.split('/') if s]
        non_placeholder = [s for s in segments if not (s.startswith('{') and s.endswith('}'))]
        if not non_placeholder:
            return ''
        first = non_placeholder[0].lower()
        if first == 'subscriptions':
            if len(non_placeholder) == 1:
                return f'Microsoft.Resources/subscriptions/{action}'
            second = non_placeholder[1].lower()
            if second == 'resourcegroups':
                if len(non_placeholder) == 2:
                    return f'Microsoft.Resources/subscriptions/resourceGroups/{action}'
                return f'Microsoft.Resources/subscriptions/resourceGroups/{"/".join(non_placeholder[2:])}/{action}'
            if second == 'resources':
                return f'Microsoft.Resources/subscriptions/resources/{action}'
            if second == 'providers':
                return f'Microsoft.Resources/subscriptions/providers/{action}'
        elif first == 'tenants':
            return f'Microsoft.Resources/tenants/{action}'
        elif first == 'savingsplanorders':
            if len(non_placeholder) >= 2 and non_placeholder[1].lower() == 'savingsplans':
                return f'Microsoft.BillingBenefits/savingsPlanOrders/savingsPlans/{action}'
            return f'Microsoft.BillingBenefits/savingsPlanOrders/{action}'
        # Paths that start with a resource-ID placeholder then a known sub-resource or action
        # suffix.  The parent resource type is not available from the URL alone, so these
        # mappings are based on known Flexera policy patterns.
        if segments and segments[0].startswith('{') and segments[0].endswith('}'):
            # Strip singleton literals (e.g. /default, /current) from suffix before lookup
            suffix_parts = [s.lower() for s in non_placeholder
                            if s.lower() not in AZURE_SINGLETON_LITERALS]
            suffix = '/'.join(suffix_parts)
            RESOURCE_ID_SUFFIX_MAP = {
                # SQL Server sub-resources
                'databases':            'Microsoft.Sql/servers/databases/read',
                'elasticpools':         'Microsoft.Sql/servers/elasticPools/read',
                # Storage account sub-resources
                'managementpolicies':   'Microsoft.Storage/storageAccounts/managementPolicies/read',
                # Savings plan sub-resources (BillingBenefits)
                'savingsplans':         'Microsoft.BillingBenefits/savingsPlanOrders/savingsPlans/read',
                # Compute VM actions
                'poweroff':             'Microsoft.Compute/virtualMachines/powerOff/action',
                'start':                'Microsoft.Compute/virtualMachines/start/action',
                'deallocate':           'Microsoft.Compute/virtualMachines/deallocate/action',
                'restart':              'Microsoft.Compute/virtualMachines/restart/action',
                'generalize':           'Microsoft.Compute/virtualMachines/generalize/action',
                'instanceview':         'Microsoft.Compute/virtualMachines/instanceView/read',
                # Synapse SQL Pool actions
                'pause':                'Microsoft.Synapse/workspaces/sqlPools/pause/action',
            }
            if suffix in RESOURCE_ID_SUFFIX_MAP:
                return RESOURCE_ID_SUFFIX_MAP[suffix]
        return ''

    def _derive_gcp_permission(self, endpoint, method):
        """Derive the GCP IAM permission string (e.g., 'compute.regions.list')."""
        parsed = urllib.parse.urlparse(endpoint)
        host = parsed.netloc
        path = parsed.path
        # Special case: /b/{id}/iam -> getIamPolicy on a storage bucket
        if host == 'storage.googleapis.com' and re.search(r'/b/[^/]+/iam$', path):
            return 'storage.buckets.getIamPolicy'
        # GCP Compute Engine selfLink-derived action paths: /{dynamic}/action
        # The resource type cannot be determined from the selfLink alone for generic
        # deletes/patches, but the named action suffix identifies well-known operations.
        # Applies to both compute.googleapis.com and www.googleapis.com selfLinks.
        SELFLINK_ACTION_MAP = {
            'start':          'compute.instances.start',
            'stop':           'compute.instances.stop',
            'setMachineType': 'compute.instances.setMachineType',
            'setLabels':      'compute.instances.setLabels',
            'createSnapshot': 'compute.disks.createSnapshot',
            'delete':         'compute.instances.delete',
        }
        for selflink_host in ('compute.googleapis.com', 'www.googleapis.com'):
            if host == selflink_host and re.match(r'^/\{dynamic\}/', path):
                action = path.split('/{dynamic}/', 1)[-1].split('?')[0].rstrip('/')
                if action in SELFLINK_ACTION_MAP:
                    return SELFLINK_ACTION_MAP[action]
        # GCP selfLink-derived structured paths: /compute/v1/{resource}[/{action}]
        # These are produced when a known GCP selfLink variable (e.g. $instance['selfLink'])
        # is resolved to a representative path like /compute/v1/instances.  The resource
        # type and, optionally, the action suffix uniquely determine the IAM permission.
        if host == 'compute.googleapis.com':
            selflink_path_m = re.match(r'^/compute/v1/(\w+)(?:/(\w+))?$', path)
            if selflink_path_m:
                resource = selflink_path_m.group(1)
                action_suffix = selflink_path_m.group(2)  # None when no action suffix
                m_upper = method.upper()
                GCP_SELFLINK_PERM_MAP = {
                    # Compute instance actions
                    ('instances', 'setMachineType', 'POST'):  'compute.instances.setMachineType',
                    ('instances', 'start', 'POST'):           'compute.instances.start',
                    ('instances', 'stop', 'POST'):            'compute.instances.stop',
                    ('instances', 'setLabels', 'POST'):       'compute.instances.setLabels',
                    ('instances', None, 'DELETE'):            'compute.instances.delete',
                    ('instances', None, 'GET'):               'compute.instances.get',
                    ('instances', None, 'PATCH'):             'compute.instances.update',
                    # Compute disk actions
                    ('disks', 'createSnapshot', 'POST'):      'compute.disks.createSnapshot',
                    ('disks', None, 'DELETE'):                'compute.disks.delete',
                    ('disks', None, 'PATCH'):                 'compute.disks.update',
                    # Compute snapshots
                    ('snapshots', None, 'DELETE'):            'compute.snapshots.delete',
                    # Compute addresses
                    ('addresses', None, 'DELETE'):            'compute.addresses.delete',
                    # Compute firewalls
                    ('firewalls', None, 'DELETE'):            'compute.firewalls.delete',
                    # GCP zone operations
                    ('zoneOperations', None, 'GET'):          'compute.zoneOperations.get',
                }
                perm = GCP_SELFLINK_PERM_MAP.get((resource, action_suffix, m_upper))
                if perm:
                    return perm
        # GCP Recommender API: the recommender type ID is embedded in the path as a
        # literal string (e.g. google.compute.commitment.UsageCommitmentRecommender).
        # The generic path-based derivation produces the incorrect permission
        # "recommender.recommendations.list"; map the known type IDs to their correct
        # type-specific IAM permissions instead.  When the type is a dynamic {id}
        # placeholder (unknown at analysis time), return empty rather than a wrong value.
        if host == 'recommender.googleapis.com':
            rec_type_m = re.search(
                r'/recommenders/([^/]+)/recommendations', path
            )
            if rec_type_m:
                rec_type = rec_type_m.group(1)
                if rec_type.startswith('{') and rec_type.endswith('}'):
                    return ''  # dynamic type — cannot determine specific permission
                RECOMMENDER_PERMISSION_MAP = {
                    'google.compute.commitment.UsageCommitmentRecommender':
                        'recommender.usageCommitmentRecommendations.list',
                    'google.compute.address.IdleResourceRecommender':
                        'recommender.computeAddressIdleResourceRecommendations.list',
                    'google.compute.disk.IdleResourceRecommender':
                        'recommender.computeDiskIdleResourceRecommendations.list',
                    'google.compute.image.IdleResourceRecommender':
                        'recommender.computeImageIdleResourceRecommendations.list',
                    'google.compute.instance.IdleResourceRecommender':
                        'recommender.computeInstanceIdleResourceRecommendations.list',
                    'google.compute.instance.MachineTypeRecommender':
                        'recommender.computeInstanceMachineTypeRecommendations.list',
                    'google.compute.instanceGroupManager.MachineTypeRecommender':
                        'recommender.computeInstanceGroupManagerMachineTypeRecommendations.list',
                    'google.cloudsql.instance.IdleRecommender':
                        'recommender.cloudsqlIdleInstanceRecommendations.list',
                    'google.cloudsql.instance.OverprovisionedRecommender':
                        'recommender.cloudsqlOverprovisionedInstanceRecommendations.list',
                    'google.cloudsql.instance.OutOfDiskRecommender':
                        'recommender.cloudsqlInstanceOutOfDiskRecommendations.list',
                    'google.iam.policy.Recommender':
                        'recommender.iamPolicyRecommendations.list',
                    'google.container.DiagnosisRecommender':
                        'recommender.containerDiagnosisRecommendations.list',
                    'google.logging.productSuggestion.containerRecommender':
                        'recommender.loggingProductSuggestionContainerRecommendations.list',
                    'google.monitoring.productSuggestion.computeRecommender':
                        'recommender.monitoringProductSuggestionComputeRecommendations.list',
                    'google.resourcemanager.projectUtilization.Recommender':
                        'recommender.resourcemanagerProjectUtilizationRecommendations.list',
                    'google.run.service.SecurityRecommender':
                        'recommender.runServiceSecurityRecommendations.list',
                    'google.cloudsecurity.GeneralRecommender':
                        'recommender.cloudSecurityGeneralRecommendations.list',
                }
                return RECOMMENDER_PERMISSION_MAP.get(rec_type, '')
        service = self._get_gcp_service_prefix_from_host(host, path)
        if not service:
            return ''
        resource = self._extract_gcp_resource_from_path(path, service)
        if not resource:
            return ''
        verb = self._get_gcp_permission_verb(path, method)
        return f'{service}.{resource}.{verb}'

    def _get_gcp_service_prefix_from_host(self, host, path=''):
        """Map a GCP API hostname to its IAM permission service prefix."""
        prefixes = self._get_gcp_service_prefixes()
        if not host:
            return ''
        # www.googleapis.com uses legacy paths that start with the service name
        if host == 'www.googleapis.com':
            path_parts = [s for s in path.split('/') if s]
            if path_parts:
                svc = path_parts[0]
                return prefixes.get(svc, svc)
            return ''
        if host.endswith('.googleapis.com'):
            host_prefix = host[:-len('.googleapis.com')]
            return prefixes.get(host_prefix, host_prefix)
        return ''

    def _extract_gcp_resource_from_path(self, path, service):
        """Extract the GCP IAM resource type name from a URL path.

        Applies the following rules in order:
        1. Handle known special-case sub-resource paths (e.g. /b/{id}/iam).
        2. Strip version segments (v1, v2, v1beta1, ...).
        3. Strip placeholder segments ({...}).
        4. Strip segments that are directly followed by a placeholder (they are
           parent-resource navigational segments, not the target resource type).
        5. Strip the service-name prefix when it appears as the first path segment.
        6. Strip common non-resource qualifiers ('global', 'aggregated').
        7. Return the last remaining segment after applying abbreviation mappings.
        """
        abbreviations = self._get_gcp_resource_abbreviations()
        # Special case: /b/{id}/iam -> IAM policy on a bucket
        if re.search(r'/b/[^/]+/iam$', path):
            return 'buckets'
        path = path.rstrip('/')
        if not path:
            return ''
        segments = [s for s in path.split('/') if s]
        # Identify segments that are directly followed by a placeholder
        followed_by_placeholder = set()
        for i, seg in enumerate(segments):
            if i + 1 < len(segments):
                nxt = segments[i + 1]
                if nxt.startswith('{') and nxt.endswith('}'):
                    followed_by_placeholder.add(i)
        version_re = re.compile(r'^v\d+')
        NON_RESOURCE = {'global', 'aggregated'}
        filtered = []
        for i, seg in enumerate(segments):
            if version_re.match(seg):
                continue
            if seg.startswith('{') and seg.endswith('}'):
                continue
            if i in followed_by_placeholder:
                continue
            if seg in NON_RESOURCE:
                continue
            filtered.append(seg)
        # Remove service-name prefix if it appears as the first path component
        if filtered and filtered[0].lower() == service.lower():
            filtered = filtered[1:]
        if not filtered:
            return ''
        resource = filtered[-1]
        # Strip :verb suffix (e.g. "entries:list" -> "entries")
        if ':' in resource:
            resource = resource.split(':')[0]
        if not resource:
            return ''
        # Detect operation-on-resource paths generated from GCP selfLink resolution
        # (e.g., /{dynamic}/start, /{dynamic}/setMachineType).
        #
        # When a define block uses `$var['selfLink'] + '/action'`, the URL resolver
        # produces a path like `/{dynamic}/action` where `{dynamic}` is the generic
        # placeholder for the selfLink.  The action segment (start, stop, createSnapshot,
        # etc.) is an operation applied to the preceding resource instance, NOT the
        # resource type itself.
        #
        # Distinguishing factor: real GCP API paths use named placeholders like
        # {project}, {zone}, {id}, {name}; selfLink-derived paths use `{dynamic}`.
        # Only suppress when the directly preceding placeholder is `{dynamic}`.
        orig_idx = None
        for i in range(len(segments) - 1, -1, -1):
            if segments[i] == resource:
                orig_idx = i
                break
        if orig_idx is not None and orig_idx > 0:
            prev_seg = segments[orig_idx - 1]
            if prev_seg == '{dynamic}':
                # This is a selfLink-derived path with an action suffix.
                # The resource type is unknown; return '' to avoid a wrong permission.
                return ''
        return abbreviations.get(resource, resource)

    def _get_gcp_permission_verb(self, path, method):
        """Determine the GCP IAM permission verb from the URL path and HTTP method."""
        # Check for :operation suffix on the last path segment
        path_stripped = path.rstrip('/')
        if path_stripped:
            last_segment = path_stripped.split('/')[-1]
            if ':' in last_segment:
                op = last_segment.split(':')[-1]
                OP_TO_VERB = {
                    'list': 'list',
                    'aggregatedList': 'aggregatedList',
                    'search': 'list',
                    'query': 'list',
                    'get': 'get',
                    'getIamPolicy': 'getIamPolicy',
                    'setIamPolicy': 'setIamPolicy',
                    'create': 'create',
                    'insert': 'create',
                    'delete': 'delete',
                    'update': 'update',
                    'patch': 'update',
                }
                return OP_TO_VERB.get(op, op)
        method_upper = method.upper()
        if method_upper == 'GET':
            return 'list'
        elif method_upper == 'POST':
            return 'create'
        elif method_upper in ('PUT', 'PATCH'):
            return 'update'
        elif method_upper == 'DELETE':
            return 'delete'
        return 'get'

    def _get_ds_raw_path(self, ds_body):
        """Extract the raw path string from a datasource body (lightweight, for iteration chain analysis)."""
        path_match = re.search(r'path\s+join\(\[([^\]]+)\]\)', ds_body)
        if path_match:
            join_content = path_match.group(1)
            parts = []
            current_part = ''
            depth = 0
            for char in join_content + ',':
                if char in '([':
                    depth += 1
                    current_part += char
                elif char in ')]':
                    depth -= 1
                    current_part += char
                elif char == ',' and depth == 0:
                    part = current_part.strip()
                    if part:
                        parts.append(part)
                    current_part = ''
                else:
                    current_part += char
            path_result = ''
            for part in parts:
                part = part.strip()
                val_m = re.search(r'val\(iter_item,\s*["\']([^"\']+)["\']\)', part)
                if val_m:
                    path_result += '{' + val_m.group(1) + '}'
                else:
                    string_m = re.match(r'^["\']([^"\']+)["\']$', part)
                    if string_m:
                        path_result += string_m.group(1)
            return path_result if path_result else None
        path_match = re.search(r'path\s+["\']([^"\']+)["\']', ds_body)
        if path_match:
            return path_match.group(1)
        return None

    def _build_azure_iter_resource_type_map(self, datasources):
        """Build a map from datasource name to Azure resource type string.

        For datasources whose path starts with {id} or {resourceID} (i.e. produced by
        val(iter_item, "id") or val(iter_item, "resourceID")), resolve the Azure resource
        type by following the iterate chain and run_script parameter references until a
        datasource with a /providers/Namespace/resourceType path is found.

        Returns a dict: {datasource_name: 'Namespace.Provider/resourceType'}
        """
        ds_info_map = {}
        for ds in datasources:
            body = ds['body']
            name = ds['name']
            iter_m = re.search(r'\biterate\s+\$(\w+)', body)
            iterate_parent = iter_m.group(1) if iter_m else None
            path = self._get_ds_raw_path(body)
            # Collect all $ds_* variable references for filter/script datasources
            ds_refs = ['ds_' + ref for ref in re.findall(r'\$ds_(\w+)', body)]
            ds_info_map[name] = {
                'path': path,
                'iterate_parent': iterate_parent,
                'ds_refs': ds_refs,
            }

        def get_azure_type(ds_name, seen=None):
            if seen is None:
                seen = set()
            if ds_name in seen or ds_name not in ds_info_map:
                return None
            seen = seen | {ds_name}
            info = ds_info_map[ds_name]
            path = info.get('path') or ''
            # Path starts with a placeholder — follow the iterate parent and
            # accumulate any non-placeholder, non-singleton suffix segments so
            # that multi-level chains like {id}/databases/{id}/transparentDataEncryption
            # resolve to the correct type (e.g. Microsoft.Sql/servers/databases/...).
            if path.startswith('{id}') or path.startswith('{resourceID}') or path.startswith('{name}'):
                parent = info.get('iterate_parent')
                parent_type = get_azure_type(parent, seen)
                if parent_type is None:
                    return None
                AZURE_SINGLETON_LITERALS = {'default', 'current', 'latest', 'primary', 'live'}
                bracket_end = path.index('}')
                suffix = path[bracket_end + 1:]
                suffix_segs = [
                    s for s in suffix.strip('/').split('/')
                    if s and not s.startswith('{') and s.lower() not in AZURE_SINGLETON_LITERALS
                ]
                if suffix_segs:
                    return parent_type + '/' + '/'.join(suffix_segs)
                return parent_type
            # Path contains /providers/ — extract the resource type
            if path and '/providers/' in path:
                m = re.search(r'/providers/([A-Za-z.]+(?:/[A-Za-z]+)+)', path)
                if m:
                    type_str = m.group(1)
                    segments = type_str.split('/')
                    non_placeholder = [s for s in segments if not (s.startswith('{') and s.endswith('}'))]
                    return '/'.join(non_placeholder) if non_placeholder else None
            # No useful path — try iterate parent then script/datasource references
            candidates = []
            if info.get('iterate_parent'):
                candidates.append(info['iterate_parent'])
            for ref in info.get('ds_refs', []):
                if ref not in seen and ref != ds_name:
                    candidates.append(ref)
            for candidate in candidates:
                result = get_azure_type(candidate, seen)
                if result:
                    return result
            return None

        result = {}
        for name, info in ds_info_map.items():
            path = info.get('path') or ''
            if path.startswith('{id}') or path.startswith('{resourceID}'):
                resource_type = get_azure_type(info.get('iterate_parent'), {name})
                if resource_type:
                    result[name] = resource_type
        return result

    def _get_azure_provider_resource_types(self):
        """Return the set of primary Azure ARM resource types used in this policy's datasources.

        Scans the Flexera ``path join([...])`` and ``path "..."`` declarations in
        datasource bodies for ``/providers/Namespace/resourceType`` patterns.
        Meta-resources such as ``locations``, ``operations``, and ``metrics`` are
        excluded so that only the *data* resource types remain.

        Returns a set of strings like ``{'Microsoft.Compute/virtualMachines'}``.
        When the set contains exactly one element the caller can safely derive an
        Azure RBAC permission for define-block API calls that operate on dynamic
        ARM resource IDs (``href: $instance["id"]`` style).
        """
        # Azure ARM path segments that are navigation/meta helpers, not data resources.
        AZURE_META_RESOURCES = frozenset({
            'locations', 'operations', 'providers', 'usage', 'usages',
            'metrics', 'metricdefinitions', 'advisorrecommendations',
            'features', 'skus', 'capabilities',
        })
        types = set()
        # Only inspect Flexera policy-language path declarations (path join([...]) or
        # path "..."), NOT JavaScript paths inside script blocks, to avoid picking up
        # sub-resource paths built at runtime (e.g. resource_id + "/providers/insights/metrics").
        def _add_type_from_join(join_content):
            p = re.search(
                r'/providers/([A-Za-z][A-Za-z0-9]*\.[A-Za-z][A-Za-z0-9]*/[A-Za-z][A-Za-z0-9]+)',
                join_content,
            )
            if not p:
                return
            resource_type = p.group(1)
            parts = resource_type.split('/')
            if len(parts) != 2:
                return
            resource_name = parts[1].lower()
            if resource_name in AZURE_META_RESOURCES:
                return
            # Normalize namespace capitalisation
            ns_parts = parts[0].split('.')
            parts[0] = '.'.join(seg[0].upper() + seg[1:] if seg else seg for seg in ns_parts)
            primary = '/'.join(parts)
            types.add(primary)
            # Also check whether the join content contains a sub-resource path that follows
            # the primary type.  Pattern: the primary type is followed (after a variable
            # reference) by a string literal like "/subType".  This indicates that the
            # policy's define blocks may be operating on a child resource, not the top-level
            # resource type, so the fallback permission derivation should not fire.
            remaining = join_content[p.end():]
            sub_m = re.search(r'"/([A-Za-z][A-Za-z0-9]+)"', remaining)
            if sub_m:
                sub_name = sub_m.group(1).lower()
                if sub_name not in AZURE_META_RESOURCES:
                    # Preserve original casing from the source
                    types.add(f'{primary}/{sub_m.group(1)}')

        for m in re.finditer(r'\bpath\s+join\(\[([^\]]+)\]\)', self.content):
            _add_type_from_join(m.group(1))
        for m in re.finditer(r'\bpath\s+"([^"]*providers/[^"]+)"', self.content):
            _add_type_from_join(m.group(1))
        # Detect sub-resource datasource paths of the form:
        #   path join([val(iter_item, "id"), "/subType"])
        # These follow on from the primary resource type already detected above and
        # indicate that define blocks may operate on child resources (e.g. databases
        # under servers) rather than the top-level resource type.  Adding the combined
        # compound type to the cache prevents the fallback from assigning an incorrect
        # parent-level permission (servers/write instead of servers/databases/write).
        if types:
            primary_list = sorted(types)
            for m in re.finditer(
                r'\bpath\s+join\(\[\s*(?:val\([^)]+\)|"[^"]*\{[^}]+\}[^"]*")'
                r'\s*,\s*"/([A-Za-z][A-Za-z0-9]+)"',
                self.content,
            ):
                sub_name = m.group(1)
                if sub_name.lower() in AZURE_META_RESOURCES:
                    continue
                # Match the sub-resource to the detected primary type (heuristic:
                # pick the one-type case so the fallback becomes 2 types and won't fire).
                for primary in primary_list:
                    compound = f'{primary}/{sub_name}'
                    if compound not in types:
                        types.add(compound)
        return types

    def _extract_define_blocks(self):
        """Extract all define blocks from the policy template."""
        define_blocks = []
        lines = self.content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            define_match = re.match(r'^define\s+(\w+)\s*\([^)]*\).*\bdo\s*$', line)
            if define_match:
                define_name = define_match.group(1)
                define_lines = []
                i += 1
                depth = 1
                while i < len(lines) and depth > 0:
                    current_line = lines[i]
                    if not re.match(r'^\s*#', current_line):
                        if re.search(r'\bdo\s*$', current_line):
                            depth += 1
                        elif re.match(r'^\s*(?:if|unless)\b', current_line) and not re.search(r'\bdo\s*$', current_line):
                            # if/unless blocks in CWF do not use 'do' but are still
                            # closed by 'end', so they must be counted as depth openers.
                            depth += 1
                        elif re.match(r'^\s*end\s*$', current_line):
                            depth -= 1
                            if depth == 0:
                                break
                    define_lines.append(current_line)
                    i += 1
                define_blocks.append({
                    'name': define_name,
                    'body': '\n'.join(define_lines)
                })
            i += 1
        return define_blocks

    def _resolve_define_variable(self, var_expr, pre_context, _depth=0):
        """Resolve a value expression in a define block to a string.

        Handles string literals, well-known parameter references, simple variable
        lookups in pre_context, concatenation with +, and join([...]) calls.
        Returns the resolved string, or None if too dynamic to resolve.
        """
        if not var_expr or _depth > 2:
            return None
        var_expr = var_expr.strip().rstrip(',').strip()
        if not var_expr:
            return None
        # String literal
        m = re.match(r'^["\']([^"\']*)["\']$', var_expr)
        if m:
            return m.group(1)
        # Well-known Azure management endpoint parameter or local variable derived from it.
        # Only match when var_expr IS a simple variable reference (not a larger expression
        # that happens to mention azure_endpoint in a concatenation).
        if re.match(r'^\$\w*azure_endpoint\w*$', var_expr, re.IGNORECASE):
            return 'management.azure.com'
        # Unwrap common single-argument function calls (strip, to_s, etc.) that just pass
        # a value through without changing its semantic meaning for URL/host resolution.
        single_arg_func_m = re.match(r'^(?:strip|to_s|downcase|upcase)\s*\(\s*(.+?)\s*\)\s*$', var_expr)
        if single_arg_func_m:
            return self._resolve_define_variable(single_arg_func_m.group(1), pre_context, _depth + 1)
        # Array/hash access for S3 bucket host: $var["host"] or $var['host']
        if re.match(r'^\$\w+\[["\'"]host["\']\]$', var_expr) or re.match(r"^\$\w+\['host'\]$", var_expr):
            return '{bucket}.s3.amazonaws.com'
        # GCP resource selfLink field: $var['selfLink'] or $var["selfLink"]
        # selfLink is always a full Google Cloud API URL, e.g.
        # https://compute.googleapis.com/compute/v1/projects/{p}/zones/{z}/instances/{name}
        # Map the variable name to the most likely GCP service host AND resource path so
        # that _derive_gcp_permission can identify the resource type for permission lookup.
        selflink_m = re.match(r"^\$(\w+)\[(?:'selfLink'|\"selfLink\")\]$", var_expr)
        if selflink_m:
            var_name = selflink_m.group(1).lower()
            # Maps variable name -> (host, resource path without trailing placeholder)
            # The resource path must NOT end with a placeholder so that
            # _extract_gcp_resource_from_path can identify the final path segment as the
            # resource type (the "followed_by_placeholder" logic strips segments that
            # are directly followed by a {placeholder}).
            GCP_SELFLINK_RESOURCE_MAP = {
                'snapshot': ('compute.googleapis.com', 'compute/v1/snapshots'),
                'instance': ('compute.googleapis.com', 'compute/v1/instances'),
                'disk':     ('compute.googleapis.com', 'compute/v1/disks'),
                'address':  ('compute.googleapis.com', 'compute/v1/addresses'),
                'firewall': ('compute.googleapis.com', 'compute/v1/firewalls'),
                'operation': ('compute.googleapis.com', 'compute/v1/zoneOperations'),
            }
            if var_name in GCP_SELFLINK_RESOURCE_MAP:
                # Special case: a variable named 'instance' in a Cloud SQL policy
                # (one that calls sqladmin.googleapis.com) refers to a Cloud SQL instance,
                # not a Compute Engine instance.  Its selfLink points to sqladmin, so we
                # must not map it to compute.googleapis.com — return a generic placeholder
                # so that the permission derivation returns empty rather than wrong.
                if var_name == 'instance' and 'sqladmin.googleapis.com' in self.content:
                    return 'https://sqladmin.googleapis.com/{dynamic}'
                host, resource_path = GCP_SELFLINK_RESOURCE_MAP[var_name]
                return f'https://{host}/{resource_path}'
            # Unknown variable name — fall back to generic {dynamic} placeholder.
            # Keep compute.googleapis.com for known compute variable prefixes, otherwise
            # use www.googleapis.com (the legacy/generic GCP API host).
            GCP_RESOURCE_HOSTS = {
                'snapshot': 'compute.googleapis.com',
                'instance': 'compute.googleapis.com',
                'disk': 'compute.googleapis.com',
                'address': 'compute.googleapis.com',
                'firewall': 'compute.googleapis.com',
                'operation': 'compute.googleapis.com',
            }
            host = GCP_RESOURCE_HOSTS.get(var_name, 'www.googleapis.com')
            return f'https://{host}/{{dynamic}}'
        # Concatenation with + (handles both 'a + b' (spaced) and 'a+b' (unspaced))
        concat_parts = self._split_concat_expr(var_expr)
        if concat_parts is not None and len(concat_parts) > 1:
            resolved = [self._resolve_define_variable(p, pre_context, _depth + 1) for p in concat_parts]
            return ''.join(r if r is not None else '{dynamic}' for r in resolved)
        # join([...]) call
        join_m = re.match(r'^join\(\[(.+)\]\)\s*$', var_expr, re.DOTALL)
        if join_m:
            join_inner = join_m.group(1)
            parts = [p.strip() for p in join_inner.split(',')]
            result = ''
            for part in parts:
                r = self._resolve_define_variable(part, pre_context, _depth + 1)
                result += r if r is not None else '{dynamic}'
            return result
        # Simple variable reference $var (not array access like $var["key"])
        m = re.match(r'^\$(\w+)$', var_expr)
        if m:
            var_name = m.group(1)
            assign_m = re.search(r'\$' + re.escape(var_name) + r'\s*=\s*(.+)', pre_context)
            if assign_m:
                rhs = assign_m.group(1).strip().rstrip(',').strip()
                return self._resolve_define_variable(rhs, pre_context, _depth + 1)
        # ARM / generic resource ID field access: $var["id"], $var["resourceID"],
        # $var["attached_vm"], $var["href"], $var["url"] — these are runtime ARM resource
        # IDs (full paths like /subscriptions/.../providers/Microsoft.Compute/virtualMachines/name).
        # We can't resolve them statically but we know the path will be non-empty.
        ARM_ID_FIELDS = frozenset({'id', 'resourceID', 'attached_vm', 'href', 'url'})
        field_access_m = re.match(r"^\$\w+\[(?:\"([^\"]+)\"|'([^']+)')\]$", var_expr)
        if field_access_m:
            field_name = field_access_m.group(1) or field_access_m.group(2)
            if field_name in ARM_ID_FIELDS:
                return '{id}'
        return None

    def _split_concat_expr(self, expr):
        """Split a CWF/Ruby expression on + operators outside string literals.

        Handles both 'a + b' (spaced) and 'a+b' (unspaced) forms.
        Returns a list of stripped non-empty parts when at least one + was found
        outside a string, or None if no such + exists.
        """
        parts = []
        current = []
        in_str = False
        str_char = None
        found_concat = False
        for ch in expr:
            if in_str:
                current.append(ch)
                if ch == str_char:
                    in_str = False
            elif ch in ('"', "'"):
                in_str = True
                str_char = ch
                current.append(ch)
            elif ch == '+':
                found_concat = True
                parts.append(''.join(current).strip())
                current = []
            else:
                current.append(ch)
        if current:
            parts.append(''.join(current).strip())
        parts = [p for p in parts if p]
        return parts if found_concat else None

    def _extract_balanced_parens(self, text, open_idx):
        """Return (content, end_pos) for balanced parens starting at open_idx (pointing to '(')."""
        depth = 0
        i = open_idx
        while i < len(text):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
                if depth == 0:
                    return text[open_idx + 1:i], i + 1
            i += 1
        return text[open_idx + 1:], len(text)

    def _extract_balanced_braces(self, text, open_idx):
        """Return the content inside balanced braces starting at open_idx (pointing to '{').

        Unlike _extract_hash_from_text, this correctly handles nested braces in values.
        Returns the raw string including the outer braces, or None if not balanced.
        """
        depth = 0
        i = open_idx
        while i < len(text):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    return text[open_idx:i + 1]
            i += 1
        return None

    def _extract_hash_pairs(self, hash_block):
        """Parse key-value pairs from a Ruby/RCL hash block.

        Keys must be string literals. String-valued entries return the literal string;
        entries with variable/expression values (e.g. $var["key"]) return '{dynamic}'.
        This ensures that keys whose values are runtime variables (e.g. query param keys
        like "uploadId") are still captured so they can be used for operation derivation.
        """
        pairs = {}
        for m in re.finditer(
            r'["\']([^"\']+)["\']\s*(?:=>|:)\s*'
            r'(?:["\']([^"\']*)["\']'       # group 2: string literal value
            r'|(\$[\w\[\]"\'.$]+))',         # group 3: variable reference
            hash_block,
        ):
            key = m.group(1)
            if m.group(2) is not None:
                pairs[key] = m.group(2)
            elif key not in pairs:
                pairs[key] = '{dynamic}'
        return pairs

    def _extract_hash_from_text(self, text, key):
        """Extract the {…} hash (or variable name) for a given key from a text block.

        Returns the raw '{...}' string if found inline, a variable name (str without '$')
        if a variable reference is used, or None if not found.
        """
        m = re.search(r'\b' + re.escape(key) + r'\s*:\s*(\{)', text)
        if m:
            brace_start = m.start(1)
            depth = 0
            i = brace_start
            while i < len(text):
                if text[i] == '{':
                    depth += 1
                elif text[i] == '}':
                    depth -= 1
                    if depth == 0:
                        return text[brace_start:i + 1]
                i += 1
        m = re.search(r'\b' + re.escape(key) + r'\s*:\s*(\$(\w+))', text)
        if m:
            return m.group(2)  # variable name without $
        return None

    def _extract_http_requests_from_define(self, define_name, define_body):
        """Extract all http_request() calls from a define block.

        Returns a list of request_info dicts compatible with _build_endpoint_url,
        _derive_permission, etc.
        """
        results = []
        pos = 0
        while True:
            idx = define_body.find('http_request(', pos)
            if idx == -1:
                break
            pre_context = define_body[:idx]
            arg_str, end_pos = self._extract_balanced_parens(define_body, idx + len('http_request'))
            pos = end_pos
            # Strip outer { } for the http_request({...}) call style
            arg_inner = arg_str.strip()
            if arg_inner.startswith('{') and arg_inner.endswith('}'):
                arg_inner = arg_inner[1:-1]
            # When the entire argument is a single variable ($request = {...}), look up
            # that variable's hash assignment in pre_context and use it as the arg body.
            single_var_m = re.match(r'^\s*\$(\w+)\s*$', arg_inner)
            if single_var_m:
                var_name = single_var_m.group(1)
                brace_m = None
                for bm in re.finditer(r'\$' + re.escape(var_name) + r'\s*=\s*\{', pre_context):
                    brace_m = bm
                if brace_m is None:
                    continue
                hash_str = self._extract_balanced_braces(pre_context, brace_m.end() - 1)
                if hash_str is None:
                    continue
                arg_inner = hash_str[1:-1]  # strip outer { }
            # Extract verb
            verb_m = re.search(r'\bverb\s*:\s*["\']([^"\']+)["\']', arg_inner, re.IGNORECASE)
            method = verb_m.group(1).upper() if verb_m else 'GET'
            # Extract host
            host = None
            host_m = re.search(r'\bhost\s*:\s*(.+)', arg_inner)
            if host_m:
                host_val = host_m.group(1).strip().split('\n')[0].rstrip(',').strip()
                host = self._resolve_define_variable(host_val, pre_context)
            # Extract href or path
            path = '/'
            href_m = re.search(r'\b(?:href|path)\s*:\s*(.+)', arg_inner)
            if href_m:
                href_val = href_m.group(1).strip().split('\n')[0].rstrip(',').strip()
                resolved = self._resolve_define_variable(href_val, pre_context)
                if resolved is not None:
                    path = resolved
            # Extract query_strings (inline hash or variable reference)
            query_params = {}
            qs_raw = self._extract_hash_from_text(arg_inner, 'query_strings')
            if qs_raw is not None:
                if isinstance(qs_raw, str) and qs_raw.startswith('{'):
                    query_params = self._extract_hash_pairs(qs_raw)
                elif isinstance(qs_raw, str):
                    # Variable reference — locate and brace-balance the assignment
                    for qm in re.finditer(r'\$' + re.escape(qs_raw) + r'\s*=\s*\{', pre_context):
                        hash_str = self._extract_balanced_braces(pre_context, qm.end() - 1)
                        if hash_str:
                            query_params = self._extract_hash_pairs(hash_str)
            # Extract headers (inline hash or variable reference).
            # CWF http_request() uses `header:` (singular); some callers use `headers:`.
            headers = {}
            hdr_raw = self._extract_hash_from_text(arg_inner, 'headers') \
                   or self._extract_hash_from_text(arg_inner, 'header')
            if hdr_raw is not None:
                if isinstance(hdr_raw, str) and hdr_raw.startswith('{'):
                    headers = self._extract_hash_pairs(hdr_raw)
                elif isinstance(hdr_raw, str):
                    for hm in re.finditer(r'\$' + re.escape(hdr_raw) + r'\s*=\s*\{', pre_context):
                        hash_str = self._extract_balanced_braces(pre_context, hm.end() - 1)
                        if hash_str:
                            headers = self._extract_hash_pairs(hash_str)
            results.append({
                'has_request': True,
                'method': method,
                'host': host,
                'path': path,
                'script_name': None,
                'query_params': query_params,
                'body_params': {},
                'headers': headers,
            })

        # Also handle http_delete(), http_get(), http_put(), http_post(), http_patch().
        # These use a single `url:` key with the full URL instead of separate host/href,
        # and the verb is implied by the function name rather than a `verb:` key.
        HTTP_VERB_FUNCS = {
            'http_delete': 'DELETE',
            'http_get': 'GET',
            'http_put': 'PUT',
            'http_post': 'POST',
            'http_patch': 'PATCH',
        }
        for func_name, verb in HTTP_VERB_FUNCS.items():
            search_pos = 0
            func_call = func_name + '('
            while True:
                idx = define_body.find(func_call, search_pos)
                if idx == -1:
                    break
                pre_context = define_body[:idx]
                arg_str, end_pos = self._extract_balanced_parens(define_body, idx + len(func_name))
                search_pos = end_pos
                arg_inner = arg_str.strip()
                if arg_inner.startswith('{') and arg_inner.endswith('}'):
                    arg_inner = arg_inner[1:-1]
                # When the entire argument is a single variable, look up its hash definition
                # and extract the url: from there.
                single_var_m = re.match(r'^\s*\$(\w+)\s*$', arg_inner)
                if single_var_m:
                    var_name = single_var_m.group(1)
                    brace_m = None
                    for bm in re.finditer(r'\$' + re.escape(var_name) + r'\s*=\s*\{', pre_context):
                        brace_m = bm
                    if brace_m is None:
                        continue
                    hash_str = self._extract_balanced_braces(pre_context, brace_m.end() - 1)
                    if hash_str is None:
                        continue
                    arg_inner = hash_str[1:-1]
                # Extract URL
                url_m = re.search(r'\burl\s*:\s*(.+)', arg_inner)
                host = None
                path = '/'
                if url_m:
                    url_val = url_m.group(1).strip().split('\n')[0].rstrip(',').strip()
                    resolved_url = self._resolve_define_variable(url_val, pre_context)
                    if resolved_url and 'http' in resolved_url:
                        full_url = resolved_url if resolved_url.startswith('http') else 'https://' + resolved_url
                        parsed = urllib.parse.urlparse(full_url)
                        host = parsed.netloc
                        path = parsed.path or '/'
                        # urlparse may fold a {dynamic} suffix into the netloc when there is
                        # no slash between the hostname and the placeholder (e.g. from a
                        # string concatenation like "https://" + endpoint + arm_id + "?...").
                        # Detect this and move the placeholder into the path instead.
                        if '{dynamic}' in host:
                            host, _, suffix = host.partition('{dynamic}')
                            path = '/{dynamic}' + suffix + path
                    else:
                        # Can't resolve URL — look for host hints in the surrounding context
                        url_hint = re.search(r'https?://([^\s/\'"]+)', pre_context)
                        if url_hint:
                            host = url_hint.group(1)
                if not host:
                    continue
                headers = {}
                hdr_raw = self._extract_hash_from_text(arg_inner, 'headers') \
                       or self._extract_hash_from_text(arg_inner, 'header')
                if hdr_raw is not None and isinstance(hdr_raw, str) and hdr_raw.startswith('{'):
                    headers = self._extract_hash_pairs(hdr_raw)
                results.append({
                    'has_request': True,
                    'method': verb,
                    'host': host,
                    'path': path,
                    'script_name': None,
                    'query_params': {},
                    'body_params': {},
                    'headers': headers,
                })

        return results

    def extract_api_calls(self):
        """Extract all API calls from the policy template."""
        api_calls = []
        
        datasources = self._extract_datasources()

        # Build Azure resource type map for datasources using {id}-prefixed paths
        azure_type_map = self._build_azure_iter_resource_type_map(datasources)
        
        for datasource in datasources:
            request_info = self._extract_request_info(datasource['body'])
            
            if not request_info['has_request']:
                continue
            
            # If request uses a script, extract info from the script
            if request_info['script_name']:
                script_request = self._extract_request_from_script(request_info['script_name'])
                if script_request:
                    # Merge script request info
                    if script_request['host']:
                        request_info['host'] = script_request['host']
                    if script_request['path']:
                        request_info['path'] = script_request['path']
                    if script_request['method']:
                        request_info['method'] = script_request['method']
                    if script_request['query_params']:
                        request_info['query_params'].update(script_request['query_params'])
                    if script_request.get('body_params'):
                        request_info['body_params'] = script_request['body_params']
                    if script_request.get('headers'):
                        request_info['headers'].update(script_request['headers'])

            # Fix {id}/{resourceID}-prefix paths for Azure datasources by resolving
            # the resource type from the iterate chain
            path = request_info.get('path', '')
            if (path.startswith('{id}') or path.startswith('{resourceID}')) and datasource['name'] in azure_type_map:
                resource_type = azure_type_map[datasource['name']]
                suffix = path[path.index('}') + 1:]
                request_info['path'] = f'/providers/{resource_type}/{{id}}{suffix}'
            
            # Process all API calls (not just cloud providers)
            if request_info['host']:
                # Determine which service this API call targets
                api_service = self._determine_api_service(request_info['host'])
                
                # Extract fields from the response
                fields = self._extract_fields(datasource['body'])
                
                # Also extract fields from processing scripts
                processing_fields = self._extract_fields_from_processing_script(datasource['body'])
                fields.extend(processing_fields)
                
                # Deduplicate fields while preserving order
                seen = set()
                unique_fields = []
                for field in fields:
                    if field not in seen:
                        unique_fields.append(field)
                        seen.add(field)
                
                # Build the endpoint URL
                endpoint = self._build_endpoint_url(request_info)

                # Extract operation name
                operation = self._extract_operation_name(endpoint, request_info['method'], api_service, request_info)

                # Derive the cloud provider IAM permission for this API call
                permission = self._derive_permission(endpoint, request_info['method'], api_service, request_info, operation)

                if endpoint:
                    # If no fields found, add at least one entry for the API call
                    if not unique_fields:
                        api_calls.append({
                            'policy_name': self.policy_name,
                            'datasource_name': datasource['name'],
                            'method': request_info['method'],
                            'endpoint': endpoint,
                            'operation': operation,
                            'permission': permission,
                            'field': '{entire response}',
                            'api_service': api_service
                        })
                    else:
                        # Add one entry per field
                        for field in unique_fields:
                            api_calls.append({
                                'policy_name': self.policy_name,
                                'datasource_name': datasource['name'],
                                'method': request_info['method'],
                                'endpoint': endpoint,
                                'operation': operation,
                                'permission': permission,
                                'field': field,
                                'api_service': api_service
                            })

        # Process define blocks (remediation and action API calls)
        define_blocks = self._extract_define_blocks()
        # Build the set of primary Azure resource types once per policy (used for
        # permission fallback when define blocks operate on dynamic ARM resource IDs).
        _azure_resource_types_cache = None

        for define_block in define_blocks:
            http_requests = self._extract_http_requests_from_define(
                define_block['name'], define_block['body']
            )
            for request_info in http_requests:
                if not request_info.get('host'):
                    continue
                api_service = self._determine_api_service(request_info['host'])
                endpoint = self._build_endpoint_url(request_info)
                operation = self._extract_operation_name(
                    endpoint, request_info['method'], api_service, request_info
                )
                permission = self._derive_permission(
                    endpoint, request_info['method'], api_service, request_info, operation
                )
                # For Azure define blocks that use a dynamic ARM resource ID as the
                # href (represented as /{id} in the endpoint), try to derive the
                # permission from the policy's datasource resource types when the
                # normal derivation returned empty.
                if not permission and api_service == 'Azure' and endpoint:
                    parsed_path = urllib.parse.urlparse(endpoint).path
                    # Only attempt when the path is a bare placeholder (no provider type).
                    # Accept both {id} and {dynamic} placeholder forms, with or without
                    # trailing slash, since URL-construction code in CWF policies may
                    # produce either variant.
                    BARE_PLACEHOLDER_PATHS = ('/', '/{id}', '/{id}/', '/{dynamic}', '/{dynamic}/')
                    if parsed_path in BARE_PLACEHOLDER_PATHS:
                        if _azure_resource_types_cache is None:
                            _azure_resource_types_cache = self._get_azure_provider_resource_types()
                        if len(_azure_resource_types_cache) == 1:
                            resource_type = next(iter(_azure_resource_types_cache))
                            method_to_action = {
                                'GET': 'read', 'POST': 'action',
                                'PUT': 'write', 'PATCH': 'write', 'DELETE': 'delete',
                            }
                            action = method_to_action.get(
                                request_info['method'].upper(), 'action'
                            )
                            permission = f'{resource_type}/{action}'
                if endpoint:
                    api_calls.append({
                        'policy_name': self.policy_name,
                        'datasource_name': f'define:{define_block["name"]}',
                        'method': request_info['method'],
                        'endpoint': endpoint,
                        'operation': operation,
                        'permission': permission,
                        'field': '{action}',
                        'api_service': api_service
                    })
                    # compute.disks.createSnapshot requires a companion IAM permission on
                    # the snapshot resource that will be created.  Emit a second record so
                    # the simulation and Dangerfile test can find both permissions.
                    if permission == 'compute.disks.createSnapshot':
                        api_calls.append({
                            'policy_name': self.policy_name,
                            'datasource_name': f'define:{define_block["name"]}',
                            'method': request_info['method'],
                            'endpoint': endpoint,
                            'operation': operation,
                            'permission': 'compute.snapshots.create',
                            'field': '{action}',
                            'api_service': api_service
                        })

        return api_calls


def main():
    """Main function to run the script."""
    arg_parser = argparse.ArgumentParser(
        description='Extract REST API calls and permissions from Flexera Policy Templates.'
    )
    arg_parser.add_argument(
        '--output-dir',
        metavar='DIR',
        default=None,
        help='Write output files to DIR instead of the default data/policy_api_list/ directory.'
    )
    args = arg_parser.parse_args()

    # Get the repository root directory (two levels up from script location)
    script_path = Path(__file__).resolve() if '__file__' in globals() else Path.cwd()
    repo_root = script_path.parent.parent.parent if '__file__' in globals() else Path.cwd()
    
    # Path to active policy list
    active_policy_list_file = repo_root / 'data' / 'active_policy_list' / 'active_policy_list.json'
    
    if not active_policy_list_file.exists():
        print(f"Error: Active policy list not found: {active_policy_list_file}", file=sys.stderr)
        sys.exit(1)
    
    # Load active policy list
    with open(active_policy_list_file, 'r') as f:
        active_policies = json.load(f)
    
    policies = active_policies.get('policies', [])
    if not policies:
        print("Error: No policies found in active_policy_list.json", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing {len(policies)} policy templates...")

    # Load permission lookup tables once before processing all files
    PolicyTemplateParser.set_repo_root(repo_root)

    # Collect all API calls
    all_api_calls = []
    processed_count = 0
    error_count = 0
    
    for policy_info in policies:
        policy_file = repo_root / policy_info['file_name']
        
        # Skip meta parent policies
        if '_meta_parent.pt' in str(policy_file):
            continue
        
        if not policy_file.exists():
            print(f"Warning: Policy file not found: {policy_file}", file=sys.stderr)
            error_count += 1
            continue
        
        try:
            # Parse the policy template
            parser = PolicyTemplateParser(str(policy_file))
            api_calls = parser.extract_api_calls()
            
            # Add policy metadata to each API call
            for call in api_calls:
                call['policy_file'] = policy_info['file_name']
                call['policy_version'] = policy_info.get('version', '')
            
            all_api_calls.extend(api_calls)
            processed_count += 1
            
            if processed_count % 50 == 0:
                print(f"  Processed {processed_count}/{len(policies)} policies...")
        
        except Exception as e:
            print(f"Error processing {policy_file}: {e}", file=sys.stderr)
            error_count += 1
    
    print(f"\nProcessed {processed_count} policies successfully, {error_count} errors")
    print(f"Extracted {len(all_api_calls)} total API call fields")
    
    # Create output directory if it doesn't exist
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = repo_root / 'data' / 'policy_api_list'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write to JSON
    json_output_file = output_dir / 'policy_api_list.json'
    with open(json_output_file, 'w') as f:
        json.dump({
            'api_calls': all_api_calls
        }, f, indent=2)
    
    print(f"JSON output written to: {json_output_file}")
    
    # Write to CSV
    csv_output_file = output_dir / 'policy_api_list.csv'
    with open(csv_output_file, 'w', newline='') as csvfile:
        fieldnames = ['policy_name', 'policy_file', 'policy_version', 'datasource_name', 'api_service', 'method', 'endpoint', 'operation', 'permission', 'field']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for call in all_api_calls:
            writer.writerow(call)
    
    print(f"CSV output written to: {csv_output_file}")


if __name__ == '__main__':
    main()
