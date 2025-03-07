# Meta Parent: Google Credential

## What It Does

This meta parent policy template reports the status of an Google credential via a single child policy. A meta parent is necessary because the child policy may fail to complete execution, and therefore not raise an incident, if there is a problem with the Google credential.

The credential will be reported as having one of the three following statuses:

- *Passed* - The child applied policy was able to successfully make a "projects.list" REST API request to the Google Cloud Resource Manager API.
- *Failed* - Either the child applied policy was *not* able to successfully make a "projects.list" REST API request to the Google Cloud Resource Manager API, or the request did not return any Google Projects.
- *Unknown* - The child applied policy has not yet been created or completed execution, and as a result, the status of the Google credential is unknown. This is most commonly seen soon after applying the meta parent policy and should mostly disappear after 24 hours.

__NOTE: This meta parent policy template is not automatically generated and is customized for this specific use case. It needs to be manually updated and maintained whenever the child policy template is updated.__
