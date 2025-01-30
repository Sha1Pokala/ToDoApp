import pandas as pd 

df1 = pd.DataFrame({
    "EmployeeID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Age": [30, 35, 40]
})

# Merge on different column names
merged_df = pd.merge(df1, df2, left_on="EmployeeID", right_on="ID")
print(merged_df)

