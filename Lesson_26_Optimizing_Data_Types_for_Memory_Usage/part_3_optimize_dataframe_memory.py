import numpy as np

# New sample DataFrame
data_numbers = {
    'ProductID': [1, 2, 3, 4, 5],
    'Quantity': [120, 30, 85, 40, 25]  # values within np.int8 range
}

df_numbers = pd.DataFrame(data_numbers)

# Changing data types to optimize memory usage
df_numbers['ProductID'] = df_numbers['ProductID'].astype(np.int8)
df_numbers['Quantity'] = df_numbers['Quantity'].astype(np.int8)

# Check the memory usage
print(df_numbers.memory_usage(deep=True))
