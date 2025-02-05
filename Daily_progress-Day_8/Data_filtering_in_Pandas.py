# Tasks:
# Select Columns: Extract only the columns Name and Salary.
# Filter Condition: Filter employees who have a salary greater than 55,000.
# Multiple Conditions: Find employees in the IT department with more than 4 years of experience.
# Missing Values: Identify and display rows where the Department is missing (NaN).
# Sorting: Filter employees with a salary greater than 50,000 and sort the result by Years_of_Experience in descending order.

import pandas as pd

# Employee dataset
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106],
    'Name': ['John', 'Sarah', 'Mike', 'Anna', 'James', 'Laura'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing', None],
    'Salary': [50000, 60000, 55000, 52000, 48000, 45000],
    'Years_of_Experience': [5, 7, 6, 4, 3, 2]
}

df = pd.DataFrame(data)

# 1. Select only the Name and Salary columns
name_salary_df = df[['Name', 'Salary']]
print("1. Selected Name and Salary Columns:")
print(name_salary_df)

# 2. Filter employees with Salary > 55,000
high_salary_df = df[df['Salary'] > 55000]
print("\n2. Employees with Salary > 55,000:")
print(high_salary_df)

# 3. Filter employees in IT department with > 4 years of experience
it_experience_df = df[(df['Department'] == 'IT') & (df['Years_of_Experience'] > 4)]
print("\n3. IT Employees with More Than 4 Years of Experience:")
print(it_experience_df)

# 4. Identify rows with missing Department values
missing_department_df = df[df['Department'].isna()]
print("\n4. Rows with Missing Department:")
print(missing_department_df)

# 5. Filter employees with Salary > 50,000 and sort by Years_of_Experience descending
sorted_filtered_df = df[df['Salary'] > 50000].sort_values(by='Years_of_Experience', ascending=False)
print("\n5. Filtered Employees with Salary > 50,000 (Sorted by Experience):")
print(sorted_filtered_df)

# Bonus Task: Use the .query() method to filter salary between 50,000 and 60,000
query_filtered_df = df.query('50000 < Salary < 60000')
print("\nBonus Task: Employees with Salary between 50,000 and 60,000:")
print(query_filtered_df)
