filtered_cities = df[df['City'].str.contains('o')]
print(filtered_cities)
df['City'] = df['City'].astype('category')
print(df['City'].dtypes)
