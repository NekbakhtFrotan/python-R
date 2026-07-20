# Store marks of 10 students
marks = list(map(int, input("Enter marks of 10 students: ").split()))

# Highest mark
highest = max(marks)

# Lowest mark
lowest = min(marks)

# Average mark
average = sum(marks) / len(marks)

# Count students scoring above average
count = 0
for mark in marks:
    if mark > average:
        count += 1

# Display the results
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Average Mark:", average)
print("Students Above Average:", count)