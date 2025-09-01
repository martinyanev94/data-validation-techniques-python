# Extracting year, month, and day
df_dates['year'] = df_dates['date'].dt.year
df_dates['month'] = df_dates['date'].dt.month
df_dates['day'] = df_dates['date'].dt.day
df_dates['day_of_week'] = df_dates['date'].dt.day_name()

print(df_dates)
