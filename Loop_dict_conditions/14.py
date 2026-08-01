n = int(input("Enter a positive integer: "))

temp = n
count = 0
sum_digits = 0
reversed_num = 0

while temp > 0:
    digit = temp % 10
    count += 1
    sum_digits += digit
    reversed_num = reversed_num * 10 + digit
    temp //= 10

print(f"Number of digits: {count}")
print(f"Sum of digits: {sum_digits}")
print(f"Reversed number: {reversed_num}")
