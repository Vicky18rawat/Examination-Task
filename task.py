import pandas as pd



class ItemsRecyclingSystem:
    REWARDS = {'GLASS BOTTLE': 0.10, 'PLASTIC BOTTLE': 0.05, 'TIN CONTAINER': 0.15}

    def __init__(self):
        """
        This method is called when a new object of the class is created. It initializes the instance variables 'items' and 'total_reward' to empty list and 0.0 respectively.
        """
        self.items = []
        self.total_reward = 0.0

    def add_item(self, item):
        # Adds an item to the list of items and updates the total reward.

        if item in self.REWARDS:
            self.items.append(item)
            self.total_reward += self.REWARDS[item]
            print(f"\nAdded item: {item}. Reward added: INR {self.REWARDS[item]}\n")
        else:
            print("\nInvalid item. Please enter GLASS BOTTLE, PLASTIC BOTTLE or TIN CONTAINER\n")

    def view_total_items(self):
        """
        Prints the total number of items added by the user and displays a table of the items and their counts.
        If no items have been added, it prints a message indicating that no items have been added.
        """
         
        if len(self.items) == 0:
            print("\nNo items added by you.\n")
            return 
        print(f"\nFollowing items added by you-\n")
        counts = {}
        for item in self.items:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        items_df = pd.DataFrame(list(counts.items()), columns=['Item', 'Count'])
        items_df.index = items_df.index + 1
        print(items_df,"\n")
    
    def view_total_reward(self):
        # Prints total rewards value in INR earned by a user
        print(f"\nYour total reward: INR {self.total_reward:.2f}\n")

    def reset_system(self):
        # Resets the instance variables 'items' and 'total_reward' to empty list and 0.0 respectively when user choose 4 to reset system
        self.items = []
        self.total_reward = 0.0
        print("\nSystem reset for a new user session.\n")

def main():
    """
    The main function of the program.
    creates object of class and starts functionalities as per user selection
    """
    system = ItemsRecyclingSystem()
    while True:
        print("Enter 1 to add an item")
        print("Enter 2 to view all items added by you")
        print("Enter 3 to view total reward")
        print("Enter 4 to reset system")
        print("Enter 5 to exit\n\n")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("Enter an item to add (GLASS BOTTLE, PLASTIC BOTTLE or TIN CONTAINER)\n").upper()
            system.add_item(item)
        elif choice == '2':
            system.view_total_items()
        elif choice == '3':
            system.view_total_reward()
        elif choice == '4':
            system.reset_system()
        elif choice == '5':
            print("\nExiting\nThanks for using this system.\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, 4 or 5.\n")

if __name__ == "__main__":
    print("-----------------------------------------------------------")
    print("AUTOMATED COLLECTION AND REWARD SYSTEM FOR RECYCLABLE ITEMS")
    print("-----------------------------------------------------------")
    main()
