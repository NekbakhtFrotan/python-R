students = {}


def calculate_average(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)


def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


while True:
    print("\nStudent Record Menu")
    print("1. Add a student")
    print("2. Update one of a student's marks")
    print("3. Search by student ID")
    print("4. Display every student's average and letter grade")
    print("5. Display the student or students with the highest average")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ").strip()
        if student_id in students:
            print("Student ID already exists.")
            continue

        name = input("Enter student name: ").strip()
        marks = []
        for i in range(3):
            while True:
                try:
                    mark = float(input(f"Enter mark {i + 1}: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100.")

        students[student_id] = {"name": name, "marks": marks}
        print("Student added.")

    elif choice == "2":
        student_id = input("Enter student ID: ").strip()
        if student_id not in students:
            print("Student ID not found.")
            continue

        while True:
            try:
                position = int(input("Enter mark position (1, 2, or 3): "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if position not in (1, 2, 3):
                print("Position must be 1, 2, or 3.")
                continue

            while True:
                try:
                    new_mark = float(input("Enter new mark: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if 0 <= new_mark <= 100:
                    students[student_id]["marks"][position - 1] = new_mark
                    print("Mark updated.")
                    break
                else:
                    print("Mark must be between 0 and 100.")
            break

    elif choice == "3":
        student_id = input("Enter student ID to search: ").strip()
        if student_id in students:
            student = students[student_id]
            average = calculate_average(student["marks"])
            print(f"Name: {student['name']}")
            print(f"Marks: {student['marks']}")
            print(f"Average: {average}")
            print(f"Grade: {get_grade(average)}")
        else:
            print("Student ID not found.")

    elif choice == "4":
        for student_id, student in students.items():
            average = calculate_average(student["marks"])
            print(f"{student_id}: {student['name']} - Average: {average}, Grade: {get_grade(average)}")

    elif choice == "5":
        if not students:
            print("No students available.")
            continue

        highest_average = None
        top_students = []

        for student_id, student in students.items():
            average = calculate_average(student["marks"])
            if highest_average is None or average > highest_average:
                highest_average = average
                top_students = [student_id]
            elif average == highest_average:
                top_students.append(student_id)

        print("Students with the highest average:")
        for student_id in top_students:
            student = students[student_id]
            print(f"{student_id}: {student['name']} - Average: {calculate_average(student['marks'])}, Grade: {get_grade(calculate_average(student['marks']))}")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
