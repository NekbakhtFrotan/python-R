import pandas as pd
import numpy as np

# Read the dataset
sales = pd.read_csv("sales_dirty_dataset.csv")

# Create a copy
sales_clean = sales.copy()

# Remove duplicate Order IDs
sales_clean = sales_clean.drop_duplicates(
    subset="OrderID",
    keep="first"
)

print("Shape after removing duplicates:")
print(sales_clean.shape)

# Clean month
sales_clean["Month"] = (
    sales_clean["Month"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

valid_months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales_clean.loc[
    ~sales_clean["Month"].isin(valid_months),
    "Month"
] = "Unknown"

# Clean region
sales_clean["Region"] = (
    sales_clean["Region"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

# Clean product
sales_clean["Product"] = (
    sales_clean["Product"]
    .astype("string")
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

# Convert columns to numeric
numeric_columns = [
    "Quantity",
    "UnitPrice"
]

for column in numeric_columns:
    sales_clean[column] = pd.to_numeric(
        sales_clean[column],
        errors="coerce"
    )

# Clean quantity
valid_quantity = sales_clean["Quantity"].between(1, 100)

quantity_median = sales_clean.loc[
    valid_quantity,
    "Quantity"
].median()

sales_clean.loc[
    ~valid_quantity |
    sales_clean["Quantity"].isna(),
    "Quantity"
] = quantity_median

sales_clean["Quantity"] = (
    sales_clean["Quantity"]
    .round()
    .astype(int)
)

# Clean unit price
valid_price = sales_clean["UnitPrice"].between(1, 10000)

price_median = sales_clean.loc[
    valid_price,
    "UnitPrice"
].median()

sales_clean.loc[
    ~valid_price |
    sales_clean["UnitPrice"].isna(),
    "UnitPrice"
] = price_median

sales_clean["UnitPrice"] = (
    sales_clean["UnitPrice"]
    .round(2)
)

# Calculate total sales
sales_clean["TotalSales"] = (
    sales_clean["Quantity"] *
    sales_clean["UnitPrice"]
).round(2)

# Check missing values
print("\nMissing Values")
print(sales_clean.isnull().sum())

# Check duplicate Order IDs
print("\nDuplicate Order IDs")
print(sales_clean["OrderID"].duplicated().sum())

# Validate cleaned data
print("\nValidation")
print("Quantity:", sales_clean["Quantity"].between(1, 100).all())
print("Unit Price:", sales_clean["UnitPrice"].between(1, 10000).all())
print("Month:", sales_clean["Month"].isin(valid_months + ["Unknown"]).all())

# Show cleaned data
print("\nFirst 5 Rows of Cleaned Dataset")
print(sales_clean.head())

# Save the cleaned dataset
sales_clean.to_csv(
    "sales_cleaned_dataset.csv",
    index=False
)

print("\nSales dataset cleaned successfully!")