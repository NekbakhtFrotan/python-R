# Numbers from 1 to 20
numbers = [i for i in range(1, 21)]
print("Numbers:", numbers)

# Even numbers from 1 to 20
even = [i for i in range(1, 21) if i % 2 == 0]
print("Even Numbers:", even)

# Odd numbers from 1 to 20
odd = [i for i in range(1, 21) if i % 2 != 0]
print("Odd Numbers:", odd)

# Squares of numbers from 1 to 10
squares = [i**2 for i in range(1, 11)]
print("Squares:", squares)