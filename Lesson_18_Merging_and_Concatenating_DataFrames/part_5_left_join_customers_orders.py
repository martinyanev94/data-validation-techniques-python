# Perform a left join
left_merged_df = pd.merge(customers, orders, on='CustomerID', how='left')
print(left_merged_df)
