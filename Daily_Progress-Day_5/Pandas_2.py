# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "City": ["New York", "Los Angeles", "Chicago"]
# }
# df = pd.DataFrame(data)
# Add a new column called "Salary" with values [50000, 60000, 70000].
# Filter the DataFrame to show only rows where Age > 25.


import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
 }

df=pd.DataFrame(data)

# Add a new column called "Salary" with values [50000, 60000, 70000].
df["Salary"]= [50000,60000,70000]
print(df)

 #Filter the DataFrame to show only rows where Age > 25.
filtered_df = df[df["Age"] > 25]
print(filtered_df)


