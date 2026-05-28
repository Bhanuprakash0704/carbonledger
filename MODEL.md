# CarbonLedger Data Model

## Overview

CarbonLedger is designed as a multi-tenant ESG emissions ingestion and analyst review platform.
The system ingests emissions-related operational data from multiple enterprise sources such as SAP exports, utility electricity reports, and corporate travel systems.

The data model prioritizes:

* multi-tenancy
* auditability
* source provenance
* normalization
* analyst review workflows
* realistic enterprise ingestion patterns

---

# Core Entities

## 1. Tenant

Represents a company or organization using the platform.

### Why this entity exists

The platform is designed as a multi-tenant SaaS-style system where multiple companies can upload and review emissions data independently.

### Fields

| Field        | Purpose              |
| ------------ | -------------------- |
| company_name | Name of organization |
| created_at   | Audit timestamp      |

### Design Notes

Every uploaded source and emission record belongs to a tenant to ensure logical isolation between organizations.

---

# 2. Source

Represents an ingestion event or uploaded source file.

Examples:

* SAP fuel export CSV
* utility electricity report
* travel expense export

### Why this entity exists

In ESG systems, preserving source provenance is critical for auditability.

Analysts must know:

* where data came from
* when it was uploaded
* what system produced it

### Fields

| Field       | Purpose                    |
| ----------- | -------------------------- |
| tenant      | Owner organization         |
| source_type | sap / utility / travel     |
| file_name   | Original uploaded filename |
| uploaded_at | Upload timestamp           |

### Design Notes

The Source model acts as a source-of-truth tracking layer.
Each emission record can be traced back to the exact uploaded file that generated it.

This becomes important during:

* ESG audits
* reconciliation
* analyst review
* ingestion debugging

---

# 3. EmissionRecord

Represents a normalized emissions-related operational row.

Examples:

* diesel fuel purchase
* electricity consumption
* flight travel segment

### Why this entity exists

Raw enterprise exports are inconsistent and difficult to analyze directly.

The EmissionRecord model provides:

* normalized analytical fields
* review workflow state
* suspicious record detection
* audit tracking

---

# EmissionRecord Fields

| Field               | Purpose                       |
| ------------------- | ----------------------------- |
| tenant              | Organization ownership        |
| source              | Source provenance tracking    |
| category            | Fuel / Electricity / Travel   |
| scope               | ESG Scope 1 / 2 / 3           |
| quantity            | Original quantity from source |
| unit                | Original unit                 |
| normalized_quantity | Standardized quantity         |
| normalized_unit     | Standardized unit             |
| co2e                | Calculated emissions value    |
| suspicious          | Flag for analyst review       |
| status              | Review workflow state         |
| raw_data            | Original source payload       |
| edited_by_analyst   | Tracks analyst modification   |
| created_at          | Audit timestamp               |

---

# Scope Classification

The platform uses simplified ESG scope mapping:

| Scope   | Meaning                        | Example             |
| ------- | ------------------------------ | ------------------- |
| Scope 1 | Direct emissions               | Fuel combustion     |
| Scope 2 | Purchased electricity          | Utility electricity |
| Scope 3 | Indirect operational emissions | Business travel     |

---

# Normalization Strategy

Enterprise exports contain inconsistent units and formats.

Examples:

* liters vs gallons
* localized SAP exports
* inconsistent date formats

The platform stores:

* original values
* normalized analytical values

This preserves:

* auditability
* traceability
* analytical consistency

---

# Suspicious Record Detection

Certain records are automatically flagged as suspicious.

Current implemented checks:

* negative quantities
* invalid calculated emissions

These flags support analyst review workflows before records are approved or locked.

---

# Review Workflow

Emission records move through multiple states:

| Status   | Meaning                 |
| -------- | ----------------------- |
| pending  | Awaiting analyst review |
| approved | Accepted by analyst     |
| rejected | Invalid data            |
| locked   | Finalized for audit     |

This workflow models realistic ESG governance processes.

---

# Auditability Design

The model prioritizes traceability and audit readiness through:

* source provenance tracking
* immutable timestamps
* raw source payload storage
* analyst modification tracking
* workflow statuses

This design supports future ESG audit and compliance requirements.

---

# Multi-Tenancy Design

All major entities are tenant-scoped.

Benefits:

* organizational isolation
* scalability
* SaaS deployment readiness
* future role-based access support

---

# Future Improvements

Potential future extensions:

* emission factor versioning
* facility-level hierarchy
* asynchronous ingestion jobs
* OCR utility bill parsing
* external ERP integrations
* approval history tracking
* analyst comments
* row-level lineage graphs

These were intentionally deferred to keep the MVP focused on ingestion, normalization, and analyst review workflows.
