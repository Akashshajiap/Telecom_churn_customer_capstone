import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

os.makedirs(
    "../04_PYTHON_OUTPUT",
    exist_ok=True
)


# ==========================================
# LOAD CLEANED CUSTOMER DATA
# ==========================================

customers = pd.read_csv(
    "../Python/"
    "telecom_customer_churn_cleaned.csv"
)

# ==========================================
# LOAD CLEANED ZIP DATA
# ==========================================

zip_population = pd.read_csv(
    "../Python/"
    "telecom_zipcode_population_cleaned.csv"
)


# ==========================================
# BASIC DATA PROFILE
# ==========================================

print("========== DATA PROFILE ==========")

print("Customer Shape:",
      customers.shape)

print("ZIP Shape:",
      zip_population.shape)

print("\nCustomer Columns:")
print(customers.columns.tolist())

print("\nMissing Values:")
print(customers.isnull().sum())


# ==========================================
# CUSTOMER STATUS
# ==========================================

print("\n========== CUSTOMER STATUS ==========")

print(
    customers["customer_status"]
    .value_counts()
)


# ==========================================
# CHURN ANALYSIS
# ==========================================

churned = customers[
    customers["customer_status"] == "Churned"
]

print("\nChurned Customers:",
      len(churned))


# Exclude Joined customers from churn-rate denominator

active_base = customers[
    customers["customer_status"] != "Joined"
]

churn_rate = (
    len(churned) /
    len(active_base)
) * 100

print(
    "Churn Rate:",
    round(churn_rate, 2),
    "%"
)


# ==========================================
# CHURN FLAG
# ==========================================

customers["churn_flag"] = (
    customers["customer_status"]
    .eq("Churned")
    .astype(int)
)


# ==========================================
# CONTRACT ANALYSIS
# ==========================================

print("\n========== CONTRACT ==========")

print(
    customers["contract"]
    .value_counts()
)


print("\n========== CHURN BY CONTRACT ==========")

print(
    pd.crosstab(
        customers["contract"],
        customers["customer_status"],
        normalize="index"
    ) * 100
)


# ==========================================
# REVENUE BY CONTRACT
# ==========================================

print("\n========== REVENUE BY CONTRACT ==========")

print(
    customers
    .groupby("contract")["total_revenue"]
    .sum()
    .sort_values(ascending=False)
)


# ==========================================
# INTERNET TYPE
# ==========================================

print("\n========== CHURN BY INTERNET TYPE ==========")

print(
    pd.crosstab(
        customers["internet_type"],
        customers["customer_status"],
        normalize="index"
    ) * 100
)


# ==========================================
# PAYMENT METHOD
# ==========================================

print("\n========== CHURN BY PAYMENT METHOD ==========")

print(
    pd.crosstab(
        customers["payment_method"],
        customers["customer_status"],
        normalize="index"
    ) * 100
)


# ==========================================
# CHURN REASON
# ==========================================

print("\n========== CHURN REASONS ==========")

reason = (
    customers[
        customers["customer_status"] == "Churned"
    ]["churn_reason"]
    .value_counts()
)

print(reason)


# ==========================================
# CHURN CATEGORY
# ==========================================

print("\n========== CHURN CATEGORIES ==========")

category = (
    customers[
        customers["customer_status"] == "Churned"
    ]["churn_category"]
    .value_counts()
)

print(category)


# ==========================================
# FEATURE ENGINEERING
# ==========================================

customers["age_group"] = pd.cut(
    customers["age"],
    bins=[0, 25, 35, 45, 55, 65, 100],
    labels=[
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "56-65",
        "65+"
    ]
)


customers["tenure_group"] = pd.cut(
    customers["tenure_in_months"],
    bins=[0, 6, 12, 24, 48, 72, 100],
    labels=[
        "0-6 Months",
        "7-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-72 Months",
        "73+ Months"
    ]
)


# ==========================================
# REVENUE METRICS
# ==========================================

customers["net_revenue"] = (
    customers["total_revenue"]
    - customers["total_refunds"]
)


customers["revenue_per_month"] = (
    customers["total_revenue"]
    /
    customers["tenure_in_months"]
    .replace(0, 1)
)


# ==========================================
# SAVE EDA DATASET
# ==========================================

customers.to_csv(
    "../04_PYTHON_OUTPUT/"
    "telecom_customer_churn_eda.csv",
    index=False
)


# ==========================================
# VISUALIZATION 1
# CUSTOMER STATUS
# ==========================================

plt.figure(figsize=(8, 5))

customers["customer_status"].value_counts().plot(
    kind="bar"
)

plt.title("Customer Status Distribution")
plt.xlabel("Customer Status")
plt.ylabel("Customers")

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "01_customer_status.png"
)

plt.close()


# ==========================================
# VISUALIZATION 2
# CHURN BY CONTRACT
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=customers,
    x="contract",
    hue="customer_status"
)

plt.title("Customer Status by Contract")
plt.xlabel("Contract")
plt.ylabel("Customers")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "02_churn_by_contract.png"
)

plt.close()


# ==========================================
# VISUALIZATION 3
# CHURN BY INTERNET TYPE
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=customers,
    x="internet_type",
    hue="customer_status"
)

plt.title("Customer Status by Internet Type")
plt.xlabel("Internet Type")
plt.ylabel("Customers")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "03_churn_by_internet.png"
)

plt.close()


# ==========================================
# VISUALIZATION 4
# CHURN BY PAYMENT METHOD
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=customers,
    x="payment_method",
    hue="customer_status"
)

plt.title("Customer Status by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Customers")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "04_churn_by_payment.png"
)

plt.close()


# ==========================================
# VISUALIZATION 5
# CHURN BY TENURE
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=customers,
    x="tenure_group",
    hue="customer_status"
)

plt.title("Customer Status by Tenure")
plt.xlabel("Tenure Group")
plt.ylabel("Customers")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "05_churn_by_tenure.png"
)

plt.close()


# ==========================================
# VISUALIZATION 6
# REVENUE BY CONTRACT
# ==========================================

revenue = (
    customers
    .groupby("contract")["total_revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

revenue.plot(kind="bar")

plt.title("Total Revenue by Contract")
plt.xlabel("Contract")
plt.ylabel("Total Revenue")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "06_revenue_by_contract.png"
)

plt.close()


# ==========================================
# VISUALIZATION 7
# CHURN BY AGE GROUP
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=customers,
    x="age_group",
    hue="customer_status"
)

plt.title("Customer Status by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Customers")

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "07_churn_by_age.png"
)

plt.close()


# ==========================================
# VISUALIZATION 8
# CHURN REASONS
# ==========================================

plt.figure(figsize=(10, 7))

reason.plot(kind="barh")

plt.title("Churn Reasons")
plt.xlabel("Customers")
plt.ylabel("Churn Reason")

plt.tight_layout()

plt.savefig(
    "../04_PYTHON_OUTPUT/"
    "08_churn_reasons.png"
)

plt.close()


# ==========================================
# ZIP POPULATION ANALYSIS
# ==========================================

print("\n========== ZIP POPULATION ==========")

print(zip_population.head())

print("\nZIP Shape:",
      zip_population.shape)

print("\nZIP Missing Values:")
print(zip_population.isnull().sum())


print("\n====================================")
print("Python EDA Completed Successfully")
print("====================================")