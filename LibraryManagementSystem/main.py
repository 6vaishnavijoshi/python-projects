# Library Management System

books = []

while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Total Books")
    print("9. Exit")

    choice = input("\nEnter your choice (1-9): ")

    # ---------------- ADD BOOK ----------------
    if choice == "1":

        book_id = input("Enter Book ID: ")

        found = False

        for book in books:
            if book["id"] == book_id:
                found = True
                break

        if found:
            print("Book ID already exists!")

        else:

            name = input("Enter Book Name: ")
            author = input("Enter Author Name: ")
            category = input("Enter Category: ")
            price = input("Enter Price: ")

            book = {
                "id": book_id,
                "name": name,
                "author": author,
                "category": category,
                "price": price,
                "status": "Available"
            }

            books.append(book)

            print("Book Added Successfully!")

    # ---------------- VIEW BOOKS ----------------
    elif choice == "2":

        if len(books) == 0:
            print("No Books Available.")

        else:

            print("\n========== BOOK LIST ==========")

            for book in books:

                print("---------------------------------")
                print("Book ID   :", book["id"])
                print("Book Name :", book["name"])
                print("Author    :", book["author"])
                print("Category  :", book["category"])
                print("Price     :", book["price"])
                print("Status    :", book["status"])

    # ---------------- SEARCH BOOK ----------------
    elif choice == "3":

        search_id = input("Enter Book ID: ")

        found = False

        for book in books:

            if book["id"] == search_id:

                print("\nBook Found")
                print("---------------------------")
                print("Book ID   :", book["id"])
                print("Book Name :", book["name"])
                print("Author    :", book["author"])
                print("Category  :", book["category"])
                print("Price     :", book["price"])
                print("Status    :", book["status"])

                found = True
                break

        if not found:
            print("Book Not Found!")

    # ---------------- UPDATE BOOK ----------------
    elif choice == "4":

        update_id = input("Enter Book ID to Update: ")

        found = False

        for book in books:

            if book["id"] == update_id:

                book["name"] = input("Enter New Book Name: ")
                book["author"] = input("Enter New Author: ")
                book["category"] = input("Enter New Category: ")
                book["price"] = input("Enter New Price: ")

                print("Book Updated Successfully!")

                found = True
                break

        if not found:
            print("Book Not Found!")

    # ---------------- DELETE BOOK ----------------
    elif choice == "5":

        delete_id = input("Enter Book ID to Delete: ")

        found = False

        for book in books:

            if book["id"] == delete_id:

                books.remove(book)

                print("Book Deleted Successfully!")

                found = True
                break

        if not found:
            print("Book Not Found!")

    # ---------------- ISSUE BOOK ----------------
    elif choice == "6":

        issue_id = input("Enter Book ID to Issue: ")

        found = False

        for book in books:

            if book["id"] == issue_id:

                found = True

                if book["status"] == "Available":

                    book["status"] = "Issued"

                    print("Book Issued Successfully!")

                else:

                    print("Book is Already Issued!")

                break

        if not found:
            print("Book Not Found!")

    # ---------------- RETURN BOOK ----------------
    elif choice == "7":

        return_id = input("Enter Book ID to Return: ")

        found = False

        for book in books:

            if book["id"] == return_id:

                found = True

                if book["status"] == "Issued":

                    book["status"] = "Available"

                    print("Book Returned Successfully!")

                else:

                    print("Book is Already Available!")

                break

        if not found:
            print("Book Not Found!")

    # ---------------- TOTAL BOOKS ----------------
    elif choice == "8":

        print("Total Books :", len(books))

    # ---------------- EXIT ----------------
    elif choice == "9":

        print("Thank You for Using Library Management System.")
        break

    # ---------------- INVALID CHOICE ----------------
    else:

        print("Invalid Choice! Please Enter Between 1 and 9.")