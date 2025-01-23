# Create the following DataFrame using pandas:

# Name	Age	City
# John	28	Houston
# Emma	24	Seattle
# Olivia	30	Boston
# Print the entire DataFrame.
# Access and print the "City" column.
# Access and print the second row (index 1).

import pandas as pd

data={ 
     "Name": ["John", "Emma", "Olivia"],
     "Age": [28, 24, 30],
     "City": ["Houston", "Seattle", "Boston"]
}

df= pd.DataFrame(data)

# Print the entire DataFrame.
print ("DataFrame:\n", df)

# Access and print the "City" column.
print (df["City"])

# Access and print the second row (index 1).
print (df.iloc[1])