# Mental Health Wellness at Workplace

## Project Overview

This repository contains a small data analysis project focused on employee mental health in the workplace. The project includes a dataset, a Python cleanup and analysis script, SQL analysis queries, and a Power BI report.

## Files

- `Mental_health_at_workplace.py`
  - Reads the raw dataset from `mental_health_workplace.csv`
  - Cleans missing values
  - Drops unused columns
  - Prints summary statistics for employee mental health, stress, work-life balance, job satisfaction, and other workplace factors
  - Exports the cleaned dataset to `mental_health_cleaned.csv`

- `mental_health_workplace.csv`
  - Raw source dataset containing employee-level mental health and workplace information
  - Columns include demographics, compensation, hours, mental health condition, diagnosis and treatment, stress and burnout, work-life balance, productivity, support metrics, and intention to leave

- `mental_health_cleaned.csv`
  - Cleaned version of the dataset produced by `Mental_health_at_workplace.py`
  - Used as the source table for SQL analysis and reporting

- `mental_health_analysis_queries.sql`
  - SQL queries for analyzing the cleaned dataset in a database environment
  - Includes queries for salary by country, work-life balance, intent to leave, workload by industry, diagnosis counts, satisfaction by gender, sleep trends, and employer support

- `Emloyee_mental_health_analysis.pbix`
  - Power BI report file for visualizing and exploring the cleaned dataset
  - Contains dashboards or visuals based on the employee mental health analysis

## Getting Started

### Prerequisites

- Python 3.x
- `pandas` library
- Optionally, Power BI Desktop to open `Emloyee_mental_health_analysis.pbix`

### Install dependencies

```bash
pip install pandas
```

### Run the cleanup and analysis script

```bash
python Mental_health_at_workplace.py
```

This will:
- load `mental_health_workplace.csv`
- fill missing values for key columns
- drop unused columns
- display summary statistics to the console
- export `mental_health_cleaned.csv`

## Analysis Workflow

1. Use `Mental_health_at_workplace.py` to produce a cleaned dataset.
2. Load `mental_health_cleaned.csv` into a SQL database or Power BI.
3. Run the queries in `mental_health_analysis_queries.sql` to explore trends.
4. Open `Emloyee_mental_health_analysis.pbix` in Power BI for interactive dashboards.


- add more robust data validation and error handling
- modularize the Python script into functions
- add visualization directly in Python using `matplotlib` or `seaborn`
- document column definitions and expected value ranges
- build a reproducible data pipeline for cleaning, analysis, and reporting
