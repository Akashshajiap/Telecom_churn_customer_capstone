# 📊 Telecom Customer Churn & Revenue Analytics

An end-to-end data analytics project that takes a raw telecom customer dataset from cleaning through to an executive-ready Power BI dashboard — covering Python EDA, MySQL data modeling, SQL analysis, and interactive BI reporting.

![Python](https://img.shields.io/badge/Python-Pandas-3776AB?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-Pivot%20Analysis-217346?logo=microsoftexcel&logoColor=white)

---

## 📌 Executive Summary

This project analyzes **7,043 telecom customers** to understand why customers churn and how that churn impacts revenue. Raw customer and ZIP-code population data is cleaned in Python, loaded into a MySQL database, queried with SQL for churn and geographic analysis, and visualized in a 4-page Power BI dashboard (Executive Overview, Churn Analysis, Geographic & Population Analysis, Revenue & Retention) plus a supporting Excel pivot workbook.

The analysis found an overall **churn rate of ~28%** (among customers who weren't brand-new), heavily concentrated in **month-to-month contracts**, **Fiber Optic internet customers**, and customers paying by **mailed check or bank withdrawal** — with **competitor offers** as the single largest driver of churn.

## 🎯 Business Problem

Telecom providers operate in a highly competitive market where customer acquisition is expensive and churn directly erodes recurring revenue. Without a structured view of *who* is churning, *why*, and *where*, the business can't prioritize retention spend effectively. Key pain points this project addresses:

- No consolidated view of churn rate, revenue at risk, and customer segments in one place.
- Unclear which contract types, services, and payment methods correlate with higher churn.
- No geographic lens on churn — is attrition concentrated in specific cities or population densities?
- Manual, ad-hoc reporting instead of a governed data pipeline (raw data → cleaned data → database → dashboard).

## ❓ Business Questions

1. What is the overall customer churn rate, and how much revenue is at risk?
2. Which contract types, internet service types, and payment methods have the highest churn?
3. Why are customers churning (churn reasons and churn categories)?
4. Does tenure (how long a customer has stayed) affect the likelihood of churn?
5. Are there geographic patterns in churn — specific cities or ZIP codes with disproportionate churn?
6. How does revenue differ across contract types and service types, and where is retention strongest?
7. Do demographic factors (age, gender) show any relationship with churn?

## 🛠️ Tools & Technologies

| Layer | Tools |
|---|---|
| Data Cleaning & EDA | Python (Pandas, Matplotlib, Seaborn) |
| Database | MySQL, SQLAlchemy, PyMySQL |
| Querying & Views | SQL (joins, aggregations, views, data-quality checks) |
| Reporting (spreadsheet) | Microsoft Excel (Pivot Tables, Dashboard sheet) |
| Business Intelligence | Power BI Desktop (DAX, data modeling, interactive dashboard) |

## 📂 Dataset

The project uses three linked datasets (based on the IBM/Maven Analytics Telco Customer Churn dataset structure):

| File | Description |
|---|---|
| `telecom_customer_churn.csv` | Raw customer-level data — 7,043 rows × 38 columns covering demographics, account/contract details, subscribed services, charges, and churn status/reason |
| `telecom_zipcode_population.csv` | ZIP-code-level population lookup, joined to customers on `zip_code` for geographic analysis |
| `telecom_data_dictionary.csv` | Field-level data dictionary describing every column in the Customer Churn and Zip Code Population tables |
| `telecom_customer_churn_cleaned.csv` / `telecom_zipcode_population_cleaned.csv` | Cleaned, standardized versions produced by `clean_data.py` (snake_case columns, trimmed text, numeric type coercion) |

**Key fields:** `customer_id`, `gender`, `age`, `city`, `zip_code`, `tenure_in_months`, `contract`, `internet_type`, `payment_method`, `monthly_charge`, `total_revenue`, `customer_status` (Stayed / Churned / Joined), `churn_category`, `churn_reason`.

## 🔄 Project Methodology

The project follows a linear pipeline from raw data to dashboard:

1. **Load & Inspect** (`data_loading.py`) — load raw CSVs, profile shape, dtypes, missing values, and duplicates.
2. **Clean** (`clean_data.py`) — standardize column names, strip whitespace, coerce numeric types, validate customer IDs, flag data-quality issues (e.g. negative monthly charges), and export cleaned CSVs.
3. **Exploratory Data Analysis** (`eda.py`) — compute churn rate, engineer features (`churn_flag`, `age_group`, `tenure_group`, `net_revenue`, `revenue_per_month`), and generate 8 exploratory charts.
4. **Load to Database** (`load_mysql.py`, `database.sql`, `create_tables.sql`) — create the `telecom_churn` MySQL database and `customers` / `zip_population` tables, and load the cleaned data via SQLAlchemy.
5. **SQL Analysis & Quality Checks** (`analysis.sql`, `data_quality.sql`) — churn rate, geographic churn/revenue breakdowns, and duplicate/missing-value validation.
6. **Views for BI** (`views.sql`) — a `vw_customer_geography` SQL view joining customers with ZIP population for direct use in Power BI.
7. **Reporting** — an Excel workbook (`Telecom_Churn_Analysis.xlsx`) with pivot analysis and a dashboard sheet, and a 4-page interactive **Power BI** dashboard (`Telecom_Churn_Dashboard.pbix`).

## 🐍 Python Analysis

- **Data profiling**: shape, dtypes, missing values, unique values, duplicate customer ID checks for both the customer and ZIP population tables.
- **Data quality checks**: negative `monthly_charge` values isolated for review.
- **Churn rate calculation**: churned customers as a percentage of the active base (Joined customers excluded from the denominator since they haven't had a chance to churn or stay).
- **Feature engineering**: `churn_flag` (binary), `age_group` and `tenure_group` bins, `net_revenue` (`total_revenue − total_refunds`), and `revenue_per_month`.
- **Visual EDA**: 8 saved charts — customer status distribution, churn by contract, by internet type, by payment method, by tenure group, by age group, revenue by contract, and top churn reasons.

## 🗄️ SQL Analysis

Implemented in MySQL against the `telecom_churn` database:

- **Schema**: `customers` (38 columns matching the cleaned CSV) and `zip_population` (`zip_code`, `population`), created via `create_tables.sql`.
- **Data quality**: duplicate `customer_id` checks, missing `zip_code` checks, duplicate/missing ZIP population checks (`data_quality.sql`).
- **Core analysis** (`analysis.sql`): total and churned customer counts, overall churn rate, customer-to-ZIP-population joins, churn and revenue by ZIP code, churn by city + population, and churn rate by ZIP — demonstrating joins, `GROUP BY`, boolean aggregation, and calculated business metrics.
- **Reporting view** (`views.sql`): `vw_customer_geography`, a single joined view (customers + population) consumed directly by Power BI.

## 📈 Power BI Dashboard

`Telecom_Churn_Dashboard.pbix` is a 4-page interactive report built on the `customers` and `zip_population` tables:

| Page | Focus | Key Visuals |
|---|---|---|
| **Executive Overview** | Top-line KPIs | Customer Status donut, Churned by Contract, Churn by Internet Type, KPI cards (Total Customers, Churned Customers, Churn Rate %, Total Revenue, Avg. Monthly Charge, Avg. Tenure) |
| **Churn Analysis** | Why customers churn | Churn Rate by Contract, by Internet Type, by Payment Method, Churned by Category, Top 6 Churn Reasons, Tenure vs. Churn Rate trend |
| **Geographic & Population Analysis** | Where churn happens | Top Cities by Customers, Top 5 Cities by Churned Customers, Revenue by City, Customer Distribution treemap, City map |
| **Revenue & Retention** | Revenue impact | Revenue by Contract, Revenue by Internet Type, Top 10 Cities by Revenue, Average Monthly Charge by Status, Average Tenure by Status |

Every page shares global slicers (**Gender, Contract, Internet Type, Payment Method, City**) and in-report page-navigation buttons for a guided, self-service experience.

## 📊 Key Insights

- **Overall churn rate ≈ 28%** (1,869 of 6,589 non-new customers churned).
- **Contract type is the strongest churn driver**: Month-to-Month customers churn at **~46%**, vs. **~11%** for One-Year and just **~3%** for Two-Year contracts.
- **Fiber Optic customers churn more than DSL/Cable**: ~41% churn vs. ~19% (DSL) and ~26% (Cable) — despite Fiber being the most popular service.
- **Payment method matters**: customers paying by Mailed Check (~37%) or Bank Withdrawal (~34%) churn far more than those on Credit Card (~14%).
- **Competitors are the #1 churn driver**: "Competitor had better devices," "Competitor made better offer," and "Competitor offered more data/higher speeds" together account for the largest share of churn reasons, ahead of price or product dissatisfaction.
- **Attitude of support/service staff** is a significant, controllable churn category — distinct from competitive pressure.
- Churn and revenue both show geographic concentration, with a small number of cities contributing disproportionately to both total customers and churned customers.

## 💡 Business Recommendations

- **Incentivize longer contracts**: promote One- and Two-Year contract upgrades (discounts, loyalty perks) to month-to-month customers, since contract length is the single biggest churn lever.
- **Shore up Fiber Optic retention**: investigate service reliability/pricing for Fiber customers specifically, since they churn at nearly double the rate of DSL despite paying a premium.
- **Push customers toward automatic/credit-card payment**: customers on Mailed Check or Bank Withdrawal are markedly higher-risk; billing-method migration campaigns could reduce friction-driven churn.
- **Build a competitive retention playbook**: since "competitor" reasons dominate churn, create win-back offers and proactive competitive-intelligence monitoring for at-risk segments.
- **Invest in customer support training**: "Attitude of support/service person" is a controllable churn category — unlike competitor actions, this is directly addressable through service-quality initiatives.
- **Prioritize retention spend geographically**: focus retention campaigns on the highest-churn, highest-population cities identified in the Geographic Analysis page for the greatest revenue protection per dollar spent.

## ✨ Project Highlights

- 🔗 **Full pipeline**: raw CSV → Python cleaning/EDA → MySQL → SQL analysis/views → Excel & Power BI reporting.
- 🧹 **Rigorous data quality process**: duplicate checks, missing-value profiling, and negative-value validation before any analysis.
- 🧮 **Feature engineering** for tenure/age segmentation and net/per-month revenue metrics.
- 🗄️ **Relational data modeling in MySQL** with a purpose-built reporting view (`vw_customer_geography`) for BI consumption.
- 📈 **4-page interactive Power BI dashboard** with cross-filtering slicers and guided navigation.
- 📊 **Excel companion workbook** with pivot-table analysis and a dashboard sheet for stakeholders without Power BI access.

## 📁 Project Structure

```
telecom-churn-analytics/
├── data/
│   ├── telecom_customer_churn.csv
│   ├── telecom_zipcode_population.csv
│   └── telecom_data_dictionary.csv
├── Python/
│   ├── data_loading.py
│   ├── clean_data.py
│   ├── eda.py
│   ├── load_mysql.py
│   ├── telecom_customer_churn_cleaned.csv
│   └── telecom_zipcode_population_cleaned.csv
├── 04_PYTHON_OUTPUT/
│   └── (EDA charts + telecom_customer_churn_eda.csv)
├── SQL/
│   ├── database.sql
│   ├── create_tables.sql
│   ├── data_quality.sql
│   ├── analysis.sql
│   └── views.sql
├── Excel/
│   └── Telecom_Churn_Analysis.xlsx
├── PowerBI/
│   └── Telecom_Churn_Dashboard.pbix
└── README.md
```

## 🚀 How to Run the Project

1. **Clone the repository** and place the raw CSVs in a `data/` folder.
2. **Python cleaning & EDA**
   ```bash
   pip install pandas matplotlib seaborn sqlalchemy pymysql
   python Python/data_loading.py
   python Python/clean_data.py
   python Python/eda.py
   ```
3. **Load into MySQL**
   - Run `SQL/database.sql` and `SQL/create_tables.sql` in MySQL Workbench (or CLI) to create the database and schema.
   - Update the MySQL username/password/host in `Python/load_mysql.py`, then run it to load the cleaned data:
     ```bash
     python Python/load_mysql.py
     ```
4. **Run SQL analysis**
   - Execute `SQL/data_quality.sql`, `SQL/analysis.sql`, and `SQL/views.sql` in MySQL to reproduce the churn/geographic queries and create the `vw_customer_geography` view.
5. **Open the reports**
   - Open `Excel/Telecom_Churn_Analysis.xlsx` for the pivot-table view.
   - Open `PowerBI/Telecom_Churn_Dashboard.pbix` in Power BI Desktop (point the data source to your MySQL instance or the cleaned CSVs) and refresh.

## 👤 Author

Prepared as a portfolio data analytics project demonstrating the full pipeline from raw data to business-ready insights: **Python (cleaning & EDA) → MySQL & SQL (modeling & analysis) → Excel & Power BI (reporting & visualization)**.

## Images

<img width="1207" height="692" alt="Screenshot 2026-08-24 152832" src="https://github.com/user-attachments/assets/a20f7f2b-5c87-46af-8436-4ed80c297b84" />
<img width="1202" height="684" alt="Screenshot 2026-08-24 152857" src="https://github.com/user-attachments/assets/0fe3051a-4602-4582-b299-d091f57c83e7" />
<img width="1207" height="686" alt="Screenshot 2026-08-24 152917" src="https://github.com/user-attachments/assets/97e67b95-a27e-4be2-b30d-7ec2e4d66aed" />
<img width="1210" height="682" alt="Screenshot 2026-08-24 152953" src="https://github.com/user-attachments/assets/8738b0d4-3bee-46cc-add9-f5a83408d1dd" />



