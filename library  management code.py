# ============================================
#   LIBRARY MANAGEMENT SYSTEM (Project)
#   Concepts used: loops, tuples, lists, if-else
# ============================================

# Each book is a TUPLE: (book_id, title, author, available)
# available = True  -> book is in the library
# available = False -> book is issued to someone

import datetime

books = [
    (1, "Python Basics", "Guido Rossum", True),
    (2, "C Programming", "Dennis Ritchie", True),
    (3, "Data Structures", "Mark Weiss", True),
    (4, "Discrete Maths", "Kenneth Rosen", True),
    (5, "Digital Logic", "Morris Mano", True),
    (6, "Higher Engineering","GS Grrehwal",True),
    (7, "Harry Potter","J.K Rowling",True),
    (8, "Cosmos","Carl Sagan",True),
    (9, "Thinking Fast And Slow","Daniel Kahneman",True),
    (10, "The Diary Of A Young Girl","Anne Frank",True),
    (11, "Computer Science","Author",True),
    (12, "Electronic","Author",True),
    (13, "Mechanical","Author",True),
]



def show_menu():
    print("\n===== LIBRARY MENU =====")
    print("1. View all books")
    print("2. Search a book")
    print("3. Issue a book")
    print("4. Student's Detail")
    print("5. Return a book")
    print("6. Add a new book")
    print("7. delete_book")
    print("8. update_book")
    print("9. sort_books")
    print("10. library_statitics")
    print("11. search_by_author")
    print("12. Register a student")
    print("13. View all students")
    print("14. Issue book with due date")
    print("15. Return book with fine")
    print("16. View issue log")
    print("17. Save library data")
    print("18. Load library data")
    print("19. Add book category")
    print("20. View books by category")
    print("21. Most issued books report")
    print("22. Export full report")
    print("23. Exit")




def view_books():
    print("\nID  | Title                | Author           | Status")
    print("-" * 60)
    for book in books:
        book_id, title, author, available = book   # tuple unpacking
        if available:
            status = "Available"
        else:
            status = "Issued"
        print(book_id, " |", title.ljust(20), "|", author.ljust(16), "|", status)
    input("Press Enter to return to the main menu...")


def search_book():
    keyword = input("Enter book title to search: ").lower()
    found = False
    for book in books:
        if keyword in book[1].lower():         # book[1] is the title
            print("Found ->", book)
            found = True
    if not found:
        print("No book found with that name.")
    input("Press Enter to return to the main menu...")


def issue_book():
    view_books()
    book_id = int(input("\nEnter book ID to issue: "))
    found = False
    for i in range(len(books)):
        book = books[i]
        if book[0] == book_id:
            found = True
            if book[3]:
                # Tuples cannot be changed, so we replace the whole tuple
                books[i] = (book[0], book[1], book[2], False)
                print("Book issued:", book[1])
            else:
                print("Sorry, this book is already issued.")
            break
    if not found:
        print("Invalid book ID.")
    input("Press Enter to return to the main menu...")


def student_detail(): 
    student_name = input("Enter Student name: ")
    print(student_name)
    student_id = int(input("Enter registration number: "))
    print(student_id)
    email = input("Enter email id: ")
    print(email)
    phone_number = int(input("Enter the phone no. : "))
    print(phone_number)
    number_of_issued_book = int(input("Enter number of book issued: "))
    print(number_of_issued_book)
    print("Student Registerd Successfully!")
    input("Press Enter to return to the main menu...") 


def return_book():
    book_id = int(input("Enter book ID to return: "))
    found = False
    for i in range(len(books)):
        book = books[i]
        if book[0] == book_id:
            found = True
            if not book[3]:
                books[i] = (book[0], book[1], book[2], True)
                print("Book returned:", book[1])
            else:
                print("This book was not issued.")
            break
    if not found:
        print("Invalid book ID.")
    input("Press Enter to return to the main menu...")



def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    new_id = len(books) + 1
    new_book = (new_id, title, author, True)   # creating a new tuple
    books.append(new_book)
    print("Book added successfully with ID", new_id)
    input("Press Enter to return to the main menu...")

 
def delete_book():
    book_id = int(input("Enter book ID to delete: "))
    for book in books:
        if book[0] == book_id:
            books.remove(book)
            print("Book deleted successfully!")
            return
    print("Book ID not found.")
    input("Press Enter to return to the main menu...")

 
def update_book():
    book_id = int(input("Enter book ID to update: "))
    for i in range(len(books)):
        book_id_existing, title, author, available = books[i]   # tuple unpacking
        if book_id_existing == book_id:
            print("Leave blank to keep the current value.")
            new_title = input("Enter new title: ") or title
            new_author = input("Enter new author name: ") or author
            books[i] = (book_id_existing, new_title, new_author, available)
            print("Book updated successfully!")
            return
    print("Book ID not found.")
    input("Press Enter to return to the main menu...")


