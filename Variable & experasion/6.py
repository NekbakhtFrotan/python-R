numbers = []
n = input("Enter the number of elements in the list: " )
for i in range(int(n)):
    element = input("Enter element " + str(i + 1) + ": ")
    numbers.append(int(element))

num = input("Enter the number to check: ")
if int(num) in numbers:
    index = numbers.index(int(num))
    print("The number is in the list.", index)
