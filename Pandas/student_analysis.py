# exploring datset and identifying issues

import pandas as pd

# Read the dataset
students = pd.read_csv("student_dirty_dataset.csv")

# Show basic information
print("Shape:", students.shape)
print("\nColumns:")
print(students.columns)

print("\nDataset Information:")
students.info()

print("\nMissing Values:")
print(students.isnull().sum())

# Rows with missing values
print("\nRows with Missing Values:")
missing_rows = students[students.isnull().any(axis=1)]
print(missing_rows)

# Duplicate Student IDs
print("\nDuplicate Student IDs:")
duplicate_students = students[
    students.duplicated(subset="StudentID", keep=False)
]
print(duplicate_students)

# Invalid Age
print("\nInvalid Age:")
invalid_age = students[
    (students["Age"] < 16) |
    (students["Age"] > 100)
]
print(invalid_age[["StudentID", "Name", "Age"]])

# Invalid Study Hours
print("\nInvalid Study Hours:")
invalid_hours = students[
    (students["StudyHours"] < 0) |
    (students["StudyHours"] > 24)
]
print(invalid_hours)

# Invalid Attendance
print("\nInvalid Attendance:")
invalid_attendance = students[
    (students["Attendance"] < 0) |
    (students["Attendance"] > 100)
]
print(invalid_attendance)

# Invalid Math Marks
print("\nInvalid Math Marks:")
invalid_math = students[
    (students["Math"] < 0) |
    (students["Math"] > 100)
]
print(invalid_math)

# Invalid Physics Marks
print("\nInvalid Physics Marks:")
physics = pd.to_numeric(students["Physics"], errors="coerce")
invalid_physics = students[
    (physics < 0) |
    (physics > 100)
]
print(invalid_physics)

# Invalid Programming Marks
print("\nInvalid Programming Marks:")
invalid_programming = students[
    (students["Programming"] < 0) |
    (students["Programming"] > 100)
]
print(invalid_programming)

# Unique Gender Values
print("\nUnique Gender Values:")
print(students["Gender"].unique())