
# Find Maximum in a List:
# Write a program to find the largest number in a list of integers. answer this as well 


# List of integers
numbers = [10, 45, 2, 99, 23, 76, 8]

# Initialize a variable to hold the maximum value
max_number = numbers[0]  # Start by assuming the first number is the largest

# Loop through the list to find the maximum
for num in numbers:
    if num > max_number:  # Compare each number with the current max
        max_number = num

# Print the result
print("The largest number in the list is:", max_number)
