# ---------------- Text Editor with Undo and Redo Functionality ---------------- #

class TextEditor:
    def __init__(self):
        self.document = ""          # current document text
        self.undo_stack = []        # stores past changes
        self.redo_stack = []        # stores undone changes

    # 1. Make a New Change
    def make_change(self, new_text):
        self.undo_stack.append(self.document)  # save current state
        self.document = new_text               # apply new change
        self.redo_stack.clear()                # clear redo history
        print("Change applied!")

    # 2. Undo Last Change
    def undo_action(self):
        if not self.undo_stack:
            print("No action to undo!")
            return
        self.redo_stack.append(self.document)   # save current state
        self.document = self.undo_stack.pop()   # revert to previous
        print("Undo successful!")

    # 3. Redo Last Undone Change
    def redo_action(self):
        if not self.redo_stack:
            print("No action to redo!")
            return
        self.undo_stack.append(self.document)   # save current state
        self.document = self.redo_stack.pop()   # reapply undone change
        print("Redo successful!")

    # 4. Display Document
    def display_document(self):
        print("\nCurrent Document State:")
        print(self.document if self.document else "[Empty Document]")


# -------- Main Program --------
if __name__ == "__main__":
    editor = TextEditor()

    while True:
        print("\n--- Text Editor Menu ---")
        print("1. Make a Change")
        print("2. Undo Action")
        print("3. Redo Action")
        print("4. Display Document State")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            new_text = input("Enter new document content: ")
            editor.make_change(new_text)
        elif choice == "2":
            editor.undo_action()
        elif choice == "3":
            editor.redo_action()
        elif choice == "4":
            editor.display_document()
        elif choice == "5":
            print("Exiting Editor. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
