# Tradeoffs and Deferred Features

This document outlines major features and capabilities intentionally not implemented in the CarbonLedger MVP, along with the reasoning behind those decisions.

The goal of the project was to prioritize:

* realistic ingestion workflows
* normalization
* analyst review functionality
* audit-oriented data modeling

over full enterprise-scale implementation complexity.

---

# 1. Real SAP Integrations Were Not Implemented

## Deferred Features

* SAP OData integration
* IDoc processing
* BAPI connectivity
* live ERP synchronization

## Why

Real SAP integrations require:

* enterprise authentication
* network access
* ERP-specific configuration
* complex middleware handling

For the MVP, CSV-style exports provided a more practical and reviewable implementation while still modeling realistic operational data ingestion patterns.

## Tradeoff

The current implementation prioritizes:

* ingestion realism
* normalization handling
* analyst workflows

instead of enterprise middleware complexity.

---

# 2. Utility PDF Parsing Was Not Implemented

## Deferred Features

* OCR extraction
* PDF bill parsing
* tariff schedule parsing
* interval meter ingestion

## Why

PDF parsing introduces:

* OCR reliability issues
* layout variability
* significantly higher implementation complexity

CSV ingestion was selected as a more deterministic and reviewable ingestion path for the MVP.

## Tradeoff

The platform currently supports structured ingestion rather than document interpretation workflows.

---

# 3. Advanced Emission Factor Engine Was Not Implemented

## Deferred Features

* region-specific emission factors
* factor versioning
* supplier-specific calculations
* external factor databases

## Why

A production-grade emissions engine requires:

* regulatory alignment
* version control
* jurisdiction-specific logic
* external data governance

This complexity was intentionally deferred to focus on:

* ingestion architecture
* normalization workflows
* provenance tracking
* analyst review processes

## Tradeoff

The current implementation uses simplified emission calculations suitable for demonstrating ingestion and analytical workflows.

---

# 4. Authentication and RBAC Were Simplified

## Deferred Features

* role-based access control
* analyst/admin permission separation
* SSO integration
* tenant-level authorization rules

## Why

The assignment prioritized:

* data modeling
* ingestion workflows
* analyst review systems

rather than enterprise identity management.

## Tradeoff

The current implementation focuses on platform workflow functionality over security architecture depth.

---

# 5. Asynchronous Processing Was Not Implemented

## Deferred Features

* Celery workers
* background ingestion queues
* retry pipelines
* ingestion job monitoring

## Why

The current ingestion volume is small enough for synchronous processing during MVP development.

Implementing async infrastructure would significantly increase:

* deployment complexity
* operational overhead
* debugging complexity

## Tradeoff

The current design prioritizes simplicity and reviewer clarity over ingestion scalability.

---

# 6. Historical Change Tracking Was Simplified

## Deferred Features

* field-level audit history
* row versioning
* analyst comment history
* approval lineage

## Why

Basic auditability was implemented through:

* timestamps
* source provenance
* workflow states
* raw payload preservation

A complete audit event system would require significantly more infrastructure.

## Tradeoff

The MVP demonstrates audit-oriented design principles without implementing full enterprise governance workflows.

---

# 7. Travel Distance Resolution Was Simplified

## Deferred Features

* airport geolocation lookup
* route optimization
* multi-leg itinerary parsing
* real distance calculation engines

## Why

The assignment primarily evaluates ingestion realism and modeling decisions rather than transportation optimization.

## Tradeoff

The current implementation focuses on category-level travel emissions handling rather than high-precision routing calculations.

---

# 8. No File Storage Layer Was Implemented

## Deferred Features

* S3 storage
* uploaded file archival
* raw file retention policies
* secure document storage

## Why

The MVP stores normalized database records only.

Production-grade file retention introduces:

* storage management
* compliance concerns
* encryption requirements
* lifecycle policies

## Tradeoff

The current implementation prioritizes ingestion processing over document retention infrastructure.

---

# 9. No Production Deployment Infrastructure Was Added Yet

## Deferred Features

* Dockerization
* CI/CD pipelines
* Kubernetes orchestration
* monitoring/alerting

## Why

The focus of the assignment was application functionality and data architecture rather than infrastructure engineering.

## Tradeoff

The MVP prioritizes platform functionality and reviewer accessibility over production operations tooling.

---

# Summary

The CarbonLedger MVP intentionally focused on:

* ingestion realism
* audit-oriented modeling
* normalization workflows
* analyst review systems
* source provenance tracking

while deferring:

* enterprise integrations
* distributed infrastructure
* advanced ESG calculation engines
* large-scale operational concerns

This prioritization was chosen to maximize architectural clarity and assignment alignment within limited implementation time.
