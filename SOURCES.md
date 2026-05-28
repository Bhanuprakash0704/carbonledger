# Source Research and Realism Notes

This document explains the real-world source formats researched for CarbonLedger, the ingestion assumptions made, and limitations of the MVP implementation.

---

# 1. SAP Fuel and Procurement Data

## Researched Formats

I researched common SAP integration/export patterns including:

* SAP IDoc
* SAP BAPI
* SAP OData services
* flat-file CSV exports

## Selected Format

For the MVP, I selected CSV-style SAP exports.

## Why This Choice Was Made

CSV exports are common in operational finance and procurement workflows because analysts frequently:

* export reports manually
* email spreadsheets between teams
* upload procurement extracts into downstream systems

This format also allowed realistic modeling of:

* inconsistent units
* localized column naming
* operational procurement data

---

# Realistic Characteristics Modeled

The sample SAP data intentionally includes:

| Characteristic             | Example             |
| -------------------------- | ------------------- |
| inconsistent units         | liters vs gallons   |
| suspicious values          | negative quantities |
| operational fuel purchases | diesel procurement  |
| analyst-review-worthy rows | invalid values      |

---

# Example SAP Data Shape

Example columns modeled:

* material_category
* fuel_type
* quantity
* unit
* plant_code
* posting_date

---

# Real-World Challenges Not Fully Implemented

Production SAP ingestion would likely require handling:

* localized column headers
* German-language exports
* ERP-specific encoding issues
* large batch files
* duplicate procurement records
* reconciliation against master data

---

# What Would Break in Production

The MVP does not yet handle:

* direct SAP authentication
* live ERP synchronization
* schema drift
* IDoc parsing
* malformed enterprise exports
* asynchronous ingestion scaling

---

# 2. Utility Electricity Data

## Researched Formats

I researched common utility data delivery methods including:

* portal CSV exports
* PDF electricity bills
* smart meter APIs
* spreadsheet exports

## Selected Format

The MVP assumes CSV exports from utility portals.

## Why This Choice Was Made

Many facilities teams still download:

* monthly consumption reports
* billing summaries
* meter usage exports

as CSV or spreadsheet files.

This was chosen because it:

* reflects operational reality
* avoids OCR complexity
* enables deterministic ingestion workflows

---

# Realistic Characteristics Modeled

Utility data assumptions include:

| Characteristic        | Example              |
| --------------------- | -------------------- |
| billing periods       | non-calendar aligned |
| unit handling         | kWh                  |
| facility-level usage  | building electricity |
| emissions attribution | Scope 2              |

---

# Example Utility Data Shape

Example fields researched:

* meter_id
* billing_start
* billing_end
* consumption_kwh
* tariff_code
* facility_name

---

# Real-World Challenges Not Fully Implemented

Production utility ingestion may require:

* tariff parsing
* demand charges
* interval meter data
* timezone normalization
* multi-meter aggregation
* PDF OCR extraction

---

# What Would Break in Production

The MVP does not currently support:

* PDF parsing
* smart meter APIs
* interval consumption ingestion
* utility authentication workflows
* dynamic tariff structures

---

# 3. Corporate Travel Data

## Researched Formats

I researched travel management platforms including:

* Concur
* Navan
* expense-management exports
* itinerary APIs

## Selected Format

The MVP assumes exported operational travel records similar to CSV/API responses from travel platforms.

## Why This Choice Was Made

Corporate travel systems commonly expose:

* expense exports
* itinerary records
* booking summaries
* API-accessible travel events

This allowed realistic Scope 3 modeling without implementing external API integrations.

---

# Realistic Characteristics Modeled

Travel assumptions include:

| Characteristic             | Example                         |
| -------------------------- | ------------------------------- |
| travel categories          | flight, hotel, ground transport |
| indirect emissions         | Scope 3                         |
| incomplete distance data   | airport-only information        |
| operational travel records | business travel                 |

---

# Example Travel Data Shape

Example fields researched:

* employee_id
* trip_type
* departure_airport
* arrival_airport
* hotel_nights
* transport_mode

---

# Real-World Challenges Not Fully Implemented

Production travel systems may require:

* route distance calculation
* multi-leg itinerary parsing
* duplicate expense reconciliation
* employee privacy handling
* currency normalization
* international travel compliance

---

# What Would Break in Production

The MVP does not currently support:

* OAuth integrations
* live Concur/Navan APIs
* itinerary graphing
* route optimization
* airline-specific emissions factors

---

# Overall Design Philosophy

The CarbonLedger MVP intentionally focused on:

* realistic operational ingestion patterns
* analyst review workflows
* audit-oriented modeling
* normalization handling
* source provenance

rather than attempting full enterprise integration complexity.

The selected source assumptions were designed to balance:

* realism
* implementation feasibility
* reviewer clarity
* architectural quality
  within the scope of the assignment.
