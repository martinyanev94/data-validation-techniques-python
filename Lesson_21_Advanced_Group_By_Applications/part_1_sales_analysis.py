import pandas as pd

data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [200, 300, 450, 350, 500, 250],
    'Returns': [15, 10, 5, 8, 12, 4]
}

df = pd.DataFrame(data)
grouped_data = df.groupby(['Region', 'Product']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Returns=('Returns', 'sum'),
    Average_Sales=('Sales', 'mean')
).reset_index()

print(grouped_data)
0  East      A           500             12           500.0
1  East      B           250              4           250.0
2  North     A           200             15           200.0
3  North     B           300             10           300.0
4  South     A           450              5           450.0
5  South     B           350              8           350.0
