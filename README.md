# Data Engineering Assignment

## Project Overview

# Data Engineering Pipeline with PostgreSQL, ClickHouse & Docker

An end-to-end Data Engineering pipeline built using Python, PostgreSQL, ClickHouse, SQLAlchemy, and Docker. The project demonstrates a modern ETL workflow that ingests raw CSV data, performs data quality validation, transforms it into a staging layer, builds a dimensional star schema for analytics, and validates the warehouse before serving analytical queries.

## Key Features

* End-to-end ETL pipeline with automated execution using Docker Compose.
* Generic CSV ingestion into PostgreSQL Raw Layer.
* Data quality validation framework with configurable validation rules.
* High-performance staging layer built on ClickHouse.
* Star schema warehouse with fact and dimension tables.
* Automated warehouse validation for data integrity and consistency.
* Analytics-ready SQL queries for business insights.
* Environment-based configuration using `.env`.
* Modular, scalable, and production-oriented project structure.

## Tech Stack

* **Language:** Python
* **Databases:** PostgreSQL, ClickHouse
* **Libraries:** SQLAlchemy, Pandas, ClickHouse Connect
* **Containerization:** Docker & Docker Compose
* **Architecture:** ETL • Data Quality • Star Schema • Data Warehouse


## Architecture

                          CSV Files
                              │
                              ▼
                 Generic CSV Loader (Python)
                              │
                              ▼
                    PostgreSQL (Raw Layer)
                              │
                              ▼
                   Raw Data Validation
                              │
                              ▼
               ClickHouse Staging Layer
                              │
                              ▼
             Warehouse Transformation
                              │
                              ▼
                  Star Schema Warehouse
        ┌──────────────┬──────────────┐
        │              │              │
        ▼              ▼              ▼
  dim_customer   dim_product   dim_seller
        │              │              │
        └──────────────┴──────────────┘
                      │
                      ▼
                 dim_date
                      │
                      ▼
                  fact_sales
                      │
                      ▼
            Warehouse Validation
                      │
                      ▼
             Analytical SQL Reports

## Technology Stack

Python 3.13

PostgreSQL

ClickHouse

Docker & Docker Compose

SQL

Git

Bash

## Project Structure

## Pipeline Flow

CSV Files

↓

Raw PostgreSQL

↓

Raw Validation

↓

ClickHouse Staging

↓

Warehouse (Star Schema)

↓

Warehouse Validation

↓

Business Analytics

## Data Warehouse Design
Dimensions
dim_customer
dim_product
dim_seller
dim_date
Fact

fact_sales

Grain:

One record per order item.

## Data Validation
Raw Layer
NULL checks
Duplicate checks
Row count validation
Warehouse
Primary key validation
Duplicate key validation
Revenue validation
Referential integrity
Row count reconciliation
Payment anomaly warning

## Business Analytics
Monthly Revenue
Top Product Categories
Revenue by State
Top Sellers
Payment Analysis
Delivery Performance
Customer Analysis
Order Status Analysis
## How to Run

docker compose up --build

# Final Project Structure

de-assignment/

├── data/
├── docs/
├── images/
├── pipeline/
│   ├── ingestion/
│   ├── raw/
│   ├── staging/
│   └── warehouse/
├── sql/
│   ├── warehouse/
│   └── analytics/
├── docker-compose.yml
├── README.md
└── requirements.txt

## Future Improvements
