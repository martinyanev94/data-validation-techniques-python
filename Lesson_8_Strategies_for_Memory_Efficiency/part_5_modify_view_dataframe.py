# Create a view (not a copy)
view_df = df[['CustomerID', 'PurchaseAmount']]

# Modify the view
view_df['PurchaseAmount'] *= 1.1  # Apply a discount adjustment

print(view_df.head())
