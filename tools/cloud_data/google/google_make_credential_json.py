#!/usr/bin/env python3
"""
Creates a GCP credential JSON file from the GOOGLE_AUTH_JSON environment variable.

This script is intended for use in GitHub Actions workflows where GCP credentials
are stored as an Actions secret (GOOGLE_AUTH_JSON) and need to be written to a
file referenced by GOOGLE_APPLICATION_CREDENTIALS.

Usage: python3 google_make_credential_json.py
"""

import os
import json
import sys


def main():
    output_filename = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    auth_json = os.getenv("GOOGLE_AUTH_JSON")

    # Both env vars must be set and non-empty for this script to work
    if not output_filename:
        print("ERROR: GOOGLE_APPLICATION_CREDENTIALS environment variable is not set or empty.")
        sys.exit(1)

    if not auth_json:
        print("ERROR: GOOGLE_AUTH_JSON environment variable is not set or empty.")
        sys.exit(1)

    # Create the directory if it doesn't exist
    output_dir = os.path.dirname(output_filename)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Store JSON from environment variable in local file
    with open(output_filename, "w") as type_file:
        type_file.write(auth_json)


if __name__ == "__main__":
    main()
