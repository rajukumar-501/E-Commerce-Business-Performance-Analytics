# ============================================================
# MYNTRA DATA ANALYTICS PROJECT
# Python - Data Cleaning & Exploratory Data Analysis
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------------------------------------
# 1. FILE PATHS
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = BASE_DIR / "Dataset" / "Myntra_Analysis.csv"
CLEANED_PATH = BASE_DIR / "Dataset" / "Myntra_Cleaned.csv"

print("=" * 60)
print("MYNTRA DATA ANALYTICS - PYTHON")
print("=" * 60)


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ------------------------------------------------------------
# 3. VIEW BASIC INFORMATION
# ------------------------------------------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 4. REMOVE EXTRA SPACES FROM COLUMN NAMES
# ------------------------------------------------------------

df.columns = df.columns.str.strip()


# ------------------------------------------------------------
# 5. REMOVE EXTRA SPACES FROM TEXT COLUMNS
# ------------------------------------------------------------

text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()


# ------------------------------------------------------------
# 6. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\nMissing Values:")
missing_values = df.isnull().sum()
print(missing_values)


# ------------------------------------------------------------
# 7. CHECK DUPLICATES
# ------------------------------------------------------------

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows:", duplicate_count)

if duplicate_count > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.")


# ------------------------------------------------------------
# 8. CHECK DUPLICATE ORDER IDs
# ------------------------------------------------------------

duplicate_orders = df["Order_ID"].duplicated().sum()

print("\nDuplicate Order IDs:", duplicate_orders)


# ------------------------------------------------------------
# 9. CONVERT DATE COLUMN
# ------------------------------------------------------------

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

print("\nInvalid Dates:", df["Order_Date"].isna().sum())


# ------------------------------------------------------------
# 10. CHECK NUMERIC COLUMNS
# ------------------------------------------------------------

