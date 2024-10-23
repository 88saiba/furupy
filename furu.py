import os
import platform
from utils.input_manager import InputManager
from utils.lottery import Lottery
from utils.file_manager import FileManager

def clear_terminal():
    # Clear the terminal based on the OS
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def main():
    input_manager = InputManager()
    lottery = Lottery()
    file_manager = FileManager()

    while True:
        clear_terminal()  # Clear the terminal every time we return to the main menu
        print("\n=== Fortune Tool ===")
        print("1. Enter Data")
        print("2. Start Drawing")
        print("3. View List of Choices")
        print("4. Reset Data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            input_manager.collect_data()
        elif choice == '2':
            selected_choice = lottery.draw_choice(input_manager.choices)
            print(f"Selected choice: {selected_choice[0]} with ID {selected_choice[1]}")
            save_choice = input("Do you want to save the result? (y/n): ")
            if save_choice.lower() == 'y':
                file_manager.save_data(input_manager.choices, selected_choice)
        elif choice == '3':
            input_manager.view_list()
        elif choice == '4':
            input_manager.reset_data()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
