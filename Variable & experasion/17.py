# Create a 3 × 3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the entire matrix
print("Matrix:")
for row in matrix:
    print(row)

# Print the first row
print("First Row:", matrix[0])

# Print the last column
print("Last Column:", [row[2] for row in matrix])

# Calculate the sum of all elements
total = 0
for row in matrix:
    total += sum(row)

print("Sum of all elements:", total)