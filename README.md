# CarbonLedger

## Overview

CarbonLedger is a lightweight ESG emissions ingestion and analyst review platform built to simulate realistic enterprise sustainability reporting workflows.

The platform allows analysts to:

* upload emissions-related operational data
* normalize inconsistent source formats
* calculate CO2e values
* flag suspicious records
* review emissions data through a dashboard UI

The system was designed with a strong focus on:

* auditability
* source provenance
* normalization workflows
* analyst usability
* multi-tenant architecture

---

# Features

## Backend Features

* Django REST Framework APIs
* Multi-tenant data model
* SAP CSV ingestion
* Source provenance tracking
* Emission normalization
* Suspicious record detection
* Workflow statuses
* Audit-oriented schema
* Admin dashboard support

---

## Frontend Features

* React + Vite dashboard
* CSV upload UI
* Emission records table
* Suspicious record indicators
* Summary analytics cards
* Automatic dashboard refresh after ingestion

---

# Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Frontend   | React + Vite          |
| Backend    | Django REST Framework |
| Database   | SQLite                |
| API Client | Axios                 |
| Parsing    | Pandas                |
| Language   | Python / JavaScript   |

---

# Project Structure

```text
carbonledger/

    emissions/
    frontend/
    ingestion/
    MODEL.md
    DECISIONS.md
    TRADEOFFS.md
    SOURCES.md
    manage.py
```

---

# Setup Instructions

## Backend Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

#### Git Bash

```bash
source venv/Scripts/activate
```

#### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install django djangorestframework pandas django-cors-headers
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start backend server

```bash
python manage.py runserver
```

Backend runs at:

```text
http://127.0.0.1:8000/
```

---

# Frontend Setup

## 1. Move into frontend directory

```bash
cd frontend
```

## 2. Install dependencies

```bash
npm install
```

## 3. Start frontend server

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173/
```

---

# API Endpoints

| Endpoint         | Method | Purpose                |
| ---------------- | ------ | ---------------------- |
| /api/upload/sap/ | POST   | Upload SAP CSV         |
| /api/records/    | GET    | Fetch emission records |
| /admin/          | GET    | Django admin panel     |

---

# Example Workflow

1. Analyst uploads SAP CSV export
2. Backend parses source file
3. Quantities are normalized
4. CO2e values are calculated
5. Suspicious records are flagged
6. Records are stored in database
7. Dashboard refreshes automatically

---

# Suspicious Record Detection

The MVP currently flags:

* negative quantities
* invalid emissions calculations

These records are surfaced for analyst review before approval or audit locking.

---

# ESG Scope Mapping

| Scope   | Meaning                        |
| ------- | ------------------------------ |
| Scope 1 | Direct fuel emissions          |
| Scope 2 | Purchased electricity          |
| Scope 3 | Indirect operational emissions |

---

# Documentation

Additional design documentation:

* MODEL.md
* DECISIONS.md
* TRADEOFFS.md
* SOURCES.md

---

# Future Improvements

Potential future enhancements include:

* real SAP integrations
* utility PDF OCR parsing
* travel API integrations
* advanced anomaly detection
* RBAC authentication
* asynchronous ingestion jobs
* historical audit lineage
* emission factor versioning

---

# Design Philosophy

The project intentionally prioritizes:

* realistic ingestion workflows
* audit-oriented modeling
* normalization handling
* analyst review systems
* architectural clarity

over enterprise-scale infrastructure complexity.
