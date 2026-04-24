# E-Commerce ETL Pipeline

This project implements and end-to-end ETL pipeline that processes e-commerce sales data fron CSV files and loads it to PostgreSQL for analysis.

# Architecture

CSV Files -> Python (ETL) -> PostgreSQL -> SQL Analysis

Extract: Load data from orders and products CSV files
Transform: Clean data, handle missing values, validate relationships
Load: Insert transformed data to PostgreSQL tables with defined schema

## Tech Stack

- Python(, pandas, SQLAlchemy)
- PostgreSQL
- SQL

## Data structure

- **products** (products details)
  -product_id (PK)
  -product_name
  -category

- **orders** (main transactional table)
  -order_id
  -order_date
  -customer_id
  -product_id (FK -> products)
  -qty
  -unit_price
  -currency
  -total_price

\*The 'orders' table references 'products' via foreign key

## Data validation

Before loading data, a validation step ensures all product_id in the 'orders' dataset exists in the products table.

## Example queries

### Total Revenue

```sql
SELECT SUM(total_price) FROM orders;
```

### Revenue by category

```sql
SELECT p.category, SUM(o.total_price) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category;
```

## How to run

1. Create a database in PostgreSQL
2. Run 'sql/squema.sql' to create tables
3. Run 'script/etl.py' to load data
4. Run queries from 'sql/analysis.sql'

## Limitations

- Revenue is grouped by currency and not converted into a single currency

## Future Improvements

- Add currency conversion using an API
- Implement incremental data loading
- Automate pipeline execution
