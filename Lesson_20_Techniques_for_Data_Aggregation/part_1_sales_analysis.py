import pandas as pd

sales_data = {
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [200, 150, 300, 250, 400, 120],
    'Returns': [10, 5, 8, 2, 15, 1]
}

df = pd.DataFrame(sales_data)
result = df.groupby("Region").agg(
    Total_Sales=pd.NamedAgg(column="Sales", aggfunc="sum"),
    Total_Returns=pd.NamedAgg(column="Returns", aggfunc="sum"),
)
print(result)
Region                            
North           900              33
South           520              8
