# Suppose we have another Series for sales
sales_data = pd.Series([100, 200, 300, 400, 500], index=["a", "b", "c", "d", "e"])

# Filter by sales greater than 250
high_sales = sales_data[sales_data > 250]
print(high_sales)
d    400
e    500
dtype: int64
