# Architectural and Product Decisions

This document captures major implementation decisions, assumptions, simplifications, and tradeoffs made during development of CarbonLedger.

---

# 1. SAP Ingestion Format Choice

## Decision

I chose CSV-style SAP exports as the primary SAP ingestion format.

## Why

Real SAP environments expose multiple integration methods:

* IDoc
* BAPI
* OData services
* flat-file exports

For this assignment, CSV exports were selected because:

* they are common in operational finance workflows
* analysts frequently export SAP reports manually
* CSV ingestion allowed realistic handling of inconsistent enterprise data without implementing full SAP connectivity

## Assumptions

The implemented SAP export contains:

* fuel procurement rows
* quantity and unit columns
* plant/location identifiers
* inconsistent units

---

# 2. Utility Data Handling

## Decision

I modeled utility ingestion as CSV portal exports rather than PDF parsing or direct APIs.

## Why

Many facilities teams still receive electricity consumption reports as downloadable CSV or spreadsheet exports from utility portals.

CSV ingestion was selected because:

* it is operationally realistic
* easier to normalize
* avoids OCR complexity
* aligns with analyst-driven workflows

## Deferred Complexity

The following were intentionally not implemented:

* PDF OCR parsing
* tariff breakdown extraction
* interval meter data
* utility API authentication

---

# 3. Corporate Travel Handling

## Decision

Travel data was modeled as exported operational records similar to Concur/Navan exports.

## Why

Real travel systems often expose:

* CSV exports
* expense records
* itinerary exports
* API endpoints

The simplified model focuses on:

* category mapping
* emissions attribution
* Scope 3 classification

## Assumptions

Travel records may contain:

* flights
* hotels
* ground transport

Distance calculations were intentionally simplified.

---

# 4. Multi-Tenancy Design

## Decision

All major entities are tenant-scoped.

## Why

The system was designed as a SaaS-style ESG platform capable of supporting multiple organizations simultaneously.

This enables:

* organizational isolation
* future RBAC support
* scalable architecture

---

# 5. Source Provenance Tracking

## Decision

Emission records reference a Source entity.

## Why

ESG reporting requires strong auditability.

Analysts must know:

* which file created a row
* when it was uploaded
* what ingestion source produced it

This design improves:

* traceability
* debugging
* audit readiness

---

# 6. Normalization Strategy

## Decision

Both raw and normalized values are stored.

## Why

Enterprise operational exports often contain:

* inconsistent units
* localized formatting
* mixed conventions

Storing normalized fields separately preserves:

* original source fidelity
* analytical consistency

---

# 7. Suspicious Record Detection

## Decision

The MVP flags:

* negative quantities
* invalid emission calculations

## Why

The assignment specifically requested surfacing suspicious records for analyst review.

The suspicious flag acts as an initial anomaly detection layer.

## Deferred Complexity

More advanced anomaly detection was intentionally not implemented, such as:

* statistical outlier detection
* duplicate detection
* historical trend validation

---

# 8. Analyst Review Workflow

## Decision

Emission records support workflow states:

* pending
* approved
* rejected
* locked

## Why

The assignment required analyst review before audit locking.

This workflow models realistic governance and ESG review processes.

---

# 9. Frontend Design Choice

## Decision

React + Vite was selected for the frontend.

## Why

This stack provides:

* fast iteration
* lightweight setup
* modern component architecture
* strong developer productivity

The dashboard was intentionally designed to prioritize:

* analyst usability
* upload simplicity
* rapid review workflows

---

# 10. Emission Factor Simplification

## Decision

Emission calculations use simplified static conversion logic.

## Why

The assignment primarily evaluates:

* ingestion realism
* data modeling
* normalization
* analyst workflow design

A full emission-factor engine would significantly increase scope and complexity.

---

# 11. Database Choice

## Decision

SQLite was used for local development.

## Why

SQLite reduced setup complexity for the MVP while remaining fully compatible with Django ORM.

Production deployment could migrate easily to:

* PostgreSQL
* MySQL

---

# 12. What I Would Ask the PM

If product clarification were available, I would ask:

1. What level of ESG reporting accuracy is expected?
2. Should historical emission-factor versioning be supported?
3. Are uploads analyst-driven or automated integrations?
4. What approval hierarchy exists?
5. Is facility-level reporting required?
6. What audit/compliance frameworks must be supported?
7. Should rejected records remain editable?
8. What retention policy exists for raw uploaded files?
