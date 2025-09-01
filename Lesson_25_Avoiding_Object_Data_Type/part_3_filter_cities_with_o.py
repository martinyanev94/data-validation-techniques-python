df_inconsistent['City'] = df_inconsistent['City'].astype(str)
# Now we can filter again
filtered_cities_fixed = df_inconsistent[df_inconsistent['City'].str.contains('o')]
print(filtered_cities_fixed)
