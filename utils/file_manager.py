import os
from datetime import datetime

class FileManager:
    def save_data(self, choices, selected_choice):
        # Create a filename with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/choices_{timestamp}.txt"

        with open(filename, 'w') as file:
            file.write("List of Choices:\n")
            for name, id_ in choices:
                file.write(f"{name} with ID {id_}\n")
            file.write(f"\nSelected choice: {selected_choice[0]} with ID {selected_choice[1]}\n")

        print(f"Data has been saved to {filename}")
