# Take a list of integers from the user
numbers = list(map(int, input("Enter numbers: ").split()))

# Calculate sum
total = sum(numbers)

# Calculate average
average = total / len(numbers)

# Find largest and smallest values
largest = max(numbers)
smallest = min(numbers)

# Display the results
print("Sum:", total)
print("Average:", average)
print("Largest value:", largest)
print("Smallest value:", smallest)