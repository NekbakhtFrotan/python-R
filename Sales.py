import pandas as pd
import numpy as np

# Function to read the CSV file
def read_file(file_name):
    df = pd.read_csv(file_name)
    return df


# Function to fill missing values
def fill_missing(df, column, value):
    df[column] = df[column].fillna(value)


# Function to clean the data
def clean_data(df):

    # Display the dataset
    print(df)

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Check duplicate Order IDs
    print("\nDuplicate Order IDs:")
    print(df[df.duplicated(subset="OrderID")])

    # Check invalid Quantity
    print("\nInvalid Quantity:")
    print(df[df["Quantity"] < 0])

    # Check invalid Unit Price
    print("\nInvalid Unit Price:")
    print(df[df["UnitPrice"] < 0])

    # Check invalid Month
    valid_months = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    print("\nInvalid Months:")
    print(df[~df["Month"].isin(valid_months) & df["Month"].notna()])

    # Replace invalid values with NaN
    df.loc[df["Quantity"] < 0, "Quantity"] = np.nan
    df.loc[df["UnitPrice"] < 0, "UnitPrice"] = np.nan
    df.loc[~df["Month"].isin(valid_months), "Month"] = np.nan

    # Fill missing values
    fill_missing(df, "Month", "Unknown")
    fill_missing(df, "Product", "Unknown")
    fill_missing(df, "Region", "Unknown")
    fill_missing(df, "Quantity", df["Quantity"].mean())
    fill_missing(df, "UnitPrice", df["UnitPrice"].median())

    # Remove duplicate Order IDs
    df = df.drop_duplicates(subset="OrderID")

    # Clean Product and Region
    df["Product"] = df["Product"].str.strip().str.title()
    df["Region"] = df["Region"].str.strip().str.title()

    # Compute Total Sales
    df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

    # Validate cleaned data
    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    print("\nDuplicate Order IDs After Cleaning:")
    print(df.duplicated(subset="OrderID").sum())

    return df


# Function to save the cleaned file
def save_file(df, file_name):
    df.to_csv(file_name, index=False)
    print("\nFile saved successfully.")


# Main Program
sales = read_file("sales_dirty.csv")

sales = clean_data(sales)

print("\nCleaned Dataset:")
print(sales.to_string())

save_file(sales, "Sales_cleaned.csv")