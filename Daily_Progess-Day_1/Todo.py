print("Welcome to your To-Do List App!")

while True:  # Infinite loop to keep the app running
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "3":  # Check if the user wants to exit
        print("Thank you for using the To-Do List App. Goodbye!")
        break  # Exit the loop
    else:
        print("You chose option", choice)