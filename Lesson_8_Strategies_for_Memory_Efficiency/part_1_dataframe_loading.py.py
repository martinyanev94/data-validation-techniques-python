# Define the data types to use
dtypes = {
    'CustomerID': 'int32',        # Assuming CustomerID can fit in int32
    'Age': 'int8',                # Keeping the age as an int8
    'PurchaseAmount': 'float32'   # Assume purchase amounts do not need float64
}

# Read the CSV with specified data types
df = pd.read_csv(csv_file_path, usecols=['CustomerID', 'Age', 'PurchaseAmount'], dtype=dtypes)

print(df.info())
