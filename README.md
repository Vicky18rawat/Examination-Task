How to setup and run this project?
-----------------------------------
Simply run the python file in terminal or in command prompt using command "python task.py"

Brief overview of code structure
-------------------------------------
**Imports:**
The code imports the pandas library for data manipulation and display.

**ItemsRecyclingSystem Class:**
**Class Variable (REWARDS)**: A dictionary that maps each recyclable item type to its corresponding reward value.
**__init__ Method**: Initializes the instance variables items an empty list to store items and a variable for total_reward.
**add_item Method**: Adds an item to the list of items and updates the total reward.
**view_total_items Method**: Prints the total number of items added and displays a table with item counts using a Pandas DataFrame. If no items have been added, it informs the user.
**view_total_reward Method**: Prints the total reward accumulated by the user in INR.
**reset_system Method**: Resets the items list and total_reward to their initial states, effectively starting a new user session.

**Main Function:**
The main function acts as the user interface, presenting a menu to the user and performing actions based on the user's input.
Menu Options:
Add an item.
View all items added.
View total reward.
Reset the system.
Exit the program.
User Interaction: Depending on the user's choice, the corresponding method of the ItemsRecyclingSystem instance is called. Invalid choices prompt the user to enter a valid option.

**Program Execution:**
The main function is called when the script is run directly, displaying a welcome message and starting the user interaction loop.


**Any assumptions or design decisions you made**
----------------------------------------------
I have assumed the items as GLASS BOTTLE, PLASTIC BOTTLE and TIN CONTAINER instead of A, B and C.
