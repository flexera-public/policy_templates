# Custom Branding

## What It Does

This Policy allows a customer to brand the FlexeraOne platform quickly and consistently.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

- A sub domain need to be configured to ensure that the Branding of the logon screen takes effect as outlined in the [Partner MSP Customizations](https://docs.flexera.com/flexera/EN/Administration/PartnerMSPCustomizations.htm) documentation. Otherwise the policy will only allow tenant to update the landing page.

## How It Works

- Run the Custom Branding policy in the tenant ensuring you select the credentials required
- For non MSP Customers you can only apply the All Customer Settings Category
- For MSP Customers you can apply bother All Customer Settings Category and the MSP Specific Settings Category
- Select the areas that require white labelling by either selecting Yes/No for show/hide features, or, entering a URL to Images or Links
- If there are items that do not need to be changed, leave the default text of No Change and it will be ignored
- Run the policy and review if there are any errors, an incident will be generated if an item fails and will tell you which Item has failed and why
- Once run, you should terminate the policy so it does not continue to run

## Input Parameters

This policy has the following input parameters required when launching the policy.

### Applies to whole policy (Optional)

- *Email addresses* - A list of email addresses to notify

### Category : All Customer Settings

- *Nav Logo Image* - The web address of the image resource file location to use in place of the Flexera logo that displays in the app navigation’s expanded state. Must start with http : // or https : //
- *Nav Logo Small image* - The web address of the image resource file location to use in place of the small Flexera logo that displays in the app navigation’s collapsed state. Must start with http : // or https : //
- *Marketing Footer Hide* - A boolean to determine show/hide of the marketing footer on the landing page.
- *Marketing Submit Ideas Hide* - A boolean to determine show/hide of the Submit Ideas link on the landing page.
- *Marketing Support Plan Hide* - A boolean to determine show/hide of the Support Plan Information link on the landing page.
- *Marketing Open New Case Link* - A URL override pointing to your own Open New Case link on the landing page. Must start with http : // or https : //
- *Marketing flexera com hide* - A boolean to determine show/hide of the Flexera.com link on the landing page.
- *Marketing Support Help Link* - A URL override pointing to your own Support Help link on the landing page. Must start with http : // or https : //

### Category : MSP Specific Settings

- *Login Logo Image* - The web address of the image resource file location to use in place of the Flexera logo for unauthenticated pages like login, password reset, and so on. Must start with http  :// or https  ://
- *Global Customer Support Link* - A URL override pointing to your own Customer Support link on the login page and elsewhere throughout the app. Must start with http : // or https : //
- *Marketing Login Image* - The web address of the image resource file location to use in place of the Flexera marketing section on the login page. Must start with http : // or https : //
- *Marketing Login CTA Link* - A URL override pointing to your own Download Now call to action link on the login page. Must start with http : // or https : //
- *Marketing Login CTA text* - Plain text override of the Download Now call to action text displayed on the login page.
- *Marketing Login Eyebrow Text* - Plain text to override of the eyebrow marketing text on the login page.
- *Marketing Login Blurb Text* - Plain text to override of the marketing blurb on the login page.
- *Marketing Login Title Text* - Plain text override of the marketing title text on the login page.

The [Partner MSP Cusotmizations](https://docs.flexera.com/flexera/EN/Administration/PartnerMSPCustomizations.htm) page in the docs has detailed information on the settings and diagrams for custom branding

## Policy Actions

The following policy actions are taken when branding fails.

- Send an email report
- Create an incident

## Cost

This policy template does not incur any cloud costs.
