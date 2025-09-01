def apply_discount(total):
    discount_rate = 0.1  # 10% discount
    return total * (1 - discount_rate)

discounted_results = df.groupby("Region").agg(
    Discounted_Total_Sales=pd.NamedAgg(column="Sales", aggfunc=apply_discount),
)
print(discounted_results)
Region                          
North                   810.0
South                   540.0
