students = {"Ahmad": 97, "Ali": 100, "Mohammad": 93, "Mahdi": 89, "Haidar": 99}

total = 0
for score in students.values():
    total += score

avg = total / len(students)
print(avg)

# (c) Identify the student with the highest mark without using max()
highest_name = None
highest_score = -1
for name, score in students.items():
    if score > highest_score:
        highest_score = score
        highest_name = name

print(highest_name)

# (d) Display the names of all students scoring at least 60
for name, score in students.items():
    if score >= 60:
        print(name)


        