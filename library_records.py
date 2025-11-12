# ---------------- Library Borrowing Records Management ---------------- #

# Sample data: Member -> Number of books borrowed
borrow_records = {
    "Student A": 3,
    "Student B": 0,
    "Student C": 5,
    "Student D": 2,
    "Student E": 0
}

# Sample data: Book -> Number of times borrowed
book_records = {
    "Book1": 10,
    "Book2": 5,
    "Book3": 7,
    "Book4": 3,
    "Book5": 12
}


# 1. Compute the average number of books borrowed by all library members
def average_borrowings(records):
    total = sum(records.values())
    count = len(records)
    return total / count if count != 0 else 0


# 2. Find the book with highest and lowest borrowings
def highest_lowest_books(records):
    highest = max(records, key=records.get)
    lowest = min(records, key=records.get)
    return highest, records[highest], lowest, records[lowest]


# 3. Count members who have not borrowed any books
def count_zero_borrowers(records):
    return sum(1 for borrow in records.values() if borrow == 0)


# 4. Find the most frequently borrowed book (mode)
def most_frequent_book(records):
    max_borrow = max(records.values())
    most_borrowed = [book for book, count in records.items() if count == max_borrow]
    return most_borrowed, max_borrow


# ---------------- Menu-driven Execution ---------------- #
def menu():
    while True:
        print("\n===== Library Borrowing Records Menu =====")
        print("1. Compute average borrowings per member")
        print("2. Find highest and lowest borrowed book")
        print("3. Count members with zero borrowings")
        print("4. Find most frequently borrowed book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print(f"\nAverage borrowings per member: {average_borrowings(borrow_records):.2f}")

        elif choice == "2":
            high_book, high_count, low_book, low_count = highest_lowest_books(book_records)
            print(f"\nHighest borrowed book: {high_book} ({high_count} times)")
            print(f"Lowest borrowed book: {low_book} ({low_count} times)")

        elif choice == "3":
            print(f"\nMembers with zero borrowings: {count_zero_borrowers(borrow_records)}")

        elif choice == "4":
            most_books, borrow_count = most_frequent_book(book_records)
            print(f"\nMost frequently borrowed book(s): {', '.join(most_books)} ({borrow_count} times)")

        elif choice == "5":
            print("\nExiting... Thank you for using Library Records System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# ---------------- Run Program ---------------- #
print("Library Borrowing Records Analysis System\n")
menu()
