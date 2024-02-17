from NoteManager import NoteManager

if __name__ == "__main__":
    manager = NoteManager()

    while True:
        print("\nChoose an option:")
        print("1. Add a new note")
        print("2. Edit a note")
        print("3. Delete a note")
        print("4. List all notes")
        print("5. Filter notes by date")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the note: ")
            body = input("Enter the body of the note: ")
            manager.add_note(title, body)
            print("Note added successfully.")

        elif choice == "2":
            note_id = int(input("Enter the ID of the note you want to edit: "))
            title = input("Enter the new title of the note: ")
            body = input("Enter the new body of the note: ")
            if manager.edit_note(note_id, title, body):
                print("Note edited successfully.")
            else:
                print("Note not found.")

        elif choice == "3":
            note_id = int(input("Enter the ID of the note you want to delete: "))
            if manager.delete_note(note_id):
                print("Note deleted successfully.")
            else:
                print("Note not found.")

        elif choice == "4":
            manager.list_notes()

        elif choice == "5":
            start_date = input("Enter the start date (YYYY-MM-DD HH:MM:SS): ")
            end_date = input("Enter the end date (YYYY-MM-DD HH:MM:SS): ")
            manager.filter_notes_by_date(start_date, end_date)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")