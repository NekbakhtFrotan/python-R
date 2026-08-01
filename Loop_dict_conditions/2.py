n = int(input("Enter a number: "))
sum = 0
count = 0
for i in range(1, n+1):
    if i % 2 == 0:
        print(f"Even Numbers: {i}")
        sum = sum + i
        count = count+1
print(f"Sum: {sum}")
print(f"Average: {sum/count}")
