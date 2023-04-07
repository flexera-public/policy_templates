# Policy Template README Table of Contents

## Generate README Table of Contents

The [Generate README Table of Contents](https://github.com/flexera-public/policy_templates/actions/workflows/generate-readme-policy-table-of-contents.yaml) GitHub Actions Workflow is triggered anytime there is a push to the default branch and will create a pull request with the updated README Table of Contents.

At this time, the pull request will need to be manually approved and merged but this behavior can be changed by updating the workflow.

The workflow can also be triggered manually in case there is an unexpected failure and the push trigger is not working.

Here are the manual steps to generate the README Table of Contents which should be the same / very similar to [Generate README Table of Contents](https://github.com/flexera-public/policy_templates/actions/workflows/generate-readme-policy-table-of-contents.yaml):

```sh
# Run script from root of repo
# Ignore warnings for `character class has '-' without escape`
ruby tools/readme_policy_table_of_contents/generate_readme_policy_table_of_contents.rb > TOC.tmp.md
# Use awk to update section in README with generated TOC
awk '
    BEGIN       {p=1}
    /^<!-- Begin Policy Template Table of Contents -->/   {print;system("cat TOC.tmp.md");p=0}
    /^<!-- End Policy Template Table of Contents -->/     {p=1}
    p' README.md > README.tmp.md
# Replace README.md with updated README.tmp.md
cp README.tmp.md README.md
# Cleanup
rm README.tmp.md TOC.tmp.md
```
