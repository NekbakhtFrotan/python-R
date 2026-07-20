# Take a 3 × 3 matrix from the user
matrix = []

print("Enter the 3 × 3 matrix:")

for i in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

# Row sums
print("Row Sums:")
for row in matrix:
    print(sum(row))

# Column sums
print("Column Sums:")
for j in range(3):
    column_sum = 0
    for i in range(3):
        column_sum += matrix[i][j]
    print(column_sum)

# Total sum
total = 0
for row in matrix:
    total += sum(row)

print("Total Sum:", total)