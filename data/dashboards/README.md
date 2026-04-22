# Dashboards

This directory contains manually-maintained JSON files defining FinOps dashboard configurations for use in the Flexera platform.

## Manually Maintained Files

Each JSON file in this directory defines a single dashboard. Files follow a consistent structure with a `name` string and a `config` object containing the full dashboard definition.

**Structure:** Object with two top-level keys.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Human-readable dashboard name as displayed in the Flexera UI |
| `config` | object | Full dashboard configuration object (see below) |

The `config` object contains the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `description` | string | Dashboard description |
| `layoutId` | string | Layout identifier for the dashboard grid |
| `layouts` | array | Array of layout configuration objects |
| `version` | string | Dashboard schema version |
| `widgets` | array | Array of widget definition objects that make up the dashboard |

**Example:**

```json
{
  "name": "FinOps - Executive Summary",
  "config": {
    "description": "High-level cloud spend summary for executive stakeholders.",
    "layoutId": "grid-2col",
    "layouts": [],
    "version": "1.0",
    "widgets": []
  }
}
```

## Files

| File | Dashboard Name |
| --- | --- |
| [finops_business_product.json](finops_business_product.json) | FinOps - Business / Product Owner |
| [finops_engineering_operations.json](finops_engineering_operations.json) | FinOps - Engineering / Operations |
| [finops_executive_summary.json](finops_executive_summary.json) | FinOps - Executive Summary |
| [finops_finance_procurement.json](finops_finance_procurement.json) | FinOps - Finance & Procurement |
| [finops_global_cio_ytd_view.json](finops_global_cio_ytd_view.json) | FinOps - Global CIO YTD View |
| [finops_marketplace.json](finops_marketplace.json) | FinOps - Marketplace / Operating System Overview |
| [finops_reservation_coverage.json](finops_reservation_coverage.json) | FinOps - Reservation Coverage |
| [finops_reservation_management.json](finops_reservation_management.json) | FinOps - Reservation Management |
