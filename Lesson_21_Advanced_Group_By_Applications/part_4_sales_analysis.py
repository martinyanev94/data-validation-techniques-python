filtered_data = df[df['Sales'] > 300]
condition_result = filtered_data.groupby(['Region', 'Product']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Returns=('Returns', 'sum')
).reset_index()

print(condition_result)
0  East      A           500             12
1  North     B           300             10
2  South     A           450              5
3  South     B           350              8
