import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# LOAD CLEANED CUSTOMER DATA TO MYSQL
# ==========================================

customers = pd.read_csv(
    "../Python/"
    "telecom_customer_churn_cleaned.csv"
)

# ==========================================
# LOAD CLEANED ZIP DATA TO MYSQL
# ==========================================

zip_population = pd.read_csv(
    "../Python/"
    "telecom_zipcode_population_cleaned.csv"
)

print("customer rows:", len(customers))
print("zip rows:", len(zip_population))

# ==========================================
# MYSQL CONNECTION
# ==========================================

username = "root"
password = "Akash%4012345"
host = "localhost"
database = "telecom_churn"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}")

print("MySQL connection established.")

# ==========================================
# LOAD CUSTOMER TABLE
# ==========================================

customers.to_sql(
    name="customers",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=500,
    method="multi"
)

print("Customer data loaded to MySQL.")


# ==========================================
# LOAD ZIP POPULATION TABLE
# ==========================================

zip_population.to_sql(
    name="zip_population",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=500,
    method="multi"
)

print("Zip population data loaded to MySQL.")


print("\nData loading to MySQL completed successfully.")