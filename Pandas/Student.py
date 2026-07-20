import pandas as pd
import numpy as np

# Read the student dataset
students = pd.read_csv("student_dirty_dataset.csv")

print("First 5 Rows")
print(students.head())

# Create a copy of the dataset
students_clean = students.copy()

# Remove duplicate student IDs
students_clean = students_clean.drop_duplicates(
    subset="StudentID",
    keep="first"
)

print("\nShape after removing duplicates:")
print(students_clean.shape)

# Clean student names
students_clean["Name"] = students_clean["Name"].fillna("")

students_clean["Name"] = (
    students_clean["Name"]
    .astype(str)
    .str.replace(r"[^A-Za-z .'-]", "", regex=True)
    .str.strip()
    .str.title()
)

# Fill missing names
missing_name = students_clean["Name"].eq("")

students_clean.loc[missing_name, "Name"] = (
    "Unknown_" +
    students_clean.loc[missing_name, "StudentID"].astype(str)
)

# Clean gender values
students_clean["Gender"] = (
    students_clean["Gender"]
    .astype("string")
    .str.strip()
    .str.upper()
)

gender_map = {
    "M": "M",
    "MALE": "M",
    "F": "F",
    "FEMALE": "F"
}

students_clean["Gender"] = (
    students_clean["Gender"]
    .map(gender_map)
    .fillna("Unknown")
)

# Clean department names
students_clean["Department"] = (
    students_clean["Department"]
    .astype("string")
    .str.strip()
    .str.upper()
    .fillna("Unknown")
)

students_clean["Department"] = (
    students_clean["Department"]
    .replace("N/A", "Unknown")
)

# Convert columns to numbers
numeric_columns = [
    "Age",
    "StudyHours",
    "Attendance",
    "Math",
    "Physics",
    "Programming"
]

for column in numeric_columns:
    students_clean[column] = pd.to_numeric(
        students_clean[column],
        errors="coerce"
    )

# Clean age
valid_age = students_clean["Age"].between(16, 100)

age_median = students_clean.loc[
    valid_age,
    "Age"
].median()

students_clean.loc[
    ~valid_age | students_clean["Age"].isna(),
    "Age"
] = age_median

students_clean["Age"] = (
    students_clean["Age"]
    .round()
    .astype(int)
)

# Clean study hours
valid_hours = students_clean["StudyHours"].between(0, 24)

hours_median = students_clean.loc[
    valid_hours,
    "StudyHours"
].median()

students_clean.loc[
    ~valid_hours | students_clean["StudyHours"].isna(),
    "StudyHours"
] = hours_median

students_clean["StudyHours"] = (
    students_clean["StudyHours"]
    .round()
    .astype(int)
)

# Clean attendance
valid_attendance = students_clean["Attendance"].between(0, 100)

attendance_median = students_clean.loc[
    valid_attendance,
    "Attendance"
].median()

students_clean.loc[
    ~valid_attendance | students_clean["Attendance"].isna(),
    "Attendance"
] = attendance_median

students_clean["Attendance"] = (
    students_clean["Attendance"]
    .round()
    .astype(int)
)

# Clean subject marks
subjects = ["Math", "Physics", "Programming"]

for subject in subjects:

    valid_marks = students_clean[subject].between(0, 100)

    subject_median = students_clean.loc[
        valid_marks,
        subject
    ].median()

    students_clean.loc[
        ~valid_marks | students_clean[subject].isna(),
        subject
    ] = subject_median

    students_clean[subject] = (
        students_clean[subject]
        .round()
        .astype(int)
    )

# Calculate average
students_clean["Average"] = (
    students_clean[
        ["Math", "Physics", "Programming"]
    ]
    .mean(axis=1)
    .round(2)
)

# Calculate result
students_clean["Result"] = np.where(
    students_clean["Average"] >= 40,
    "Pass",
    "Fail"
)

# Calculate grade
def assign_grade(average):

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

students_clean["Grade"] = (
    students_clean["Average"]
    .apply(assign_grade)
)

# Check missing values
print("\nMissing Values")
print(students_clean.isnull().sum())

# Check duplicate IDs
print("\nDuplicate Student IDs")
print(students_clean["StudentID"].duplicated().sum())

# Check the cleaned data
print("\nValidation")
print("Age:", students_clean["Age"].between(16, 100).all())
print("Attendance:", students_clean["Attendance"].between(0, 100).all())
print("Math:", students_clean["Math"].between(0, 100).all())
print("Physics:", students_clean["Physics"].between(0, 100).all())
print("Programming:", students_clean["Programming"].between(0, 100).all())

# Save the cleaned dataset
students_clean.to_csv(
    "student_cleaned_dataset.csv",
    index=False
)

print("\nStudent dataset cleaned successfully!")