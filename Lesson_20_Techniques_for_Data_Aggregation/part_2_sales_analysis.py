result = df.groupby("Region").agg(
    Total_Sales=pd.NamedAgg(column="Sales", aggfunc="sum"),
    Average_Sales=pd.NamedAgg(column="Sales", aggfunc="mean"),
    Total_Returns=pd.NamedAgg(column="Returns", aggfunc="sum"),
    Average_Returns=pd.NamedAgg(column="Returns", aggfunc="mean"),
)
print(result)
Region                                                       
North           900            300           33               11
South           520            260            8                2.67
