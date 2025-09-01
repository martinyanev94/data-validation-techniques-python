def custom_average(series):
    return sum(series) / len(series) if len(series) > 0 else 0

result = df.groupby("widget").agg(
    custom_avg=pd.NamedAgg(column="sales", aggfunc=custom_average)
)
print(result)
