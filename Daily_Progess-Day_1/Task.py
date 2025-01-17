# Step 1: Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2 and 3: Create a menu inside a loop
while True:  # Infinite loop to keep the program running
    print("\nWhat would you like to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Step 3: Get the user's choice
    choice = input("Enter your choice (1/2/3/4/5): ")

    # Perform the chosen operation
    if choice == "1":
        print("Result of addition:", num1 + num2)
    elif choice == "2":
        print("Result of subtraction:", num1 - num2)
    elif choice == "3":
        print("Result of multiplication:", num1 * num2)
    elif choice == "4":
        # Handle division carefully (avoid division by zero)
        if num2 != 0:
            print("Result of division:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
