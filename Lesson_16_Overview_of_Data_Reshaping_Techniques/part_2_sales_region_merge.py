sales = pd.DataFrame({
    'salesperson': ['John', 'Jane', 'John'],
    'sales': [100, 200, 150]
})

regions = pd.DataFrame({
    'salesperson': ['John', 'Jane'],
    'region': ['Northeast', 'Southwest']
})

# Merging DataFrames
merged_df = pd.merge(sales, regions, on='salesperson')
print(merged_df)
