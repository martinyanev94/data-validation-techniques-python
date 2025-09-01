aggregated_sales = sales_data.agg(['sum', 'mean', 'max'])
print(aggregated_sales)
mean      342.857142
max       500.0
dtype: float64
