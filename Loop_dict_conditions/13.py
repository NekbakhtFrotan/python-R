while True:
    value = input("Enter a positive integer: ")
    if value.isdigit() and int(value) > 0:
        n = int(value)
        break
    print("Invalid input. Try again.")

while n > 0:
    print(n, end=" ")
    n -= 1
print("\nLaunch!")
