# Merge the two DataFrames with an outer join
outer_merged_df = pd.merge(customers, orders, on='CustomerID', how='outer')
print(outer_merged_df)