def sort_books():
    print("\nSort by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter choice: ")

    if choice == "1":
        sorted_books = sorted(books, key=lambda book: book[1].lower())
    elif choice == "2":
        sorted_books = sorted(books, key=lambda book: book[2].lower())
    else:
        print("Invalid choice.")
        return

    print("\nID  | Title                | Author           | Status")
    print("-" * 60)
    for book in sorted_books:
        book_id, title, author, available = book   # tuple unpacking
        status = "Available" if available else "Issued"
        print(book_id, "|", title.ljust(20), "|", author.ljust(16), "|", status)
    input("Press Enter to return to the main menu...")


def library_statistics():
    total_books = len(books)
    issued_count = 0
    for book in books:
        book_id, title, author, available = book   # tuple unpacking
        if not available:
            issued_count += 1
    available_count = total_books - issued_count

    print("\n===== LIBRARY STATISTICS =====")
    print("Total books   :", total_books)
    print("Available     :", available_count)
    print("Issued        :", issued_count)
    print("-"*30)
    input("Press Enter to return to the main menu...")


def search_by_author():
    keyword = input("Enter author name to search: ").lower()
    found = False
    for book in books:
        if keyword in book[2].lower():   # book[2] is the author
            print("Found ->", book)
            found = True
    if not found:
        print("No books found by that author.")
    input("Press Enter to return to the main menu...")


students = [
    # (student_id, name, department)
    (101, "Rahul Sharma", "Computer Science"),
    (102, "Priya Verma", "Electronics"),
    (103, "Aman Singh", "Mechanical"),
]

issue_log = []   # each record: [student_id, book_id, issue_date, due_date, return_date]

categories = {
    # book_id : genre        -> edit these ids to match your real book list
    1: "Fiction",
    2: "Fantasy",
    3: "Science",
    4: "Self-Help",
    5: "History",
}

FINE_PER_DAY = 2      # fine in Rs. charged per day after the due date
ALLOWED_DAYS = 14     # borrowing period before a book becomes overdue


# =====  STUDENT MANAGEMENT =====

def register_student():
    student_id = int(input("Enter new student ID: "))
    name = input("Enter student name: ")
    department = input("Enter department: ")

    students.append((student_id, name, department))
    print("Student registered successfully!")
    input("Press Enter to return to the main menu...")

def view_students():
    print("\nID   | Name                 | Department")
    print("-" * 50)
    for student in students:
        student_id, name, department = student   # tuple unpacking
        print(student_id, "|", name.ljust(20), "|", department)
    input("Press Enter to return to the main menu...")

def find_student(student_id):
    for student in students:
        if student[0] == student_id:
            return student
    return None
input("Press Enter to return to the main menu...")


# =====  ISSUE / RETURN WITH DUE DATE + FINE =====

def issue_with_due_date():
    student_id = int(input("Enter student ID: "))
    student = find_student(student_id)
    if student is None:
        print("Student not found. Please register first.")
        return

    book_id = int(input("Enter book ID to issue: "))
    book_found = False
    for i in range(len(books)):
        b_id, title, author, available = books[i]   # tuple unpacking
        if b_id == book_id:
            book_found = True
            if not available:
                print("This book is already issued.")
                return
            books[i] = (b_id, title, author, False)
            issue_date = datetime.date.today()
            due_date = issue_date + datetime.timedelta(days=ALLOWED_DAYS)
            issue_log.append([student_id, book_id, issue_date, due_date, None])
            print("Book issued to", student[1], "| Due date:", due_date)
            return

    if not book_found:
        print("Book ID not found.")
    input("Press Enter to return to the main menu...")

def return_with_fine():
    book_id = int(input("Enter book ID to return: "))

    for record in issue_log:
        rec_student_id, rec_book_id, issue_date, due_date, return_date = record
        if rec_book_id == book_id and return_date is None:
            today = datetime.date.today()
            record[4] = today   # mark returned

            for i in range(len(books)):
                b_id, title, author, available = books[i]   # tuple unpacking
                if b_id == book_id:
                    books[i] = (b_id, title, author, True)
                    break

            days_late = (today - due_date).days
            if days_late > 0:
                fine = days_late * FINE_PER_DAY
                print("Book returned late by", days_late, "day(s). Fine = Rs.", fine)
            else:
                print("Book returned on time. No fine.")
            return

    print("No active issue record found for this book ID.")
    input("Press Enter to return to the main menu...")

def view_issue_log():
    print("\nStudent ID | Book ID | Issue Date | Due Date   | Return Date")
    print("-" * 65)
    for record in issue_log:
        student_id, book_id, issue_date, due_date, return_date = record
        return_display = return_date if return_date else "Not Returned"
        print(student_id, "        |", book_id, "     |", issue_date, "|", due_date, "|", return_display)
    input("Press Enter to return to the main menu...")

