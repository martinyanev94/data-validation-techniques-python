data = {
    'Product': ['A', 'B', 'C'],
    'Quantity': [10, 15, 5],
    'Price_per_Unit': [20, 30, 40]
}
sales_df = pd.DataFrame(data)
sales_df['Total_Sales'] = sales_df.apply(lambda row: row['Quantity'] * row['Price_per_Unit'], axis=1)
print(sales_df)
0       A        10               20           200
1       B        15               30           450
2       C         5               40           200
