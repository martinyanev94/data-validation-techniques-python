import pandas as pd

# Specify the CSV file path
csv_file_path = 'customer_data.csv'

# Load only specific columns from the CSV file
df = pd.read_csv(csv_file_path, usecols=['CustomerID', 'PurchaseAmount'])

print(df.head())
