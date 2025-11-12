# ---------------- Student Record Management using Linked List ---------------- #

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    # 1. Add a new student
    def add_student(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        new_node.next = self.head
        self.head = new_node
        print("   Record Added Successfully")

    # 2. Display all students
    def display(self):
        if self.head is None:
            print("⚠ No Records Found")
            return
        temp = self.head
        print("\n--- Student Records ---")
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next

    # 3. Search student by Roll or Name
    def search(self, keyword):
        temp = self.head
        while temp:
            if str(temp.roll) == str(keyword) or temp.name.lower() == keyword.lower():
                print(f"   Found: Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
                return
            temp = temp.next
        print("  Record Not Found")

    # 4. Update student record
    def update(self, roll, new_name, new_marks):
        temp = self.head
        while temp:
            if temp.roll == roll:
                temp.name = new_name
                temp.marks = new_marks
                print("   Record Updated Successfully")
                return
            temp = temp.next
        print("  Record Not Found")

    # 5. Delete student record
    def delete(self, roll):
        temp = self.head
        prev = None
        while temp:
            if temp.roll == roll:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print("   Record Deleted Successfully")
                return
            prev = temp
            temp = temp.next
        print("  Record Not Found")

    # 6. Sort Records (1=Roll, 2=Marks)
    def sort(self, key):
        if self.head is None:
            print("⚠ No Records to Sort")
            return
        swapped = True
        while swapped:
            swapped = False
            temp = self.head
            while temp.next:
                if (key == 1 and temp.roll > temp.next.roll) or (key == 2 and temp.marks > temp.next.marks):
                    # Swap data fields
                    temp.roll, temp.next.roll = temp.next.roll, temp.roll
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.marks, temp.next.marks = temp.next.marks, temp.marks
                    swapped = True
                temp = temp.next
        print("   Records Sorted Successfully")


# ---------------- Main Program ---------------- #
obj = StudentList()

while True:
    print("\n1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Sort by Roll")
    print("7. Sort by Marks")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        r = int(input("Enter Roll: "))
        n = input("Enter Name: ")
        m = float(input("Enter Marks: "))
        obj.add_student(r, n, m)

    elif choice == 2:
        obj.display()

    elif choice == 3:
        key = input("Enter Roll/Name to Search: ")
        obj.search(key)

    elif choice == 4:
        r = int(input("Enter Roll to Update: "))
        n = input("Enter New Name: ")
        m = float(input("Enter New Marks: "))
        obj.update(r, n, m)

    elif choice == 5:
        r = int(input("Enter Roll to Delete: "))
        obj.delete(r)

    elif choice == 6:
        obj.sort(1)

    elif choice == 7:
        obj.sort(2)

    elif choice == 8:
        print("Exited Program.")
        break

    else:
        print("Invalid Choice! Try Again.")
