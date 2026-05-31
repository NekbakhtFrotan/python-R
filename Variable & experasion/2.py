numbers = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = input("Enter element " + str(i + 1) + ": ")
    numbers.append(element)

print(numbers)
print(len(numbers))

