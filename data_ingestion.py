import pandas as pd

# =========================
# DATASET 1 - FUND MASTER
# =========================

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\n=====DATASET 1 - FUND MASTER =====")

print("\nShape")
print(df.shape)

print("\nData Types")
print(df.dtypes)

print("\nFirst 5 Rows")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

print("\nFund Houses")
print(df["fund_house"].unique())

print("\nCategories")
print(df["category"].unique())

print("\nSub Categories")
print(df["sub_category"].unique())

print("\nRisk Categories")
print(df["risk_category"].unique())

print("\nDuplicate Rows")
print(df.duplicated().sum())


# =========================
# DATASET 2 - NAV HISTORY
# =========================

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("\n=====DATASET 2 - NAV HISTORY =====")

print("\nShape")
print(nav_history.shape)

print("\nData Types")
print(nav_history.dtypes)

print("\nFirst 5 Rows")
print(nav_history.head())

print("\nMissing Values")
print(nav_history.isnull().sum())

print("\nDuplicate Rows")
print(nav_history.duplicated().sum())

print("\nUnique AMFI Codes")
print(nav_history["amfi_code"].nunique())

# =========================
# DATASET 3 - AUM BY FUND HOUSE
# =========================

aum_df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("\n=====DATASET 3 - AUM BY FUND HOUSE =====")

print("\nShape")
print(aum_df.shape)

print("\nData Types")
print(aum_df.dtypes)

print("\nFirst 5 Rows")
print(aum_df.head())

print("\nMissing Values")
print(aum_df.isnull().sum())

print("\nDuplicate Rows")
print(aum_df.duplicated().sum())

print("\nFund Houses")
print(aum_df["fund_house"].unique())


# =========================
# DATASET 4 - MONTHLY SIP INFLOWS
# =========================

sip_df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("\n=====DATASET 4 - MONTHLY SIP INFLOWS =====")

print("\nShape")
print(sip_df.shape)

print("\nData Types")
print(sip_df.dtypes)

print("\nFirst 5 Rows")
print(sip_df.head())

print("\nMissing Values")
print(sip_df.isnull().sum())

print("\nDuplicate Rows")
print(sip_df.duplicated().sum())


# =========================
# DATASET 5 - CATEGORY INFLOWS
# =========================

category_df = pd.read_csv("data/raw/05_category_inflows.csv")

print("\n=====DATASET 5 - CATEGORY INFLOWS =====")

print("\nShape")
print(category_df.shape)

print("\nData Types")
print(category_df.dtypes)

print("\nFirst 5 Rows")
print(category_df.head())

print("\nMissing Values")
print(category_df.isnull().sum())

print("\nDuplicate Rows")
print(category_df.duplicated().sum())

print("\nCategories")
print(category_df["category"].unique())

# =========================
# DATASET 6 - INDUSTRY FOLIO COUNT
# =========================

folio_df = pd.read_csv("data/raw/06_industry_folio_count.csv")

print("\n===== INDUSTRY FOLIO COUNT =====")

print("\nShape")
print(folio_df.shape)

print("\nData Types")
print(folio_df.dtypes)

print("\nFirst 5 Rows")
print(folio_df.head())

print("\nMissing Values")
print(folio_df.isnull().sum())

print("\nDuplicate Rows")
print(folio_df.duplicated().sum())


# =========================
# DATASET 7 - SCHEME PERFORMANCE
# =========================

scheme_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("\n===== DATASET 7 - SCHEME PERFORMANCE =====")

print("\nShape")
print(scheme_df.shape)

print("\nData Types")
print(scheme_df.dtypes)

print("\nFirst 5 Rows")
print(scheme_df.head())

print("\nMissing Values")
print(scheme_df.isnull().sum())

print("\nDuplicate Rows")
print(scheme_df.duplicated().sum())

print("\nFund Houses")
print(scheme_df["fund_house"].unique())

print("\nCategories")
print(scheme_df["category"].unique())

print("\nRisk Grades")
print(scheme_df["risk_grade"].unique())

print("\nMorningstar Ratings")
print(scheme_df["morningstar_rating"].unique())



# =========================
# DATASET 8 - INVESTOR TRANSACTIONS
# =========================

transaction_df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("\n===== DATASET 8 - INVESTOR TRANSACTIONS =====")

print("\nShape")
print(transaction_df.shape)

print("\nData Types")
print(transaction_df.dtypes)

print("\nFirst 5 Rows")
print(transaction_df.head())

print("\nMissing Values")
print(transaction_df.isnull().sum())

print("\nDuplicate Rows")
print(transaction_df.duplicated().sum())

print("\nTransaction Types")
print(transaction_df["transaction_type"].unique())

print("\nStates")
print(transaction_df["state"].unique())

print("\nCity Tiers")
print(transaction_df["city_tier"].unique())

print("\nAge Groups")
print(transaction_df["age_group"].unique())

print("\nKYC Status")
print(transaction_df["kyc_status"].unique())



# =========================
# DATASET 9 - PORTFOLIO HOLDINGS
# =========================

portfolio_df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print("\n===== DATASET 9 - PORTFOLIO HOLDINGS =====")

print("\nShape")
print(portfolio_df.shape)

print("\nData Types")
print(portfolio_df.dtypes)

print("\nFirst 5 Rows")
print(portfolio_df.head())

print("\nMissing Values")
print(portfolio_df.isnull().sum())

print("\nDuplicate Rows")
print(portfolio_df.duplicated().sum())

print("\nSectors")
print(portfolio_df["sector"].unique())

print("\nUnique Stocks")
print(portfolio_df["stock_name"].nunique())


# =========================
# DATASET 10 - BENCHMARK INDICES
# =========================

benchmark_df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("\n===== DATASET 10 - BENCHMARK INDICES =====")

print("\nShape")
print(benchmark_df.shape)

print("\nData Types")
print(benchmark_df.dtypes)

print("\nFirst 5 Rows")
print(benchmark_df.head())

print("\nMissing Values")
print(benchmark_df.isnull().sum())

print("\nDuplicate Rows")
print(benchmark_df.duplicated().sum())

print("\nBenchmark Indices")
print(benchmark_df["index_name"].unique())



# =========================
# AMFI CODE VALIDATION
# =========================

print("\n===== AMFI CODE VALIDATION =====")

fund_master_codes = set(df["amfi_code"])

nav_history_codes = set(nav_history["amfi_code"])

missing_codes = fund_master_codes - nav_history_codes

print("\nTotal Fund Master Codes:")
print(len(fund_master_codes))

print("\nTotal NAV History Codes:")
print(len(nav_history_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes exist in NAV History")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing_codes)



print("\n===== DATA QUALITY SUMMARY =====")

datasets = {
    "Fund Master": df,
    "NAV History": nav_history,
    "AUM": aum_df,
    "SIP Inflows": sip_df,
    "Category Inflows": category_df,
    "Folio Count": folio_df,
    "Scheme Performance": scheme_df,
    "Investor Transactions": transaction_df,
    "Portfolio Holdings": portfolio_df,
    "Benchmark Indices": benchmark_df
}

for name, dataset in datasets.items():
    print(f"\n{name}")

    print("Missing Values:")
    print(dataset.isnull().sum().sum())

    print("Duplicate Rows:")
    print(dataset.duplicated().sum())