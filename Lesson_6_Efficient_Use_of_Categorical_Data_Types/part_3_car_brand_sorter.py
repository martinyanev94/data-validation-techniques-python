car_order = pd.CategoricalDtype(categories=['Toyota', 'Honda', 'Ford', 'Chevrolet'], ordered=True)
df['car_brand'] = df['car_brand'].astype(car_order)

sorted_brands = df.sort_values('car_brand')
print(sorted_brands)
