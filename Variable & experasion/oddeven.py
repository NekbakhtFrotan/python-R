numbers = []
n = input("Enter the number of elements in the list: ")
for i in range (int(n)):
    element = input("Enter the element " + str(i + 1) + ": ")
    numbers.append(int(element))
odd = []
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("The odd numbers are:", odd)
print("The even numbers are:", even)