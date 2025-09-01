import pandas as pd

# Create a DataFrame with customer information
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [28, 34, 23]
})

# Create a DataFrame with order information
orders = pd.DataFrame({
    'OrderID': [101, 102, 103],
    'CustomerID': [1, 2, 1],
    'Product': ['Laptop', 'Phone', 'Tablet'],
    'Amount': [1200, 700, 300]
})

# Merge the two DataFrames on 'CustomerID'
merged_df = pd.merge(customers, orders, on='CustomerID', how='inner')
print(merged_df)
