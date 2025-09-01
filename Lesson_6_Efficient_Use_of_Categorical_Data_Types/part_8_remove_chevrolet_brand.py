df['car_brand'] = df['car_brand'].cat.remove_categories('Chevrolet')
print(df)