# =====  SAVE / LOAD LIBRARY DATA (FILE PERSISTENCE) =====

def save_data():
    file = open("library_data.txt", "w")
    for book in books:
        book_id, title, author, available = book   # tuple unpacking
        line = str(book_id) + "," + title + "," + author + "," + str(available)
        file.write(line + "\n")
    file.close()
    print("Library data saved to library_data.txt")
input("Press Enter to return to the main menu...")


def load_data():
    try:
        file = open("library_data.txt", "r")
    except FileNotFoundError:
        print("No saved data file found yet.")
        return

    books.clear()
    for line in file:
        parts = line.strip().split(",")
        book_id = int(parts[0])
        title = parts[1]
        author = parts[2]
        available = parts[3] == "True"
        books.append((book_id, title, author, available))
    file.close()
    print("Library data loaded from library_data.txt")
input("Press Enter to return to the main menu...")


# =====  CATEGORY / GENRE SUPPORT =====

def add_category():
    book_id = int(input("Enter book ID: "))
    genre = input("Enter genre for this book: ")
    categories[book_id] = genre
    print("Category saved successfully!")
input("Press Enter to return to the main menu...")


def view_by_category():
    genre = input("Enter genre to filter by: ").lower()
    print("\nBooks in genre:", genre)
    print("-" * 40)
    found = False
    for book in books:
        book_id, title, author, available = book   # tuple unpacking
        book_genre = categories.get(book_id, "Unknown")
        if book_genre.lower() == genre:
            print(book_id, "|", title, "|", author)
            found = True
    if not found:
        print("No books found in this genre.")
input("Press Enter to return to the main menu...")


# =====  MOST ISSUED (POPULAR) BOOKS REPORT =====

def most_issued_books():
    counts = {}
    for record in issue_log:
        book_id = record[1]
        if book_id in counts:
            counts[book_id] += 1
        else:
            counts[book_id] = 1

    if not counts:
        print("No books have been issued yet.")
        return

    print("\n===== MOST ISSUED BOOKS =====")
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    for book_id, count in sorted_counts:
        title = "Unknown"
        for book in books:
            if book[0] == book_id:
                title = book[1]
                break
        print(title, "-> issued", count, "time(s)")
    input("Press Enter to return to the main menu...")

# =====  SIMPLE ADMIN LOGIN =====

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "library123"


def admin_login():
    print("\n===== ADMIN LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login successful! Welcome,", username)
        return True
    else:
        print("Invalid username or password.")
        return False
input("Press Enter to return to the main menu...")


# ==== EXPORT FULL REPORT TO A TEXT FILE =====

def export_report():
    file = open("library_report.txt", "w")
    file.write("===== LIBRARY REPORT =====\n\n")

    file.write("--- BOOKS ---\n")
    for book in books:
        book_id, title, author, available = book   # tuple unpacking
        status = "Available" if available else "Issued"
        file.write(str(book_id) + " | " + title + " | " + author + " | " + status + "\n")

    file.write("\n--- STUDENTS ---\n")
    for student in students:
        student_id, name, department = student
        file.write(str(student_id) + " | " + name + " | " + department + "\n")

    file.write("\n--- ISSUE LOG ---\n")
    for record in issue_log:
        file.write(str(record) + "\n")

    file.close()
    print("Report exported to library_report.txt")
    input("Press Enter to return to the main menu...")


# ---------------- MAIN PROGRAM ----------------



print("Welcome to the Library Management System!")

while True:
    show_menu()
    choice = input("Enter your choice (1-23): ")
    if choice == "1":
     view_books()
    elif choice == "2":
     search_book()
    elif choice == "3":
     issue_book()
    elif choice == "4":
     student_detail()
    elif choice == "5":
     return_book()
    elif choice == "6":
     add_book()
    elif choice == "7":
     delete_book()
    elif choice == "8":
     update_book()
    elif choice == "9":
     sort_books()
    elif choice == "10":
     library_statistics()
    elif choice == "11":
     search_by_author()
    elif choice == "12":
     register_student()
    elif choice == "13":
     view_students()
    elif choice == "14":
     issue_with_due_date()
    elif choice == "15":
     return_with_fine()
    elif choice == "16":
     view_issue_log()
    elif choice == "17":
     save_data()
    elif choice == "18":
     load_data()
    elif choice == "19":
     add_category()
    elif choice == "20":
     view_by_category()
    elif choice == "21":
     most_issued_books()
    elif choice == "22":
     export_report()
    elif choice == "23":
     print("Goodbye!")
     break
    else:
     print("Invalid choice, try again.")
 

    
