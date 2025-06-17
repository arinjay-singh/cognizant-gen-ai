# Inventory Management System

class Inventory:
    # initialize empty inventory
    def __init__(self):
        self.items = {}
        
    # add item to the inventory
    def add_item(self, item_name, quantity, price):
        """Add an item to the inventory."""
        # if the item already exists, update its quantity and price
        if item_name in self.items:
            self.items[item_name] = (quantity, price)
        # if the item does not exist, add it to the inventory
        else:
            self.items[item_name] = (quantity, price)
        # print confirmation message
        print(f"Added/Updated item: {item_name}, Quantity: {quantity}, Price: ${price:.2f}")

    # remove item from the inventory
    def remove_item(self, item_name):
        """Remove an item from the inventory."""
        # if the item exists, remove it from the inventory
        if item_name in self.items:
            del self.items[item_name]
            print(f"Removed item: {item_name}")
        # if the item does not exist, print an error message
        else:
            print(f"Item {item_name} not found in inventory.")
      
    # update item in the inventory      
    def update_item(self, item_name, quantity=None, price=None):
        """Update the quantity and/or price of an item."""
        # if the item exists, update its quantity and/or price
        if item_name in self.items:
            current_quantity, current_price = self.items[item_name]
            # update quantity and/or price if provided
            if quantity is not None:
                current_quantity = quantity
            if price is not None:
                current_price = price
            self.items[item_name] = (current_quantity, current_price)
            print(f"Updated item: {item_name}, Quantity: {current_quantity}, Price: ${current_price:.2f}")
        # if the item does not exist, print an error message
        else:
            print(f"Item {item_name} not found in inventory.")
            
    # display all items in the inventory (output is printed to console)
    def display_inventory(self):
        """Display all items in the inventory."""
        # if the inventory is empty, print a message
        if not self.items:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        # iterate through the items and print their details
        for item_name, (quantity, price) in self.items.items():
            print(f"Item: {item_name}, Quantity: {quantity}, Price: ${price:.2f}")
            
    # calculate the total value of all items in the inventory
    def calculate_total_value(self):
        """Calculate the total value of all items in the inventory."""
        # calculate total value by summing the product of quantity and price for each item
        total_value = sum(quantity * price for quantity, price in self.items.values())
        print(f"Total inventory value: ${total_value:.2f}")
        return total_value
    
# example usage
print("Welcome to the Inventory Management System\n")
inventory = Inventory()

# add items to the inventory
inventory.add_item("Apple", 10, 2.5)
inventory.add_item("Banana", 20, 1.2)
inventory.display_inventory
print()
# add mango to the inventory
inventory.add_item("Mango", 15, 3.0)
inventory.display_inventory()
print()
# update the quantity and price of an item
inventory.update_item("Banana", quantity=25, price=1.5)
inventory.display_inventory()
print()
# remove an item from the inventory
inventory.remove_item("Apple")
inventory.display_inventory()
print()
# calculate the total value of the inventory
inventory.calculate_total_value()


