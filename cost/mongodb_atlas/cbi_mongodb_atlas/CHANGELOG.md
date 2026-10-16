# Changelog

## v1.0.0

- The policy template now creates the CBI endpoint (bill connect) automatically if it does not already exist, using the cloud vendor name `MongoDB Atlas`. Previously, the CBI endpoint had to be created in advance.
- Creating a CBI endpoint requires the `org_owner` role on the Flexera credential. The role is not required if the CBI endpoint already exists. See the README for details.

## v0.1.0

- Initial release
