df['car_brand'] = df['car_brand'].cat.add_categories('Unknown')
df.loc[3, 'car_brand'] = 'Unknown'  # Introducing an unknown value
print(df)
