# import pandas as pd
# df=pd.read_csv("../data/telecom_customer_churn.csv")
# print(df.shape)
# print(df.head())
# print(df.info())



# # number of records
# print(df.shape)

# # number of columns
# print(df.columns)

# # number of data types
# print(df.info())

# # statistics
# print(df.describe())

# # missing values
# print(df.isnull().sum())

# unique values
# print(df.nunique())

import pandas as pd


# # # ==========================================
# # # CUSTOMER DATA
# # # ==========================================

customer_file = "../data/telecom_customer_churn.csv"

customers = pd.read_csv(customer_file)

print("========== CUSTOMER DATA ==========")

print("Rows:", len(customers))
print("Columns:", len(customers.columns))
print("Shape:", customers.shape)

print("\nColumn Names:")
print(customers.columns.tolist())

print("\nFirst 5 Customers:")
print(customers.head())

print("\nData Types:")
print(customers.dtypes)

print("\nBasic Statistics:")
print(customers.describe(include="all"))


# ==========================================
# CUSTOMER ID CHECK
# ==========================================

print("\n========== CUSTOMER ID CHECK ==========")

print("Total Customer Rows:",
      len(customers))

print("Unique Customer IDs:",
      customers["Customer ID"].nunique())

print("Duplicate Customer IDs:",
      customers["Customer ID"].duplicated().sum())


# ==========================================
# ZIP POPULATION DATA
# ==========================================

zip_file = "../data/telecom_zipcode_population.csv"

zip_population = pd.read_csv(zip_file)

print("\n========== ZIP POPULATION DATA ==========")

print("Rows:", len(zip_population))
print("Columns:", len(zip_population.columns))
print("Shape:", zip_population.shape)

print("\nColumn Names:")
print(zip_population.columns.tolist())

print("\nFirst 5 ZIP Records:")
print(zip_population.head())

print("\nData Types:")
print(zip_population.dtypes)


# ==========================================
# ZIP DATA QUALITY
# ==========================================

print("\n========== ZIP DATA QUALITY ==========")

print("Duplicate ZIP Rows:",
      zip_population.duplicated().sum())

print("\nMissing Values:")
print(zip_population.isnull().sum())