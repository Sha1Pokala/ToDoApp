
# You have sales data, and you want to know:

# The total revenue per region.
# The number of unique products sold per region.
# Sample sales data

import pandas as pd

sales_data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'East'],
    'Product': ['A', 'B', 'C', 'A', 'C', 'D'],
    'Revenue': [100, 200, 150, 120, 220, 180]
}

sales_df = pd.DataFrame(sales_data)

# Total revenue per region
total_revenue = sales_df.groupby('Region')['Revenue'].sum()

# Number of unique products sold per region
unique_products = sales_df.groupby('Region')['Product'].nunique()

print("\nTotal Revenue by Region:")
print(total_revenue)

print("\nUnique Products Sold by Region:")
print(unique_products)
