import pandas as pd

# Display options to guide the user
print("Please choose an option from the menu below:")
print("1. View the original DataFrame")
print("2. Check for missing values in the DataFrame")
print("3. Drop rows or columns with missing values")
print("4. Fill missing values with a default value")
print("5. Fill missing values in the 'Age' column with the mean value")
print("6. Replace missing names with 'No Name'")

# Get user input for operation
Number = int(input("\nEnter a number corresponding to the operation you want to perform: "))

# Get user input to define axis for dropping rows/columns if needed (option 3)
if Number == 3:
    print("\nFor dropping rows or columns, choose the axis:")
    print("0 - Drop rows with missing values")
    print("1 - Drop columns with missing values")
    axis_to_drop = int(input("Enter axis (0 for rows, 1 for columns): "))

# Sample DataFrame with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", None],
    "Age": [25, None, 35, 28],
    "City": ["New York", "Los Angeles", None, "Chicago"]
}
df = pd.DataFrame(data)

# Option 1: Show the original DataFrame
if Number == 1:
    print("\nOriginal DataFrame:")
    print(df)

# Option 2: Check for missing values
elif Number == 2:
    print("\nMissing value check (True indicates missing values):")
    print(df.isna())

# Option 3: Drop rows or columns with missing values
elif Number == 3:
    if axis_to_drop in [0, 1]:
        # Drop rows or columns based on the user's input axis
        df_dropped = df.dropna(axis=axis_to_drop)
        print("\nDataFrame after dropping rows/columns with missing values:")
        print(df_dropped)
    else:
        print("Invalid axis. Please enter 0 (for rows) or 1 (for columns).")

# Option 4: Fill all missing values with a default value
elif Number == 4:
    # Fill all missing values with 'Unknown'
    df_filled = df.fillna("Unknown")
    print("\nDataFrame after filling missing values with 'Unknown':")
    print(df_filled)

# Option 5: Fill missing values in the 'Age' column with the mean of the column
elif Number == 5:
    # Fill missing values in 'Age' with the mean of the column
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    print("\nDataFrame after filling missing 'Age' values with the mean:")
    print(df)

# Option 6: Replace missing names with 'No Name'
elif Number == 6:
    # Replace missing values in the 'Name' column with 'No Name'
    df["Name"] = df["Name"].fillna("No Name")
    print("\nDataFrame after replacing missing names with 'No Name':")
    print(df)

# Invalid option handling
else:
    print("\nInvalid option. Please enter a valid number from 1 to 6.")
