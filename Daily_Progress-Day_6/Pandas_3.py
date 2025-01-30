import pandas as pd

# Creating a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "City": ["New York", "Los Angeles", "New York", "Chicago", "Los Angeles"],
    "Salary": [60000, 75000, 50000, 90000, 80000]
}

df = pd.DataFrame(data)

# Grouping by City and calculating the average salary
grouped_df = df.groupby("City")["Salary"].mean()
print(grouped_df)

# Grouping by City and applying multiple aggregations
grouped_df1 = df.groupby("City").agg({"Salary": ["mean", "sum", "count"]})
print(grouped_df1)

