
students = []
marks = []

while True:
    print("\n===== STUDENT MARKS MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Highest Marks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter student name: ")
        mark = float(input("Enter student marks: "))

        students.append(name)
        marks.append(mark)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("--------------------------")
            for i in range(len(students)):
                print(students[i], ":", marks[i])

    elif choice == "3":
        search = input("Enter student name to search: ")

        if search in students:
            index = students.index(search)
            print("Student:", students[index])
            print("Marks:", marks[index])
        else:
            print("Student not found.")

    elif choice == "4":
        if len(marks) == 0:
            print("No marks available.")
        else:
            average = sum(marks) / len(marks)
            print("Average Marks =", average)

    elif choice == "5":
        if len(marks) == 0:
            print("No marks available.")
        else:
            highest = max(marks)
            index = marks.index(highest)
            print("Top Student:", students[index])
            print("Highest Marks:", highest)

    elif choice == "6":
        print("Thank you for using Student Marks Manager!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")