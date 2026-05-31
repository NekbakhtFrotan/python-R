numbers = [1,2,3,1,1,2,3,]
count = 0
for i in numbers:
    if numbers.count(i) > 1:
        count += 1
        print(count)