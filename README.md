# Data Engineering Assignment

## Project Overview

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