df['car_brand'] = df['car_brand'].cat.rename_categories({'Toyota': 'Toyota & Lexus'})
print(df)
