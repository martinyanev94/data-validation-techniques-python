def calculate_range(series):
    return series.max() - series.min()

aggregated_custom = sales_data.agg(['sum', 'mean', calculate_range])
print(aggregated_custom)
mean         342.857142
<function calculate_range at 0x...>    350
dtype: object
