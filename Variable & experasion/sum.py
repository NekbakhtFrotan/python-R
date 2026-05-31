numbers = []

n = int(input("Enter the number of elements in the list: "))
for i in range (n):
    element = input("Enter element " + str(i + 1) + ": ")
    numbers.append(int(element))

    sum = 0
    for i in numbers:
        sum += i
        

    print("The sum of the numbers is:", sum)
    print("The average of the numbers is:", sum/n)
    