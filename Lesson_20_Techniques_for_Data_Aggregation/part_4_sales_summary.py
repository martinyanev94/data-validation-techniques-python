sales_data = {
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Product': ['A', 'A', 'B', 'B', 'A', 'A'],
    'Sales': [200, 150, 300, 250, 400, 120],
    'Returns': [10, 5, 8, 2, 15, 1]
}
df = pd.DataFrame(sales_data)
result = df.groupby(['Region', 'Product']).agg(
    Total_Sales=pd.NamedAgg(column="Sales", aggfunc="sum"),
    Total_Returns=pd.NamedAgg(column="Returns", aggfunc="sum"),
)
print(result)
Region Product                            
North  A             600           25
       B             300            8
South  A             150            5
       B             250            2
