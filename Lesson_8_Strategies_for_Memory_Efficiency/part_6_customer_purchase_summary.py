# Group by CustomerID and aggregate PurchaseAmount
summary_df = df.groupby('CustomerID', as_index=False)['PurchaseAmount'].sum()

print(summary_df.head())
