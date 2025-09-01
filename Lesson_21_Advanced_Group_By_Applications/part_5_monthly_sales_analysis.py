data = {
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', 
                            '2023-02-01', '2023-02-02']),
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [200, 300, 450, 350, 500, 250],
    'Returns': [15, 10, 5, 8, 12, 4]
}

df = pd.DataFrame(data)
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby(['Month', 'Region']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Returns=('Returns', 'sum')
).reset_index()

print(monthly_sales)
0  2023-01  North           500             25
1  2023-01  South           350             8
2  2023-02   East           750             16
