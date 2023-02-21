# Changelog

## v2.4

- adding an input list for a mix of dimensions
- validate each input from the user input list, if all are valid dimensions, it will runs anomaly report. Otherwise when user inputs at least one invalid dimension, policy will stop their processes, escalating to email you invalid/valid dimension you used

## v2.3

- changed URL link to Cost Anomalies report, now it's constructed dynamically based on detected shard

## v2.2

- changed cost metric map key from api call value to more readable value

## v2.1

- changed parameter value for dimensions from "Cloud Vendor Account Name" to "Cloud Vendor Account"
- removed parameter dimension "Operating System" and removed mapping for api call
- changed name from Cloud Cost Anomalies to Cloud Cost Anomaly Alerts

## v2.0

- initial release
