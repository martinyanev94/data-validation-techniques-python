print(df['car_brand'].cat.categories)
print(df['car_brand'].cat.codes)
total_sales = df.groupby('car_brand')['sales'].sum()
print(total_sales)
