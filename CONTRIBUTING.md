# Contribution Guide

The Flexera Policy Template Catalog is an open source project under the MIT license. Contributions from outside of the Flexera organization are accepted but will undergo peer review by the Flexera team.

## Branches

The `master` branch is the primary branch of the repository, and the branch that is used to populate the Flexera Policy Template Catalog within Flexera One. Other branches should only be created with the intent of merging them into `master`.

## Contribution Flow

### 1. Create a Branch

All contribution work should be done in its own branch. Once you have cloned the repository locally, make a branch for your work and switch to it. If you are a Flexera employee, include the JIRA ticket number in the name of your branch along with a description of the work. _Example_: `POL-1522-style-guide`

### 2. Make Changes

Make the needed changes within the branch, test your work, etc. Once the work is complete and you're ready to move it into the `master` branch, move on to the next step.

### 3. Make a Pull Request

The title of your pull request should include a general description of the change being made. If you are a Flexera employee, include the ticket number at the start of the title. _Example_: `POL-1522 Style Guide`

The description should contain a detailed description of the pull request, including any testing you did to verify that the changes work as intended.

The `READY-FOR-REVIEW` tag should be added to any pull request that you believe is complete and ready to be merged into the `master` branch.

### 4. Fix Merge Conflicts

If any merge conflicts appear, please resolve these before moving on to the next step. The pull request cannot be merged until any conflicts are resolved.

### 5. Fix Dangerfile Issues

This repository uses Dangerfile to perform automated testing. A few minutes after making your pull request, any problems detected by Dangerfile should appear as comments on the pull request. Fix these issues and push your fixes to your working branch.

Dangerfile will occasionally have false positives or fail to account for some nuance in implementation. In these cases, add a comment to the description explaining why the failed test is not a concern.

### 6. Fix Peer Review Issues

In order to merge your branch, a Flexera policy template developer will need to approve your pull request. During the review process, they may request changes.

When this happens, correct any reported issues, or engage in conversation around things you believe do not need to be changed via comments, and then request another review.

### 7. Merge Branch

Once your pull request has been approved, please merge it into the `master` branch. Once the merge is complete, your working branch will automatically be deleted.
