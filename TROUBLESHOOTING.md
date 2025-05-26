# Troubleshooting Guide

In the event that a policy template in this repository is not working as expected, please do the following before submitting an Issue or contacting Flexera support.

## 1. Verify Policy Template Version

As bugs and problems are identified with policy templates, they are updated with fixes. These fixes are then pushed to the catalog in Flexera One. For this reason, it's important to verify that you're using the latest version of a policy template when you run into issues.

The simplest way to do this is to apply the [Flexera Automation Outdated Applied Policies](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/outdated_applied_policies) policy template. This will report if any of your applied policies are on old versions.

If you are using an older version of a policy template, terminate it and apply the current version. If the issue persists, move on to the next step.

## 2. Verify Valid Credentials

Many issues can be caused if incorrect credentials were selected when applying the policy template, or if credentials have expired or modified such that they no longer have the necessary access.

The README file for the policy template will have a list of credentials required for the policy template to work correctly along with all of the permissions/access that these credentials need. Verify that each credential selected is the correct credential and that the credential has the required access.

Note that there is a known issue with credentials sometimes not working as expected in the Flexera platform if they have been in place for a long time. In these cases, simply editing the credential in Flexera One and then clicking the "Verify" button without changing anything may be enough to fix the issue.

## 3. Verify Correct Parameter Settings

Many policy templates have settings that can be configured by the end user, and some of these settings can be set incorrectly and cause a policy template to fail. Ensure all settings are set as intended; in particular, settings that reference file names, object storage buckets, etc. should be double-checked to ensure that they are correct.

## 4. Review The Error Message

If the issue persists, review the error message itself to see if an explanation is available there. Often, the error message will tell you exactly what went wrong. Some common errors and their likely causes are below:

- __404 Not Found__ - This can often indicate that one of the policy template's parameters is incorrectly configured. It is recommended that you go back to step 3 and double check those values.

- __422 Unprocessable Entity__ / __signing failed__ - This is commonly caused by stale credentials in the Flexera platform. In these cases, simply editing the offending credential in Flexera One and then clicking the "Verify" button without changing anything may be enough to fix the issue.

- __Access__ - If the error contains one of the below words, you likely have an issue with one of your credentials and should go back to step 2.
  - Authentication / Unauthenticated
  - Authorization / Unauthorized
  - Access
  - Permission
  - Rights

- __Time Exceeded__ - Policy templates have a hard 60 minute limit on how long they can run before timing out. Individual scrips within policy templates have a limit of 30 minutes. If you are running into one of the below errors, reduce the scope of the policy template by making use of parameters to filter as needed, or make use of [Meta Policies](https://github.com/flexera-public/policy_templates/blob/master/README_META_POLICIES.md).
  - Policy evaluation exceeded maximum time
  - script execution exceeded 3600s

- __ReferenceError__ / __TypeError__ - If the error mentions "ReferenceError" or "TypeError", this likely indicates a bug in the policy template itself. Please raise an [Issue](https://github.com/flexera-public/policy_templates/issues) and include as much detail as you can.

## 5. Contact Support

If after going through the above steps, you're not able to identify and resolve the issue, it is recommended that you reach out to support via the [Flexera Community](https://community.flexera.com).
