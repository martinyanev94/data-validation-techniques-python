df['City_Upper'] = df['City'].str.upper()  # Convert city names to uppercase
print(df[['City', 'City_Upper']])
