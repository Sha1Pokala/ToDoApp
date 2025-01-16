import math  # Import math for advanced mathematical operations

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def factorial(n):
    if n >= 0:
        return math.factorial(n)
    else:
        return "Error: Factorial of a negative number is not defined."

def power(a, b):
    return a ** b

def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Square root of a negative number is not defined."

def menu():
    print("\n--- Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("6. Power (a^b)")
    print("7. Square Root")
    print("8. Exit")

while True:
    menu()
    try:
        choice = int(input("Enter your choice (1-8): "))
        if choice == 1:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("Result:", addition(a, b))
        elif choice == 2:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("Result:", subtraction(a, b))
        elif choice == 3:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("Result:", multiplication(a, b))
        elif choice == 4:
            a = float(input("Enter the numerator: "))
            b = float(input("Enter the denominator: "))
            print("Result:", division(a, b))
        elif choice == 5:
            n = int(input("Enter a number: "))
            print("Result:", factorial(n))
        elif choice == 6:
            a = float(input("Enter the base: "))
            b = float(input("Enter the exponent: "))
            print("Result:", power(a, b))
        elif choice == 7:
            a = float(input("Enter the number: "))
            print("Result:", square_root(a))
        elif choice == 8:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 8.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


