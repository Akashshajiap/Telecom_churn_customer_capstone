import pandas as pd


# ==========================================
# 1. LOAD CUSTOMER DATA
# ==========================================

customer_file = (
    "../data/"
    "telecom_customer_churn.csv"
)

customers = pd.read_csv(customer_file)

print("========== ORIGINAL CUSTOMER DATA ==========")
print("Shape:", customers.shape)


# ==========================================
# 2. CLEAN CUSTOMER COLUMN NAMES
# ==========================================

customers.columns = (
    customers.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)


# ==========================================
# 3. REMOVE EXTRA SPACES
# ==========================================

customer_text_columns = (
    customers.select_dtypes(
        include="object"
    ).columns
)

for col in customer_text_columns:
    customers[col] = customers[col].str.strip()


# ==========================================
# 4. NUMERIC CUSTOMER COLUMNS
# ==========================================

numeric_columns = [
    "age",
    "number_of_dependents",
    "zip_code",
    "latitude",
    "longitude",
    "number_of_referrals",
    "tenure_in_months",
    "avg_monthly_long_distance_charges",
    "avg_monthly_gb_download",
    "monthly_charge",
    "total_charges",
    "total_refunds",
    "total_extra_data_charges",
    "total_long_distance_charges",
    "total_revenue"
]

for col in numeric_columns:
    if col in customers.columns:
        customers[col] = pd.to_numeric(
            customers[col],
            errors="coerce"
        )


# ==========================================
# 5. CUSTOMER DATA PROFILING
# ==========================================

print("\n========== CUSTOMER DATA PROFILING ==========")

print("Rows:", len(customers))
print("Columns:", len(customers.columns))

print("\nData Types:")
print(customers.dtypes)

print("\nMissing Values:")
print(customers.isnull().sum())

print("\nUnique Values:")
print(customers.nunique())


# ==========================================
# 6. CUSTOMER ID VALIDATION
# ==========================================

print("\n========== CUSTOMER ID VALIDATION ==========")

print("Total Rows:",
      len(customers))

print("Unique Customer IDs:",
      customers["customer_id"].nunique())

print("Duplicate Customer IDs:",
      customers["customer_id"].duplicated().sum())


# ==========================================
# 7. DUPLICATE CUSTOMER RECORDS
# ==========================================

duplicates = customers[
    customers["customer_id"]
    .duplicated(keep=False)
]

print("\nDuplicate Customer Records:")

if len(duplicates) > 0:
    print(duplicates)
else:
    print("No duplicate Customer IDs found.")


# ==========================================
# 8. MISSING VALUE ANALYSIS
# ==========================================

missing = (
    customers
    .isnull()
    .sum()
)

missing = (
    missing[missing > 0]
    .sort_values(ascending=False)
)

print("\n========== MISSING VALUE ANALYSIS ==========")
print(missing)


# Missing percentage

missing_percentage = (
    customers.isnull()
    .mean() * 100
)

missing_percentage = (
    missing_percentage
    .sort_values(ascending=False)
)

print("\n========== MISSING VALUE PERCENTAGE ==========")
print(missing_percentage)


# ==========================================
# 9. MONTHLY CHARGE QUALITY CHECK
# ==========================================

print("\n========== MONTHLY CHARGE CHECK ==========")

negative_monthly_charge = customers[
    customers["monthly_charge"] < 0
][
    [
        "customer_id",
        "monthly_charge",
        "contract",
        "customer_status"
    ]
]

print(
    "Negative Monthly Charge Records:",
    len(negative_monthly_charge)
)

print(negative_monthly_charge)


# ==========================================
# 10. LOAD ZIP POPULATION DATA
# ==========================================

zip_file = (
    "../data/"
    "telecom_zipcode_population.csv"
)

zip_population = pd.read_csv(zip_file)

print("\n========== ORIGINAL ZIP DATA ==========")
print("Shape:", zip_population.shape)


# ==========================================
# 11. CLEAN ZIP COLUMN NAMES
# ==========================================

zip_population.columns = (
    zip_population.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)


# ==========================================
# 12. REMOVE EXTRA SPACES
# ==========================================

zip_text_columns = (
    zip_population
    .select_dtypes(include="object")
    .columns
)

for col in zip_text_columns:
    zip_population[col] = (
        zip_population[col]
        .str.strip()
    )


# ==========================================
# 13. ZIP DATA VALIDATION
# ==========================================

print("\n========== ZIP VALIDATION ==========")

print("Rows:",
      len(zip_population))

print("Columns:",
      len(zip_population.columns))

print("\nMissing Values:")

print(
    zip_population.isnull().sum()
)

print("\nDuplicate Complete Rows:")

print(
    zip_population.duplicated().sum()
)


# ==========================================
# 14. DUPLICATE ZIP CODE CHECK
# ==========================================

if "zip_code" in zip_population.columns:

    print("\nDuplicate ZIP Codes:")

    print(
        zip_population["zip_code"]
        .duplicated()
        .sum()
    )


# ==========================================
# 15. SAVE CLEANED CUSTOMER DATA
# ==========================================

customers.to_csv(
    "../Python/"
    "telecom_customer_churn_cleaned.csv",
    index=False
)


# ==========================================
# 16. SAVE CLEANED ZIP DATA
# ==========================================

zip_population.to_csv(
    "../Python/"
    "telecom_zipcode_population_cleaned.csv",
    index=False
)


# ==========================================
# 17. FINAL VALIDATION
# ==========================================

print("\n========== FINAL VALIDATION ==========")

print(
    "Cleaned Customer Rows:",
    len(customers)
)

print(
    "Cleaned ZIP Rows:",
    len(zip_population)
)

print("\n========================================")
print("Both cleaned CSV files created.")
print("========================================")