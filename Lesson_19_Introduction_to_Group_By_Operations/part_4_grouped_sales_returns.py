result = df.groupby(["widget", "region"]).agg(
    sales_total=pd.NamedAgg(column="sales", aggfunc="sum"),
    returns_total=pd.NamedAgg(column="returns", aggfunc="sum"),
)
print(result)
widget    region                         
Widget A  North           13              2
          South           19              5
Widget B  North           11              0
          South           25             12
