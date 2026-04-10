# Flexera Data

This directory contains manually-maintained reference data for the Flexera platform.

- [iam_roles.json](iam_roles.json) - A JSON array of Flexera platform IAM role definitions. Each entry includes a `name` (role identifier), `category` (grouping category), and `displayName` (human-readable name). The file contains 54 roles across the following categories: Automation, Cloud, Data and Analytics, Discovery and Inventory, IT Visibility, Other, Platform Administration, SCA Data Library, Self-service CloudApps, Software Bill Of Materials, and Technology Spend. This file is used by policy templates and tooling that need to validate or reference Flexera IAM role definitions.
