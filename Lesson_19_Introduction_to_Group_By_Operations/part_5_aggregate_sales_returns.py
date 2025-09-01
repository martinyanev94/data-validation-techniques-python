result = df.groupby(["widget", "region"]).agg(
    sales_total=pd.NamedAgg(column="sales", aggfunc="sum"),
    returns_total=pd.NamedAgg(column="returns", aggfunc="sum"),
    sales_min=pd.NamedAgg(column="sales", aggfunc="min"),
    returns_min=pd.NamedAgg(column="returns", aggfunc="min"),
)
print(result)
