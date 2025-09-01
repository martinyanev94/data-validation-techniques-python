# Specify data types while reading a CSV file
dtype_dict = {
    'ProductID': np.int8,
    'Quantity': np.int8,
    'Price': np.float32,
    'City': 'category'
}

df_large = pd.read_csv('large_dataset.csv', dtype=dtype_dict)

# Examine the DataFrame structure and memory usage
print(df_large.dtypes)
print(df_large.memory_usage(deep=True))
