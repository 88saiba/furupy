class InputManager:
    def __init__(self):
        self.choices = []

    def collect_data(self):
        """Collects data from the user until they type 'done'."""
        print("Type 'done' to finish.")
        while True:
            name = input("Enter item: ")
            if name.lower() == 'done':
                break
            id_ = input("Enter choice ID: ")
            self.choices.append((name, id_))

    def display_choices(self):
        """Displays all choices that have been entered."""
        print("\n" + "=" * 30)  # Separator line
        if not self.choices:
            print("No choices available.")
        else:
            print("List of Choices:")
            for i, (name, id_) in enumerate(self.choices):
                print(f"{i + 1}. {name} with ID {id_}")
        print("=" * 30)  # Separator line

    def view_list(self):
        """Displays the list of choices and provides options to edit or delete."""
        self.display_choices()  # Display choices when requested to view the list
        while True:
            command = input("Type 'ed' to edit, 'del' to delete, or '0' to go back: ").lower()
            if command == '0':
                break
            elif command == 'ed':
                self.edit_choice_mode()
                break
            elif command == 'del':
                self.delete_choice_mode()
                break
            else:
                print("Invalid command. Please try again.")

    def edit_choice_mode(self):
        """Enters edit mode to modify existing choices."""
        self.display_choices()  # Display choices before editing
        while True:
            index = input("Choose the number of the data to edit (0 to cancel): ")
            if index == '0':
                print("Edit process canceled.")
                break
            try:
                index = int(index) - 1
                if 0 <= index < len(self.choices):
                    self.edit_choice(index)
                    break
                else:
                    print("Invalid number. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")

    def edit_choice(self, index):
        """Edits an existing choice based on the given index."""
        current_choice = self.choices[index]
        print(f"Editing choice: {current_choice[0]} with ID {current_choice[1]}")
        
        new_name = input("Enter new item (0 to cancel): ")
        if new_name == '0':
            print("Edit process canceled.")
            return  # Return without making changes

        new_id = input("Enter new ID (0 to cancel): ")
        if new_id == '0':
            print("Edit process canceled.")
            return  # Return without making changes

        self.choices[index] = (new_name, new_id)
        print("Choice has been updated.")

    def delete_choice_mode(self):
        """Enters delete mode to remove existing choices."""
        self.display_choices()  # Display choices before deleting
        while True:
            index = input("Choose the number of the data to delete (0 to cancel): ")
            if index == '0':
                print("Deletion canceled.")
                break
            try:
                index = int(index) - 1
                if 0 <= index < len(self.choices):
                    deleted_choice = self.choices.pop(index)
                    print(f"Choice '{deleted_choice[0]}' with ID '{deleted_choice[1]}' has been deleted.")
                    break  # Stop after successful deletion
                else:
                    print("Invalid number. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")

    def reset_data(self):
        """Clears all choices that have been entered."""
        self.choices.clear()
        print("Data has been reset.")
