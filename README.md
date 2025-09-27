# Data Collection and Pre-Processing Lab Assignment

## Overview: In this lab, we will execute the 12-step Data Engineering road-map practiced in class, this time end-to-end on a realistic e-commerce dataset.

1. Hello, Data!	Load raw CSV, display first 3 rows
2. Pick the Right Container	Justify dict vs namedtuple vs sets(1–2 sentences)
3. Implement Functions and  Data structure	Implement and use it t populate an data structure
4. Bulk Loaded	Example: Map data structures from dataframes to dictionaries
5. Quick Profiling	Min/mean/max price, unique city count (set)
6. Spot the Grime	Identify at least three dirty data cases
7. Cleaning Rules	Execute fixes inside clean(); show “before/after” counts
8. Transformations	For example: Parse coupon_code ➞ numeric discount (others apply)
9. Feature Engineering	For example: Add days_since_purchase
10. Mini-Aggregation	For example: Revenue per shipping_city (dict or pandas.groupby)
11. Serialization Checkpoint	Save cleaned data to JSON
12. Soft Interview Reflection	Markdown: < 120 words explaining how Functions have helped

## Learning Objectives: 

1. Select appropriate Python data structures (Steps 1–4)
2. Design & use a small Python class with methods (Step 3 + .clean()/total())
3. Perform common Data-Engineering tasks (ingest → wrangle → clean → transform → feature-engineer) (Steps 4–10)
4. Serialize data in at least two formats (CSV + JSON) (Step 11) 
5. Explain your design choices clearly in Markdown	(All steps - Markdown blocks)
6. Create and include a data dictionary merged from two sources	(“Data-Dictionary” section)

## Data Requirements

1. Primary transactions file: Any public e-commerce sample with ≥ 500 rows (e.g. the “1000 Sales Records” CSV on ExcelBIAnalytics¹ → keep first 500) OR the 500-row synthetic file created in class. The data must contain: date, customer_id, product, price, quantity, coupon_code (or promo field), shipping_city

2. Secondary metadata file: A second open data source of your choice (product catalogue, city look-ups, coupon descriptions, etc.) - You will mine this file to build your Data Dictionary and (optionally) enhance features


Download page: https://excelbianalytics.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/. Save the file in a folder named data/ inside your repo.


# Lab2 --- Data-Collection-and-Pre-processing
