result = df.groupby(['Region', 'Product']).agg(
    Total_Sales=pd.NamedAgg(column="Sales", aggfunc="sum"),
    Average_Sales=pd.NamedAgg(column="Sales", aggfunc="mean"),
    Count_Returns=pd.NamedAgg(column="Returns", aggfunc="count"),
)
print(result)
Region Product                                                  
North  A             600           300.0           3
       B             300           300.0           1
South  A             150           150.0           1
       B             250           250.0           1
