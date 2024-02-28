# Flexera CCO Delete All Billing Centers

## What It Does

This policy deletes all Billing Centers in the Flexera organization it is executed within. The policy will automatically self-terminate the second time it runs to avoid accidental future deletion of Billing Centers.

## How It Works

- During execution, the policy determines if this is the second time it has run since it was applied by comparing the applied policy's `created_at` date/time with the current date/time. If the difference between the two is greater than 1 minute, it is assumed the policy is running a second time.
- If this is the policy's second time running, the policy self-terminates before completing execution as a failsafe in case the user has forgotten to terminate the policy after usage.
- An incident is always raised, with the `Self Terminate` field in the incident table being true if this is the policy's second time executing since it was applied.
- Cloud Workflow is automatically kicked off.
  - If this is the policy's second time executing, but for some reason the policy has failed to self-terminate, no action will be taken.
  - If this is the policy's first time executing, all of the Billing Centers in the Flexera organization are deleted.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_admin`
  - `policy_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