numeric_columns = [
    "MRP",
    "Discount_Percent",
    "Selling_Price",
    "Quantity",
    "Revenue",
    "Rating",
    "Review_Count",
    "Refund_Amount"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# ------------------------------------------------------------
# 11. CHECK IMPORTANT MISSING VALUES
# ------------------------------------------------------------

important_columns = [
    "Order_ID",
    "Order_Date",
    "Category",
    "Brand",
    "Product",
    "MRP",
    "Selling_Price",
    "Quantity",
    "Revenue"
]

print("\nMissing values in important columns:")

for col in important_columns:
    print(f"{col}: {df[col].isnull().sum()}")


# ------------------------------------------------------------
# 12. CHECK INVALID PRICES
# ------------------------------------------------------------

invalid_prices = df[
    (df["MRP"] <= 0) |
    (df["Selling_Price"] <= 0) |
    (df["Selling_Price"] > df["MRP"])
]

print("\nInvalid Price Records:", len(invalid_prices))


# ------------------------------------------------------------
# 13. CHECK INVALID DISCOUNTS
# ------------------------------------------------------------

invalid_discount = df[
    (df["Discount_Percent"] < 0) |
    (df["Discount_Percent"] > 100)
]

print("Invalid Discount Records:", len(invalid_discount))


# ------------------------------------------------------------
# 14. CHECK INVALID QUANTITY
# ------------------------------------------------------------

invalid_quantity = df[
    df["Quantity"] <= 0
]

print("Invalid Quantity Records:", len(invalid_quantity))


# ------------------------------------------------------------
# 15. CHECK INVALID RATINGS
# ------------------------------------------------------------

invalid_rating = df[
    (df["Rating"] < 1) |
    (df["Rating"] > 5)
]

print("Invalid Rating Records:", len(invalid_rating))


# ------------------------------------------------------------
# 16. CHECK REVENUE
# ------------------------------------------------------------

df["Calculated_Revenue"] = (
    df["Selling_Price"] * df["Quantity"]
)

df["Revenue_Check"] = np.where(
    np.isclose(
        df["Revenue"],
        df["Calculated_Revenue"]
    ),
    "OK",
    "CHECK"
)

print(
    "\nRevenue mismatches:",
    (df["Revenue_Check"] == "CHECK").sum()
)


# ------------------------------------------------------------
# 17. CHECK REFUND AMOUNT
# ------------------------------------------------------------

invalid_refund = df[
    df["Refund_Amount"] < 0
]

print("Invalid Refund Records:", len(invalid_refund))


# ------------------------------------------------------------
# 18. STANDARDIZE CATEGORIES
# ------------------------------------------------------------

df["Category"] = df["Category"].str.strip()


# ------------------------------------------------------------
# 19. STANDARDIZE GENDER
# ------------------------------------------------------------

df["Gender"] = df["Gender"].str.strip()


# ------------------------------------------------------------
# 20. STANDARDIZE RETURN COLUMN
# ------------------------------------------------------------

df["Returned"] = df["Returned"].str.strip().str.title()


# ------------------------------------------------------------
# 21. STANDARDIZE ORDER STATUS
# ------------------------------------------------------------

df["Order_Status"] = (
    df["Order_Status"]
    .str.strip()
    .str.title()
)


# ------------------------------------------------------------
# 22. CREATE NEW ANALYTICS COLUMNS
# ------------------------------------------------------------

# Discount Amount
df["Discount_Amount"] = (
    df["MRP"] - df["Selling_Price"]
)

# Net Revenue
df["Net_Revenue"] = (
    df["Revenue"] - df["Refund_Amount"]
)

# Year
df["Year"] = df["Order_Date"].dt.year

# Month Number
df["Month_Number"] = df["Order_Date"].dt.month

# Month Name
df["Month"] = df["Order_Date"].dt.strftime("%b")

# Quarter
df["Quarter"] = (
    "Q" + df["Order_Date"].dt.quarter.astype(str)
)


# ------------------------------------------------------------
# 23. DATA SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA SUMMARY")
print("=" * 60)

print("\nTotal Orders:")
print(df["Order_ID"].nunique())

print("\nTotal Revenue:")
print(f"₹{df['Revenue'].sum():,.2f}")

print("\nNet Revenue:")
print(f"₹{df['Net_Revenue'].sum():,.2f}")

print("\nTotal Units Sold:")
print(df["Quantity"].sum())

print("\nAverage Rating:")
print(round(df["Rating"].mean(), 2))

print("\nTotal Refund:")
print(f"₹{df['Refund_Amount'].sum():,.2f}")


# ------------------------------------------------------------
# 24. CATEGORY ANALYSIS
# ------------------------------------------------------------

category_analysis = (
    df.groupby("Category")
    .agg(
        Revenue=("Revenue", "sum"),
        Units_Sold=("Quantity", "sum"),
        Average_Rating=("Rating", "mean"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Revenue", ascending=False)
)

print("\nCategory Analysis:")
print(category_analysis)


# ------------------------------------------------------------
# 25. BRAND ANALYSIS
# ------------------------------------------------------------

brand_analysis = (
    df.groupby("Brand")
    .agg(
        Revenue=("Revenue", "sum"),
        Units_Sold=("Quantity", "sum"),
        Average_Rating=("Rating", "mean"),
        Orders=("Order_ID", "nunique")
    )
    .sort_values("Revenue", ascending=False)
)

print("\nTop 10 Brands:")
print(brand_analysis.head(10))


# ------------------------------------------------------------
# 26. TOP 10 PRODUCTS
# ------------------------------------------------------------

product_analysis = (
    df.groupby("Product")
    .agg(
        Revenue=("Revenue", "sum"),
        Units_Sold=("Quantity", "sum"),
        Average_Rating=("Rating", "mean")
    )
    .sort_values("Revenue", ascending=False)
)

print("\nTop 10 Products:")
print(product_analysis.head(10))


# ------------------------------------------------------------
# 27. MONTHLY SALES
# ------------------------------------------------------------

monthly_sales = (
    df.groupby(["Year", "Month_Number", "Month"])
    ["Revenue"]
    .sum()
    .reset_index()
    .sort_values(["Year", "Month_Number"])
)

print("\nMonthly Revenue:")
print(monthly_sales)


# ------------------------------------------------------------
# 28. RETURN ANALYSIS
# ------------------------------------------------------------

return_analysis = (
    df.groupby("Category")
    .agg(
        Total_Orders=("Order_ID", "nunique"),
        Returned_Orders=(
            "Returned",
            lambda x: (x == "Yes").sum()
        )
    )
)

return_analysis["Return_Rate"] = (
    return_analysis["Returned_Orders"] /
    return_analysis["Total_Orders"] * 100
)

print("\nReturn Analysis:")
print(return_analysis.sort_values(
    "Return_Rate",
    ascending=False
))


# ------------------------------------------------------------
# 29. CITY ANALYSIS
# ------------------------------------------------------------

city_analysis = (
    df.groupby("City")
    .agg(
        Revenue=("Revenue", "sum"),
        Orders=("Order_ID", "nunique"),
        Units_Sold=("Quantity", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\nCity Analysis:")
print(city_analysis)


# ------------------------------------------------------------
# 30. SAVE CLEANED DATASET
# ------------------------------------------------------------

# Remove temporary validation columns
df = df.drop(
    columns=["Calculated_Revenue"],
    errors="ignore"
)

df.to_csv(
    CLEANED_PATH,
    index=False
)

print("\nCleaned dataset saved to:")
print(CLEANED_PATH)


# ============================================================
# 31. VISUALIZATION 1 - MONTHLY REVENUE
# ============================================================

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Month"],
    monthly_sales["Revenue"],
    marker="o"
)

plt.title("Myntra Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ============================================================
# 32. VISUALIZATION 2 - CATEGORY REVENUE
# ============================================================

plt.figure(figsize=(10, 5))

plt.bar(
    category_analysis.index,
    category_analysis["Revenue"]
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.xticks(
    rotation=30,
    ha="right"
)

plt.tight_layout()

plt.show()


# ============================================================
# 33. VISUALIZATION 3 - TOP 10 BRANDS
# ============================================================

top_brands = brand_analysis.head(10)

plt.figure(figsize=(10, 5))

plt.barh(
    top_brands.index[::-1],
    top_brands["Revenue"][::-1]
)

plt.title("Top 10 Brands by Revenue")
plt.xlabel("Revenue")

plt.tight_layout()

plt.show()


# ============================================================
# 34. FINAL MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("PYTHON ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nNext step:")
print("Import Myntra_Cleaned.csv into SQL.")