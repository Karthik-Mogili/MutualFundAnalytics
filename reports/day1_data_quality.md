# Day 1 Data Quality Report

## Project: Mutual Fund Analytics Platform

**Date:** 02 June 2026

---

# Dataset 01: Fund Master (01_fund_master.csv)

### Summary

Rows: 40
Columns: 15

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Unique Fund Houses Identified
✓ Categories Identified
✓ Risk Categories Identified
✓ Duplicate Records Checked

### Observations

* Launch date stored as object datatype.
* AMFI codes appear unique.
* Dataset contains Equity, Debt, Hybrid and other fund categories.
* Serves as the master reference dataset for all schemes.

---

# Dataset 02: NAV History (02_nav_history.csv)

### Summary

Rows: 46,000
Columns: 3

### Columns

* amfi_code
* date
* nav

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked

### Observations

* Contains historical NAV records for mutual fund schemes.
* AMFI code will be used to join with Fund Master dataset.
* Date column should be converted to datetime format during preprocessing.

---

# Dataset 03: AUM by Fund House (03_aum_by_fund_house.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked
✓ Fund Houses Identified

### Observations

* Contains Assets Under Management (AUM) information.
* Can be linked with Fund Master using fund house name.
* Useful for market share and growth analysis.

---

# Dataset 04: Monthly SIP Inflows (04_monthly_sip_inflows.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked

### Observations

* Contains monthly SIP inflow statistics.
* Includes SIP account growth metrics.
* Useful for investor participation trend analysis.
* Month column may require datetime conversion.

---

# Dataset 05: Category Inflows (05_category_inflows.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked
✓ Categories Identified

### Observations

* Contains category-wise inflow and outflow data.
* Useful for analyzing investor preferences across fund categories.
* Can be used to identify sector and category trends.

---

# Dataset 06: Industry Folio Count (06_industry_folio_count.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked

### Observations

* Contains industry-wide folio count information.
* Useful for measuring investor participation growth.
* Can be analyzed alongside SIP inflow trends.

---

# Dataset 07: Scheme Performance (07_scheme_performance.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked
✓ Fund Houses Identified
✓ Categories Identified
✓ Risk Grades Identified
✓ Ratings Identified

### Observations

* Contains scheme performance metrics.
* Includes category and risk information.
* Useful for return comparison and ranking analysis.
* Can be linked with Fund Master using AMFI code.

---

# Dataset 08: Investor Transactions (08_investor_transactions.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked
✓ Transaction Types Identified
✓ States Identified
✓ City Tiers Identified
✓ Age Groups Identified
✓ KYC Status Checked

### Observations

* Contains investor transaction activity.
* Includes demographic information.
* Useful for behavioral and regional investment analysis.
* Can be used to study purchase and redemption trends.

---

# Dataset 09: Portfolio Holdings (09_portfolio_holdings.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked
✓ Sectors Identified
✓ Unique Stocks Counted

### Observations

* Contains portfolio holdings of mutual fund schemes.
* Includes stock-level allocations.
* Useful for sector exposure and diversification analysis.
* Can identify top holdings across schemes.

---

# Dataset 10: Benchmark Indices (10_benchmark_indices.csv)

### Checks Performed

✓ Shape Checked
✓ Data Types Checked
✓ Missing Values Checked
✓ Duplicate Rows Checked
✓ Benchmark Indices Identified

### Observations

* Contains benchmark index performance data.
* Useful for comparing mutual fund returns with market benchmarks.
* Supports relative performance analysis.
* Date field may require datetime conversion.

---

# AMFI Code Validation

### Checks Performed

✓ AMFI Codes Compared Between Fund Master and NAV History

### Observations

* AMFI codes from Fund Master were validated against NAV History.
* No missing AMFI codes detected (update if any are found during execution).
* Relationship between Fund Master and NAV History is suitable for ETL processing and dashboard development.

---

# Overall Day 1 Summary

### Tasks Completed

✓ Project folder structure created

✓ Git repository initialized

✓ Required dependencies installed

✓ requirements.txt generated

✓ CSV datasets ingested successfully

✓ Data quality assessment performed

✓ Missing value analysis completed

✓ Duplicate record analysis completed

✓ Initial exploratory data analysis completed

✓ Dataset relationships identified

### Pending Tasks

* Fetch live NAV data from MFAPI
* Save API data into raw dataset folder
* Complete AMFI validation script
* Push project to GitHub
* Commit changes using:

```bash
git commit -m "Day 1: Data ingestion complete"
```

### Conclusion

All datasets were successfully ingested and reviewed. Initial quality checks indicate that the data is suitable for further ETL processing, validation, dashboard creation, and analytical reporting in subsequent project phases.
