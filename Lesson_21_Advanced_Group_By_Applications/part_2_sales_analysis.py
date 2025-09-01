result = df.groupby(['Region', 'Product']).agg(
    Total_Sales=('Sales', 'sum'),
    Average_Sales=('Sales', 'mean'),
    Max_Sales=('Sales', 'max'),
    Min_Sales=('Sales', 'min'),
    Total_Returns=('Returns', 'sum')
).reset_index()

print(result)
0  East      A           500           500.0        500        500             12
1  East      B           250           250.0        250        250              4
2  North     A           200           200.0        200        200             15
3  North     B           300           300.0        300        300             10
4  South     A           450           450.0        450        450              5
5  South     B           350           350.0        350        350              8
