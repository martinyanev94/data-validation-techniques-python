data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Home', 'Home'],
    'Sales': [250, 300, 150, 400, 350, 450],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South']
}

df = pd.DataFrame(data)
print(df)
0  Electronics    250  North
1      Clothing    300  South
2  Electronics    150  North
3      Clothing    400  South
4          Home    350  North
5          Home    450  South
result = df.groupby('Category')['Sales'].agg(['sum', 'mean'])
print(result)
Category
Clothing    700.0  350.000000
Electronics 400.0  200.000000
Home        800.0  400.000000
