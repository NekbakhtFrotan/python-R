import numpy as np
import pandas as pd


# Function to read the file
def read_file(file_name):
    df = pd.read_csv(file_name)
    return df


# Function to fill missing values
def fill_missing(df, column, value):
    df[column] = df[column].fillna(value)


# Function to clean the data
def clean_data(df):

    # Check missing values
    print(df.isnull().sum())

    # Check invalid data
    print(df[(df["Age"] < 0) | (df["Age"] > 100)])
    print(df[(df["StudyHours"] < 0) | (df["StudyHours"] > 24)])
    print(df[(df["Attendance"] < 0) | (df["Attendance"] > 100)])
    print(df[(df["Math"] < 0) | (df["Math"] > 100)])

    # Convert Physics to numeric
    df["Physics"] = pd.to_numeric(df["Physics"], errors="coerce")

    # Replace invalid values with NaN
    df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = np.nan
    df.loc[(df["StudyHours"] < 0) | (df["StudyHours"] > 24), "StudyHours"] = np.nan
    df.loc[(df["Attendance"] < 0) | (df["Attendance"] > 100), "Attendance"] = np.nan
    df.loc[(df["Math"] < 0) | (df["Math"] > 100), "Math"] = np.nan

    # Fill missing values
    fill_missing(df, "Name", "Unknown")
    fill_missing(df, "Gender", "No Gender")
    fill_missing(df, "Department", "Chemistry")
    fill_missing(df, "Age", df["Age"].mean())
    fill_missing(df, "StudyHours", df["StudyHours"].median())
    fill_missing(df, "Attendance", df["Attendance"].mean())
    fill_missing(df, "Math", df["Math"].median())
    fill_missing(df, "Physics", df["Physics"].median())
    fill_missing(df, "Programming", df["Programming"].median())

    # Standardize Gender
    df["Gender"] = df["Gender"].replace("Male", "M")
    df["Gender"] = df["Gender"].replace("Female", "F")
    df["Gender"] = df["Gender"].replace("X", "No Gender")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Compute Average
    df["Average"] = (df["Math"] + df["Physics"] + df["Programming"]) / 3

    return df


# Function to save the cleaned file
def save_file(df, file_name):
    df.to_csv(file_name, index=False)
    print("File saved successfully.")


# Main Program
student = read_file("student_dirty.csv")

student = clean_data(student)

print(student.to_string())

save_file(student, "Student_cleaned.csv")