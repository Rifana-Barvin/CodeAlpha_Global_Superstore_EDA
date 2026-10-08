import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. LOAD DATASET
# ==============================

df = pd.read_csv("data/superstore.csv")

print("Original Shape:", df.shape)


# ==============================
# 2. CONVERT DATE COLUMNS
# ==============================

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nDate columns converted successfully.")


# ==============================
# 3. CHECK MISSING VALUES
# ==============================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# ==============================
# 4. HANDLE POSTAL CODE
# ==============================

# Postal Code has many missing values.
# Since it is not essential for our main sales analysis,
# we remove this column.

df.drop(columns=["Postal Code"], inplace=True)


# ==============================
# 5. CHECK DUPLICATES
# ==============================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

if duplicates > 0:
    df.drop_duplicates(inplace=True)


# ==============================
# 6. CREATE NEW FEATURES
# ==============================

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.month_name()

df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days


# ==============================
# 7. FINAL DATASET INFORMATION
# ==============================

print("\nFinal Shape:", df.shape)

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFinal Data Types:")
print(df.dtypes)

print("\nFirst 5 Rows After Cleaning:")
print(df.head())
# ==============================
# 8. BASIC BUSINESS ANALYSIS
# ==============================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
average_discount = df["Discount"].mean()
average_profit_margin = df["Profit Margin"].mean()
average_shipping_days = df["Shipping Days"].mean()

print("\n" + "=" * 40)
print("BASIC BUSINESS ANALYSIS")
print("=" * 40)

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Discount: {average_discount:.2%}")
print(f"Average Profit Margin: {average_profit_margin:.2f}%")
print(f"Average Shipping Days: {average_shipping_days:.2f}")
# ==============================
# 9. CATEGORY ANALYSIS
# ==============================

category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)

print("\n" + "=" * 40)
print("CATEGORY ANALYSIS")
print("=" * 40)

print(category_analysis)
# ==============================
# 10. REGION ANALYSIS
# ==============================

region_analysis = df.groupby("Region").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Profit", ascending=False)

print("\n" + "=" * 40)
print("REGION ANALYSIS")
print("=" * 40)

print(region_analysis)
# ==============================
# 11. SUB-CATEGORY ANALYSIS
# ==============================

subcategory_analysis = df.groupby("Sub-Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Profit", ascending=False)

print("\n" + "=" * 40)
print("SUB-CATEGORY ANALYSIS")
print("=" * 40)

print(subcategory_analysis)
# ==============================
# 12. YEARLY ANALYSIS
# ==============================

yearly_analysis = df.groupby("Year").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_index()

print("\n" + "=" * 40)
print("YEARLY ANALYSIS")
print("=" * 40)
print(yearly_analysis)


# ==============================
# 13. MONTHLY ANALYSIS
# ==============================

monthly_analysis = df.groupby("Month").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_index()

print("\n" + "=" * 40)
print("MONTHLY ANALYSIS")
print("=" * 40)
print(monthly_analysis)
# ==============================
# 14. DISCOUNT VS PROFIT ANALYSIS
# ==============================

discount_analysis = df.groupby("Discount").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_index()

print("\n" + "=" * 40)
print("DISCOUNT VS PROFIT ANALYSIS")
print("=" * 40)
print(discount_analysis)


# Correlation between discount and profit
discount_profit_correlation = df["Discount"].corr(df["Profit"])

print("\nDiscount-Profit Correlation:")
print(f"{discount_profit_correlation:.4f}")
# ==============================
# 15. CUSTOMER SEGMENT ANALYSIS
# ==============================

segment_analysis = df.groupby("Segment").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)

print("\n" + "=" * 40)
print("CUSTOMER SEGMENT ANALYSIS")
print("=" * 40)
print(segment_analysis)
# ==============================
# 16. SHIPPING MODE ANALYSIS
# ==============================

shipping_analysis = df.groupby("Ship Mode").agg(
    Orders=("Order ID", "nunique"),
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Average_Shipping_Days=("Shipping Days", "mean")
).sort_values("Sales", ascending=False)

print("\n" + "=" * 40)
print("SHIPPING MODE ANALYSIS")
print("=" * 40)
print(shipping_analysis)
# ==============================
# 17. VISUALIZATIONS
# ==============================

import os

os.makedirs("outputs", exist_ok=True)

sns.set_theme(style="whitegrid")

# ------------------------------
# 1. Sales by Category
# ------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=category_analysis.reset_index(),
    x="Category",
    y="Sales"
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("outputs/sales_by_category.png")
plt.close()


# ------------------------------
# 2. Profit by Category
# ------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=category_analysis.reset_index(),
    x="Category",
    y="Profit"
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("outputs/profit_by_category.png")
plt.close()


# ------------------------------
# 3. Yearly Sales Trend
# ------------------------------

plt.figure(figsize=(8, 5))

sns.lineplot(
    data=yearly_analysis.reset_index(),
    x="Year",
    y="Sales",
    marker="o"
)

plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("outputs/yearly_sales_trend.png")
plt.close()


# ------------------------------
# 4. Monthly Sales Trend
# ------------------------------

plt.figure(figsize=(8, 5))

sns.lineplot(
    data=monthly_analysis.reset_index(),
    x="Month",
    y="Sales",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("outputs/monthly_sales_trend.png")
plt.close()


# ------------------------------
# 5. Profit by Sub-Category
# ------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=subcategory_analysis.reset_index(),
    x="Profit",
    y="Sub-Category"
)

plt.title("Profit by Sub-Category")
plt.xlabel("Profit")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.savefig("outputs/profit_by_subcategory.png")
plt.close()


# ------------------------------
# 6. Discount vs Profit
# ------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit"
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("outputs/discount_vs_profit.png")
plt.close()


# ------------------------------
# 7. Sales by Customer Segment
# ------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=segment_analysis.reset_index(),
    x="Segment",
    y="Sales"
)

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("outputs/sales_by_segment.png")
plt.close()


# ------------------------------
# 8. Profit by Region
# ------------------------------

plt.figure(figsize=(10, 8))

sns.barplot(
    data=region_analysis.reset_index(),
    x="Profit",
    y="Region"
)

plt.title("Profit by Region")
plt.xlabel("Profit")
plt.ylabel("Region")

plt.tight_layout()
plt.savefig("outputs/profit_by_region.png")
plt.close()


print("\n========================================")
print("VISUALIZATIONS CREATED SUCCESSFULLY")
print("========================================")

print("Charts saved in the 'outputs' folder.")