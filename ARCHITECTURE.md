# ARCHITECTURE.md

# CarbonLedger Architecture

## High-Level System Overview

CarbonLedger is designed as a lightweight ESG ingestion and analyst review platform.

The architecture separates:

* frontend analyst workflows
* backend ingestion APIs
* normalization logic
* persistence and audit tracking

---

# System Architecture

```text
                Analyst Upload UI
                React + Vite      
             
                        |
                        | HTTP API
                        |
             
                Django REST API     
                Upload Endpoints    
             
                        |
                        |
                Ingestion Layer     
                CSV Parsing       
                Normalization       

                        |
                        |
                EmissionRecord DB  
                    SQLite              
            
                        |
                        |
            
                Dashboard Review UI
                Summary Analytics   
```

---

# Frontend Architecture

## Stack

* React
* Vite
* Axios

## Responsibilities

The frontend handles:

* CSV upload interactions
* dashboard rendering
* summary analytics cards
* suspicious record visualization
* API communication

## Key Components

| Component       | Responsibility                |
| --------------- | ----------------------------- |
| Upload UI       | CSV file selection and upload |
| Dashboard Table | Analyst review interface      |
| Summary Cards   | Aggregated metrics            |
| Axios Client    | Backend communication         |

---

# Backend Architecture

## Stack

* Django
* Django REST Framework
* Pandas

## Responsibilities

The backend handles:

* ingestion APIs
* parsing workflows
* normalization
* suspicious detection
* persistence
* audit tracking

---

# Ingestion Pipeline

## Upload Flow

```text
CSV Upload
    |
React Upload UI
    |
Django API Endpoint
    |
CSV Parser
    |
Normalization Logic
    |
CO2e Calculation
    |
Suspicious Detection
    |
Database Persistence
    |
Dashboard Refresh
```

---

# Data Model Architecture

## Tenant

Represents an organization using the platform.

Supports:

* multi-tenancy
* organizational isolation
* SaaS-style scalability

---

## Source

Represents an uploaded ingestion source.

Tracks:

* source provenance
* upload timestamps
* source type
* audit traceability

---

## EmissionRecord

Represents normalized operational emissions data.

Supports:

* ESG categorization
* normalization
* analyst workflows
* suspicious detection
* review lifecycle states

---

# Normalization Layer

The platform separates:

* raw operational values
* normalized analytical values

This improves:

* auditability
* consistency
* traceability

Example:

* gallons - liters
* inconsistent enterprise exports

---

# Suspicious Detection Layer

The MVP currently flags:

* negative quantities
* invalid calculated emissions

This creates a lightweight anomaly-review workflow for analysts.

---

# Workflow Lifecycle

Emission records move through states:

```text
Pending
   |
Approved / Rejected
   |
Locked
```

This models realistic ESG governance workflows.

---

# Auditability Design

The architecture prioritizes:

* source provenance
* timestamps
* workflow states
* raw payload retention
* analyst modification tracking

These are important for ESG audit and compliance workflows.

---

# Multi-Tenancy Design

All major entities are tenant-scoped.

Benefits:

* organizational separation
* future RBAC compatibility
* scalable SaaS architecture

---

# Current Limitations

The MVP intentionally does not yet include:

* async ingestion queues
* real SAP connectivity
* OCR utility parsing
* advanced RBAC
* distributed infrastructure
* emission-factor versioning

These were deferred to prioritize:

* ingestion realism
* analyst workflows
* audit-oriented modeling
* implementation clarity

---

# Future Architecture Enhancements

Potential future improvements:

* PostgreSQL migration
* Celery ingestion workers
* S3 raw file storage
* OAuth integrations
* external ESG factor services
* event-driven ingestion
* facility hierarchy modeling
* historical lineage tracking
