# 🛍️ Myntra Data Analytics Project

## 📌 Project Overview

The **Myntra Data Analytics Project** is an end-to-end e-commerce data analytics project designed to analyze sales, products, brands, discounts, ratings, returns, and order performance.

The project uses **Excel, Python, Microsoft SQL Server, and Power BI** to transform raw Myntra-style e-commerce data into meaningful business insights through data cleaning, analysis, visualization, and an interactive dashboard.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Analyze overall sales and revenue performance
* Identify high-performing product categories
* Analyze brand-wise revenue and sales
* Identify top-performing products
* Analyze monthly revenue trends
* Understand discount patterns
* Analyze product ratings and reviews
* Measure order returns and refunds
* Analyze sales by city
* Analyze payment methods
* Create an interactive Power BI overview dashboard
* Develop an end-to-end data analytics workflow

---

## 🗂️ Project Structure

```text
Myntra-Data-Analytics/
│
├── Dataset/
│   ├── Myntra_Analysis.csv
│   └── Myntra_Cleaned.csv
│
├── SQL/
│   └── Myntra_Analysis.sql
│
├── Power BI/
│   └── Myntra_Analysis.pbix
│
├── Excel/
│   └── Myntra_Analysis.xlsx
│
├── Python/
│   └── Myntra_Analysis.py
│
└── README.md
```

---

# 📊 Dataset

The project uses a **5,000-row Myntra-style e-commerce dataset**.

### Dataset Columns

| Column             | Description             |
| ------------------ | ----------------------- |
| `Order_ID`         | Unique order identifier |
| `Order_Date`       | Date of order           |
| `City`             | Customer city           |
| `Category`         | Product category        |
| `Brand`            | Product brand           |
| `Product`          | Product name            |
| `Gender`           | Target gender           |
| `MRP`              | Maximum Retail Price    |
| `Discount_Percent` | Discount percentage     |
| `Selling_Price`    | Final selling price     |
| `Quantity`         | Number of units ordered |
| `Revenue`          | Order revenue           |
| `Rating`           | Product rating          |
| `Review_Count`     | Number of reviews       |
| `Payment_Method`   | Payment method          |
| `Order_Status`     | Order status            |
| `Returned`         | Return indicator        |
| `Refund_Amount`    | Refund amount           |

Additional calculated fields are used during analysis, including:

* Discount Amount
* Net Revenue
* Year
* Month
* Month Number
* Quarter

---

# 🧹 Excel Data Cleaning

Excel is used for the initial data cleaning and validation process.

### Cleaning Activities

* Remove duplicate records
* Check duplicate Order IDs
* Check missing values
* Format dates
* Standardize category names
* Standardize brand names
* Validate gender values
* Validate MRP and selling price
* Validate discount percentages
* Validate quantity
* Validate revenue
* Validate ratings
* Validate refund amounts
* Create calculated columns

### Excel Workbook

```text
Excel/Myntra_Analysis.xlsx
```

The workbook contains:

```text
Raw_Data
Cleaned_Data
Data_Quality
```

---

# 🐍 Python Data Analysis

Python is used for data cleaning, exploratory data analysis, business analysis, and visualization.

### Libraries Used

```text
Pandas
NumPy
Matplotlib
```

Install the libraries using:

```bash
pip install pandas numpy matplotlib
```

### Python Analysis Includes

* Dataset inspection
* Missing-value analysis
* Duplicate detection
* Data-type validation
* Price validation
* Discount validation
* Revenue validation
* Rating validation
* Refund validation
* Category analysis
* Brand analysis
* Product analysis
* Monthly revenue analysis
* Return analysis
* City analysis
* Revenue visualizations

### Python File

```text
Python/Myntra_Analysis.py
```

---

# 🗄️ Microsoft SQL Server Analysis

Microsoft SQL Server is used for structured business analysis and SQL querying.

### Database

```text
Myntra_Analytics
```

### Main Table

```text
Myntra_Analysis
```

### SQL Analysis Includes

* Total revenue
* Total orders
* Total units sold
* Average rating
* Total refunds
* Net revenue
* Average order value
* Category performance
* Brand performance
* Top 10 brands
* Top 10 products
* Monthly revenue
* Discount analysis
* Return analysis
* Return rate
* City-wise performance
* Payment method analysis
* Gender analysis
* Order status analysis
* Rating analysis

### SQL File

```text
SQL/Myntra_Analysis.sql
```

---

# 📈 Power BI Dashboard

Power BI is used to create the final interactive **Myntra Overview Dashboard**.

The project contains **one main Overview page**.

## Dashboard KPIs

The dashboard includes:

* 💰 Total Revenue
* 🛒 Total Orders
* 📦 Total Units Sold
* 💵 Average Order Value
* ⭐ Average Rating
* 🔄 Return Rate
* 💸 Total Refund
* 🏷️ Average Discount

---

## 📊 Dashboard Visualizations

### 1. Monthly Revenue

A line chart showing revenue trends over time.

### 2. Category Revenue

A donut chart showing revenue contribution by product category.

### 3. Top 10 Brands

A bar chart showing the highest-revenue brands.

### 4. Top 10 Products

A table showing:

* Product
* Brand
* Category
* Units Sold
* Revenue
* Rating

