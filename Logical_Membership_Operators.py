# Question 2: Logical and Membership Operators
# Write a Python program that:

# Defines a list of five fruits: ["apple", "banana", "cherry", "date", "grape"].
# Asks the user to input a fruit name.
# Checks if the entered fruit is in the list and:
# If found, prints "The fruit is available."
# If not found, prints "The fruit is not available."
# Use the not operator to ensure the program handles negative cases correctly.

# Defines a list of five fruits: ["apple", "banana", "cherry", "date", "grape"].
Fruits= ["apple", "banana", "cherry", "date", "grape"]

# Asks the user to input a fruit name.
Choosen_fruit=input("Enter a fruit name=  " ).lower()

# Checks if the entered fruit is in the list and:

if Choosen_fruit in Fruits:
 print ("The fruit is available.")

else:
 print ("The fruit is not available.")


