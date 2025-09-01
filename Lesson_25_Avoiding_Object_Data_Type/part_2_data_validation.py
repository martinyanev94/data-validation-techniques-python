data_inconsistent = {
    'City': ['Denver', 'Los Angeles', 12345, 'Chicago'],
    'Population': [715522, 3971883, 8419600, 'Not a Number']
}

df_inconsistent = pd.DataFrame(data_inconsistent)

# Attempt to filter out cities containing 'o'
try:
    filtered_cities_inconsistent = df_inconsistent[df_inconsistent['City'].str.contains('o')]
except Exception as e:
    print(f"Error: {e}")