---

# 🎛️ Dashboard Filters

The Overview dashboard contains interactive filters for:

* 📅 Date
* 🏷️ Category
* 🏢 Brand
* 👤 Gender
* 🏙️ City
* 💳 Payment Method
* 📦 Order Status
* ⭐ Rating

The filters are positioned on the **left side of the dashboard**.

---

# 📐 Power BI DAX Measures

Important measures used in the project include:

```DAX
Total Revenue =
SUM(Myntra_Analysis[Revenue])
```

```DAX
Net Revenue =
SUM(Myntra_Analysis[Net_Revenue])
```

```DAX
Total Orders =
DISTINCTCOUNT(Myntra_Analysis[Order_ID])
```

```DAX
Total Units Sold =
SUM(Myntra_Analysis[Quantity])
```

```DAX
Average Rating =
AVERAGE(Myntra_Analysis[Rating])
```

```DAX
Average Order Value =
DIVIDE(
    [Total Revenue],
    [Total Orders],
    0
)
```

```DAX
Returned Orders =
CALCULATE(
    [Total Orders],
    Myntra_Analysis[Returned] = "Yes"
)
```

```DAX
Return Rate =
DIVIDE(
    [Returned Orders],
    [Total Orders],
    0
)
```

```DAX
Total Refund =
SUM(Myntra_Analysis[Refund_Amount])
```

```DAX
Total Discount Amount =
SUM(Myntra_Analysis[Discount_Amount])
```

---

# 🎨 Dashboard Design

The Power BI dashboard follows a modern Myntra-inspired e-commerce visual style.

### Design Elements

* Pink and magenta accents
* White cards
* Dark navigation/filter sidebar
* Rounded cards
* Soft shadows
* Clean typography
* Interactive slicers
* KPI cards
* Modern charts
* Minimal and organized layout

---

# 🔄 Project Workflow

```text
                RAW DATA
                   │
                   ▼
              CSV DATASET
                   │
                   ▼
                EXCEL
          Data Cleaning & Validation
                   │
                   ▼
                PYTHON
        EDA & Data Analysis
                   │
                   ▼
           MICROSOFT SQL SERVER
        Business Queries & Analysis
                   │
                   ▼
               POWER BI
          Interactive Dashboard
                   │
                   ▼
             BUSINESS INSIGHTS
```

---

# 💡 Key Business Questions

This project answers questions such as:

1. What is the total revenue?
2. How many orders were placed?
3. How many units were sold?
4. Which categories generate the most revenue?
5. Which brands perform strongly by revenue?
6. Which products generate the most revenue?
7. How does revenue change month by month?
8. What is the average order value?
9. What is the average product rating?
10. Which categories have higher return rates?
11. How much revenue is refunded?
12. Which cities generate higher revenue?
13. Which payment methods are used across orders?
14. How do discounts relate to sales?
15. What percentage of orders are returned?

---

# 🛠️ Tools & Technologies

| Tool                             | Purpose                      |
| -------------------------------- | ---------------------------- |
| **Microsoft Excel**              | Data cleaning and validation |
| **Python**                       | EDA and visualization        |
| **Pandas**                       | Data manipulation            |
| **NumPy**                        | Numerical analysis           |
| **Matplotlib**                   | Data visualization           |
| **Microsoft SQL Server**         | Database and SQL analysis    |
| **SQL Server Management Studio** | SQL development              |
| **Power BI**                     | Interactive dashboard        |
| **DAX**                          | Power BI calculations        |

---

# 📂 Final Project Files

```text
Dataset/
    Myntra_Analysis.csv

Excel/
    Myntra_Analysis.xlsx

Python/
    Myntra_Analysis.py

SQL/
    Myntra_Analysis.sql

Power BI/
    Myntra_Analysis.pbix
```

---

# 🚀 How to Run the Project

## Step 1 — Dataset

Place the dataset inside:

```text
Dataset/Myntra_Analysis.csv
```

## Step 2 — Excel

Open:

```text
Excel/Myntra_Analysis.xlsx
```

Perform data validation and cleaning.

## Step 3 — Python

Install dependencies:

```bash
pip install pandas numpy matplotlib
```

Run:

```bash
python Python/Myntra_Analysis.py
```

## Step 4 — SQL Server

Open SQL Server Management Studio.

Create:

```text
Myntra_Analytics
```

Import the cleaned dataset and execute:

```text
SQL/Myntra_Analysis.sql
```

## Step 5 — Power BI

Open:

```text
Power BI/Myntra_Analysis.pbix
```

Connect Power BI to the SQL Server database and refresh the data.

---

# 📌 Project Outcome

The final result is an end-to-end **Myntra E-Commerce Data Analytics Dashboard** that transforms raw transactional data into structured analysis and interactive business reporting.

The project demonstrates practical skills in:

```text
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
SQL Querying
      ↓
Data Modeling
      ↓
DAX
      ↓
Data Visualization
      ↓
Business Analytics
```

---

## 👩‍💻 Author

**Myntra Data Analytics Project**

**Tools:** Excel | Python | SQL Server | Power BI

**Dataset Size:** 5,000 records

**Project Type:** E-Commerce Data Analytics
