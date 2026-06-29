# Student Management System

students = []

while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Students")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    # ---------------- Add Student ----------------
    if choice == "1":

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")

        # Check duplicate ID
        found = False

        for student in students:
            if student["id"] == student_id:
                found = True
                break

        if found:
            print("Student ID already exists!")

        else:
            student = {
                "id": student_id,
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            }

            students.append(student)

            print("Student Added Successfully!")

    # ---------------- View Students ----------------
    elif choice == "2":

        if len(students) == 0:
            print("No Students Found.")

        else:

            print("\n========== STUDENT LIST ==========")

            for student in students:

                print("------------------------------")
                print("ID     :", student["id"])
                print("Name   :", student["name"])
                print("Age    :", student["age"])
                print("Course :", student["course"])
                print("Marks  :", student["marks"])

    # ---------------- Search Student ----------------
    elif choice == "3":

        search_id = input("Enter Student ID: ")

        found = False

        for student in students:

            if student["id"] == search_id:

                print("\nStudent Found")
                print("---------------------")
                print("ID     :", student["id"])
                print("Name   :", student["name"])
                print("Age    :", student["age"])
                print("Course :", student["course"])
                print("Marks  :", student["marks"])

                found = True
                break

        if not found:
            print("Student Not Found!")

    # ---------------- Update Student ----------------
    elif choice == "4":

        update_id = input("Enter Student ID to Update: ")

        found = False

        for student in students:

            if student["id"] == update_id:

                print("Enter New Details")

                student["name"] = input("New Name: ")
                student["age"] = input("New Age: ")
                student["course"] = input("New Course: ")
                student["marks"] = input("New Marks: ")

                print("Student Updated Successfully!")

                found = True
                break

        if not found:
            print("Student Not Found!")

    # ---------------- Delete Student ----------------
    elif choice == "5":

        delete_id = input("Enter Student ID to Delete: ")

        found = False

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                print("Student Deleted Successfully!")

                found = True
                break

        if not found:
            print("Student Not Found!")

    # ---------------- Total Students ----------------
    elif choice == "6":

        print("Total Students :", len(students))

    # ---------------- Exit ----------------
    elif choice == "7":

        print("Thank You for Using Student Management System.")
        break

    # ---------------- Invalid Choice ----------------
    else:

        print("Invalid Choice! Please Enter Between 1 and 7.")