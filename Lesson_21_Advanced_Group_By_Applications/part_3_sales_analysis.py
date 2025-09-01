def sales_range(sales):
    return sales.max() - sales.min()
custom_result = df.groupby(['Region', 'Product']).agg(
    Total_Sales=('Sales', 'sum'),
    Sales_Range=('Sales', sales_range),
    Total_Returns=('Returns', 'sum')
).reset_index()

print(custom_result)
0  East      A           500           0            12
1  East      B           250           0             4
2  North     A           200           0            15
3  North     B           300           0            10
4  South     A           450           0             5
5  South     B           350           0             8
