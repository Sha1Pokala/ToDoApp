# Practice Time

# Create a Calculator Function: Write a function that accepts two numbers and 
# an operator (+, -, *, /) as input and returns the result of the operation.


# Define functions for operations(functions should be declared outside the conditional logic)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
Operator = input("Enter the operator you want to use (+, -, *, /): ")

# Perform the chosen operation
if Operator == "+":
    print("Result:", add(a, b))
elif Operator == "-":
    print("Result:", subtract(a, b))
elif Operator == "*":
    print("Result:", multiply(a, b))
elif Operator == "/":
    print("Result:", divide(a, b))
else:
    print("Invalid operator!")

    
