# furupy | 振るpy

###### DISCLAIMER: Sorry, this is a gabut (means not that important) project, haha! But you can try it if you're unsure about something. There are many choices available, and you just have to submit your selection to this application.

This help us decide which whatever doubts there are in their heart. It allows users to input a list of anythings randomly, and save the results to a text file.

## Features
- Input and manage a list of items along with their IDs.
- Randomly select (lottery) one of the items from the list.
- Edit or delete existing items from the list.
- Reset the entire list.
- Save the list of items to a text file.


1. Clone this repository:
   ```bash
   git clone https://github.com/88saiba/furupy.git
   cd furupy
   ```
2. Ensure you have Python 3 installed on your system.

## Usage
To run the application, execute the following command in your terminal:

```bash
python furu.py
```
For easier access, you can create an alias in your `.bashrc` file. Follow these steps:

1. Open your `.bashrc` file in a text editor:
   ```bash
   nano ~/.bashrc
   ```
   
2. Add the following line at the end of the file:
   ```bash
   alias furupy='python /path/to/your/fortune_tool/furu.py'
   ```
   Replace `/path/to/your/furupy/` with the actual path to the directory where the Fortune Tool is located.

3. Save the file and exit the editor (in nano, press `CTRL + X`, then `Y`, and `Enter`).

4. Refresh your terminal session by running:
   ```bash
   source ~/.bashrc
   ```

5. Now you can run the Fortune Tool simply by typing:
   ```bash
   furupy
   ```

### Interacting with the Tool
Choose an option from the menu:

   - **1**: Enter items and their IDs.
   - **2**: Start the lottery to randomly select a item.
   - **3**: Edit existing items.
   - **4**: Reset the data.
   - **5**: Exit the application.
   
Follow the prompts to enter, edit, or reset data as needed.

## Saving Data

- When you perform a lottery, you will be given an option to save the results to a text file 
- The results will be saved to `data/choices_{actual-date}_{actual-time}.txt`. This file will contain the list of items and the selected items after the lottery.

## License
This project is licensed under the [MIT License](LICENSE).
