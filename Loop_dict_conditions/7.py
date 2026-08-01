students = {"Name": "Ahmad", "Identification": "Senior", "Program" : "General", "year": 2024}
print(students)
students["year"] = 2030
students["Email"] = "ahmad@gmail.com"
for key, value in students.items():
    print(key,":" ,value)
if "phone" in students:
    print("Phone exsit")
else:
    print("No phone")
