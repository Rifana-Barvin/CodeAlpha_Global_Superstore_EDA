# Global Superstore Exploratory Data Analysis

## Project Overview

This project performs Exploratory Data Analysis (EDA) on a 1,000-record sample of Global Superstore sales data.

The objective is to clean the dataset, analyze sales and profit patterns, identify important business insights, and create visualizations using Python.

This project was completed as part of the CodeAlpha Data Analytics Internship.

## Objectives

- Clean and prepare the dataset
- Handle missing values
- Check duplicate records
- Convert date columns into proper date format
- Create useful analytical features
- Analyze sales, profit, and quantity
- Compare product categories and sub-categories
- Analyze regional performance
- Study yearly and monthly sales trends
- Analyze the relationship between discount and profit
- Analyze customer segments
- Analyze shipping modes
- Create meaningful visualizations

## Dataset

The project uses a 1,000-record sample of Global Superstore sales data.

The dataset contains information about:

- Orders
- Customers
- Products
- Categories
- Regions
- Sales
- Quantity
- Discounts
- Profit
- Shipping costs
- Shipping modes
- Order dates
- Ship dates

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Data Cleaning

The following preprocessing steps were performed:

1. Loaded the CSV dataset using Pandas.
2. Converted `Order Date` and `Ship Date` into datetime format.
3. Checked missing values.
4. Removed the `Postal Code` column because it contained a large number of missing values and was not required for the main analysis.
5. Checked for duplicate records.
6. Created additional features:
   - Year
   - Month
   - Month Name
   - Profit Margin
   - Shipping Days
7. Verified the final dataset for missing values and correct data types.

The original dataset contained 24 columns and 1,000 records.

After preprocessing and feature engineering, the dataset contained 28 columns.

## Key Business Metrics

| Metric | Value |
|---|---:|
| Total Sales | $1,710,971.47 |
| Total Profit | $288,920.44 |
| Total Quantity Sold | 5,558 |
| Average Discount | 9.28% |
| Average Profit Margin | 15.15% |
| Average Shipping Days | 3.02 |

## Key Insights

### Category Performance

Technology was the strongest category in terms of both sales and profit.

- Technology Sales: $756,983.02
- Technology Profit: $145,068.68
- Furniture Sales: $601,492.31
- Office Supplies Sales: $352,496.14

### Regional Performance

Western Europe generated the highest sales among the regions:

- Western Europe Sales: $259,576.28

Eastern Asia generated the highest profit:

- Eastern Asia Profit: $37,911.16

This shows that the region with the highest sales was not necessarily the region with the highest profit.

### Sub-Category Performance

Phones were the strongest sub-category.

- Phone Sales: $417,939.31
- Phone Profit: $75,119.47

The Supplies sub-category recorded a small loss:

- Supplies Profit: -$89.85

### Yearly Performance

Sales increased across the analyzed years.

2015 recorded the highest:

- Sales: $607,727.03
- Profit: $104,492.36
- Quantity Sold: 2,054

### Monthly Performance

December recorded the highest monthly sales and profit:

- Sales: $225,442.22
- Profit: $42,461.27

### Discount and Profit

The correlation between discount and profit was:

`-0.5052`

The analysis shows a negative association between discount and profit in this dataset. Higher discount levels were generally associated with lower profitability.

For example, a 50% discount level recorded a profit of:

`-$20,859.36`

Correlation does not by itself prove that discounts caused the reduction in profit.

### Customer Segment

Consumer customers generated the highest sales and profit.

- Consumer Sales: $873,512.42
- Corporate Sales: $524,287.05
- Home Office Sales: $313,172.00

### Shipping Mode

Standard Class had the highest number of orders.

Average shipping time by mode:

- Standard Class: 4.92 days
- Second Class: 2.81 days
- First Class: 2.09 days
- Same Day: 0.02 days

## Visualizations

The project includes the following visualizations:

1. Sales by Category
2. Profit by Category
3. Yearly Sales Trend
4. Monthly Sales Trend
5. Profit by Sub-Category
6. Discount vs Profit
7. Sales by Customer Segment
8. Profit by Region

All charts are available in the `outputs` folder.

## Project Structure

```text
Global_Superstore_EDA/
│
├── data/
│   └── superstore.csv
│
├── outputs/
│   ├── discount_vs_profit.png
│   ├── monthly_sales_trend.png
│   ├── profit_by_category.png
│   ├── profit_by_region.png
│   ├── profit_by_subcategory.png
│   ├── sales_by_category.png
│   ├── sales_by_segment.png
│   └── yearly_sales_trend.png
│
├── .gitignore
├── eda.py
├── requirements.txt
└── README.md