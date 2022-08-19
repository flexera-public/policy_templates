# Currency Conversion

## What it does

This Policy creates an adjustment rule that converts the currency of the cost associated with the Cloud Vendor of choice. It utilizes xe.com to retrieve the latest exchange rates.

## Functional Details

- This policy supports currency codes as per [ISO 4217](https://www.xe.com/iso4217.php), and uses the xe.com API to retrieve monthly average exchange rate.
- This policy requires an API credential added to the tenant to use the xe.com API.
- This policy supports three cloud providers: AWS, Azure and Google Cloud.
- This policy creates an adjustment rule for currency conversion using the exchange rate from xe.com.
- This policy can be customized to suit user requirements, such as supporting vendors other than AWS, Azure and GCP.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Cloud provider* - Cloud provider costs that you want to apply currency conversion to
- *Currency From* - Currency you want to convert from (based on ISO 4217 codes - e.g., 'USD' for US Dollar)
- *Currency To* - Currency you want to convert to (based on ISO 4217 codes - e.g., 'EUR' for Euro)
- *Email addresses* - A list of email addresses to notify

## Supported Clouds

- All configured clouds

## Cost

This Policy Template does not incur any cloud costs.
