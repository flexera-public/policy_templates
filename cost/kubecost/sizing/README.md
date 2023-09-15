# Kubecost Request Rightsizing Recommendations Policy Template

## What it does

Kubecost request sizing recommendations policy provides Kubecost recommendations for container resource requests along with estimated savings.

## Functional Details

- The policy requests recommendations for request right-sizing based on parameters provided.
- The [container request right sizing recommendation API](https://docs.kubecost.com/apis/apis-overview/api-request-right-sizing-v2) provides recommendations for container resource requests based on configurable parameters and estimates the savings from implementing those recommendations on a per-container, per-controller level. Of course, if the cluster-level resources stay static then you will likely not enjoy real savings from applying these recommendations until you reduce your cluster resources. Instead, your idle allocation will increase.

### Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Kubecost Host or IP address* - The host or IP Address where your Kubecost runs
- *Scope* - The scope used to request savings recommendations: "overall" or "per cluster"
- *Monthly Savings Threshold* - Specify the minimum estimated monthly savings that should result in a recommendation
  - Default: 5
  - Minimum value: 1
- *Window size* - Time range to analyze. Supports hours or days before the current time in the following format: 2h or 3d
  - Default: "3d"
- *The algorithm for the CPU* - Defines whether max or a certain quantile should be used for CPU utilization metric to compute CPU request recommendation
  - Default: "max"
  - Allowed values: "max", "quantile"
- *CPU percentile* - The desired percentile to base CPU request recommendations on
  - Default: 75
  - Minimum value: 1
  - Maximum value: 100
- *Target CPU Utilization (%)* - Target CPU utilization in percent
  - Default: 80
  - Minimum value: 1
  - Maximum value: 100
- *The algorithm for Memory* - Defines whether max or a certain quantile should be used for Memory utilization metric to compute Memory request recommendation
  - Default: "max"
  - Allowed values: "max", "quantile"
- *Memory percentile* - The desired percentile to base Memory request recommendations on
  - Default: 75
  - Minimum value: 1
  - Maximum value: 100
- *Target Memory Utilization (%)* - Target memory utilization in percent
  - Default: 90
  - Minimum value: 1
  - Maximum value: 100

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
