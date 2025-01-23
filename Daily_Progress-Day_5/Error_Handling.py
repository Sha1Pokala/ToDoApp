# Let’s try a simple task to practice:

# Task: Write a program where the user inputs two numbers and the program divides them. Handle cases where:

# The input is not a number.
# The user tries to divide by zero.
# Let me know when you're ready!

try:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter second number: "))
    print( number1 / number2)
except ValueError:
    print("You must enter a valid integer!")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
finally:
    print("Program execution completed.")

