# Configure Custom Branding

## What It Does

This policy template allows a customer to apply their own branding to the FlexeraOne platform quickly and consistently.

## How It Works

- Apply the custom branding policy template in the tenant ensuring you select the credentials required.
- For non MSP Customers you can only apply the All Customer Settings Category.
- For MSP Customers you can apply the All Customer Settings Category and the MSP Specific Settings Category.
- Select the areas that require branding changes by either selecting Yes/No for show/hide features, or, entering a URL to Images or Links or text to replace existing text.
- If there are items that do not need to be changed, leave the defaults of either No or blank and it will be ignored.
- Apply the policy template and review if there are any errors, an incident will be generated if an item fails.
- After the policy template has been applied and changes are in effect, it is recommended to terminate the applied policy.

## Input Parameters

This policy template has the following input parameters required when being applied.

### Applies to whole policy (Optional)

- *Email Addresses* - A list of email addresses to notify

### Category : All Customer Settings

- *Nav Logo Image* - The URL of the image file to use in place of the Flexera logo that displays in the app navigation’s expanded state. Must start with http : // or https : //
- *Nav Logo Small image* - The URL of the image file to use in place of the small Flexera logo that displays in the app navigation’s collapsed state. Must start with http : // or https : //
- *Marketing Footer Hide* - Yes or No to show/hide the marketing footer on the landing page. (Default is No)
- *Marketing Submit Ideas Hide* - Yes or No to show/hide the Submit Ideas link on the landing page. (Default is No)
- *Marketing Support Plan Hide* - Yes or No to show/hide the Support Plan Information link on the landing page. (Default is No)
- *Marketing Open New Case Link* - A URL to be used for the Open New Case link on the landing page. Must start with http : // or https : //
- *Marketing flexera com hide* - Yes or No to show/hide the Flexera.com link on the landing page. (Default is No)
- *Marketing Support Help Link* - A URL to be used for your own Support Help link on the landing page. Must start with http : // or https : //

### Category : MSP Specific Settings

- *Login Logo Image* - The URL of the image file location to use in place of the Flexera logo on the login page. Must start with http  :// or https  ://
- *Global Customer Support Link* - A URL to use for your own Customer Support link on the login page. Must start with http : // or https : //
- *Marketing Login Image* - The URL of the image file to use in place of the Flexera marketing section on the login page. Must start with http : // or https : //
- *Marketing Login CTA Link* - A URL to use for the Download Now button action on the login page. Must start with http : // or https : //
- *Marketing Login CTA text* - Text to change the Download Now button text displayed on the login page.
- *Marketing Login Eyebrow Text* - Text to use for the eyebrow marketing text on the login page.
- *Marketing Login Blurb Text* - Text to use for the marketing blurb on the login page.
- *Marketing Login Title Text* - Text to use for the marketing title text on the login page.

The [Partner MSP Customizations](https://docs.flexera.com/flexera/EN/Administration/PartnerMSPCustomizations.htm) page in our documents has detailed information on the settings and diagrams for custom branding

## Policy Actions

The following policy actions are taken when branding fails.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `manage_organization`*

  \* Required for taking branding actions.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally a subdomain needs to be configured to ensure that the branding of the Flexera login page takes effect as outlined in the [Partner MSP Customizations](https://docs.flexera.com/flexera/EN/Administration/PartnerMSPCustomizations.htm) documentation. Otherwise the policy template will only allow the tenant to update the landing page.

## Supported Clouds

Not Applicable

## Cost

This policy template does not incur any cloud costs.
