import pandas as pd

# Read the dataset
sales = pd.read_csv("sales_dirty_dataset.csv")

# Display basic information
print("Shape:", sales.shape)

print("\nColumns")
print(sales.columns)

print("\nDataset Information")
sales.info()

print("\nMissing Values")
print(sales.isnull().sum())

# Display rows with missing values
missing_rows = sales[sales.isnull().any(axis=1)]

print("\nRows with Missing Values")
print(missing_rows)

# Display duplicate Order IDs
duplicate_orders = sales[
    sales.duplicated(subset="OrderID", keep=False)
]

print("\nDuplicate Order IDs")
print(duplicate_orders)

# Display invalid months
valid_months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

invalid_months = sales[
    ~sales["Month"].astype(str).str.strip().str.title().isin(valid_months)
]

print("\nInvalid Months")
print(invalid_months[["OrderID", "Month"]])

# Display invalid quantity
quantity = pd.to_numeric(
    sales["Quantity"],
    errors="coerce"
)

invalid_quantity = sales[
    (quantity < 1) |
    (quantity > 100) |
    (quantity.isna())
]

print("\nInvalid Quantity")
print(invalid_quantity[["OrderID", "Quantity"]])

# Display invalid unit price
unit_price = pd.to_numeric(
    sales["UnitPrice"],
    errors="coerce"
)

invalid_price = sales[
    (unit_price < 1) |
    (unit_price > 10000) |
    (unit_price.isna())
]

print("\nInvalid Unit Price")
print(invalid_price[["OrderID", "UnitPrice"]])

# Display unique months
print("\nUnique Months")
print(sales["Month"].unique())

# Display unique regions
print("\nUnique Regions")
print(sales["Region"].unique())

# Display unique products
print("\nUnique Products")
print(sales["Product"].unique())