# Practice Time
# Grocery List:
# Create a list of groceries (e.g., milk, eggs, bread).
# Add a new item to the list.
# Remove an item from the list.
# Print the final list.

# Initial list of grocery items


grocery_items = ["Eggs", "bananas", "bread", "veggies"]

# Taking the user's choice of operation
print("Choose an operation:")
print("1. Add an item")
print("2. Remove an item")
print("3. View the grocery list")
user_input = int(input("Enter the choice of operation you want to perform (1/2/3): "))

if user_input == 1:
    # Adding an item
    items_to_add = input("Enter the item to add: ").capitalize()
    grocery_items.append(items_to_add)
    print(f"'{items_to_add}' has been added. Updated list: {grocery_items}")
elif user_input == 2:
    # Removing an item
    items_to_remove = input("Enter the item to remove: ").capitalize()
    if items_to_remove in grocery_items:
        grocery_items.remove(items_to_remove)
        print(f"'{items_to_remove}' has been removed. Updated list: {grocery_items}")
    else:
        print(f"'{items_to_remove}' is not in the list.")
elif user_input == 3:
    # Viewing the grocery list
    print("Your grocery list:", grocery_items)
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
