data_with_nan = {
    'Fruit': ['Apple', 'Banana', None, 'Apple', 'Banana', 'Cherry', 'Banana', 'apple'],
    'Color': ['Red', 'Yellow', 'Orange', None, 'Yellow', 'Red', 'Yellow', 'red']
}

df_nan = pd.DataFrame(data_with_nan)
print(df_nan)
# Normalize text entries and fill missing values
df_nan['Fruit'] = df_nan['Fruit'].str.capitalize().fillna('Unknown')
df_nan['Color'] = df_nan['Color'].str.capitalize().fillna('Unknown')

fruit_nan_counts = df_nan['Fruit'].value_counts()
print(fruit_nan_counts)
