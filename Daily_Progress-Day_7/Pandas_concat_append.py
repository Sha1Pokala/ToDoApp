
# Example 1: Vertical Concatenation (default)

print("Choose 1 if you don't want to rearrange the index\nor Choose 2 if you want to rearrange the index")

import pandas as pd
Number= int(input("Enter a number:  "))

# Sample DataFrames
df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Alice", "Bob"]
})

df2 = pd.DataFrame({
    "ID": [3, 4],
    "Name": ["Charlie", "David"]
})

# pd.concat([df1, df2]) stacks the two DataFrames vertically.
concat_df = pd.concat([df1, df2])

# The append() method adds rows to a DataFrame, similar to vertical concatenation.
concat_df1 = pd.concat([df1, df2], ignore_index=True)

# Horizontal Concatenation
concat_df_horizontal = pd.concat([df1, df2], axis=1)

if Number == 1 :
# Concatenate DataFrames vertically
 print(concat_df)

elif Number == 2 :
 print(concat_df1)

elif Number==3:
 print(concat_df_horizontal)

else:
 print ("Enter a Valid number")
