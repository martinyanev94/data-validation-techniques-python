# Check for missing values in each column
missing_values = df.isnull().sum()
print('Missing values in each column:')
print(missing_values)
