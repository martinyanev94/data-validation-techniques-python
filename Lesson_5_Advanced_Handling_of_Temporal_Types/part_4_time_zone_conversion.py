# Localizing to a specific time zone
df_dates['date_localized'] = df_dates['date'].dt.tz_localize('UTC')

# Converting to another time zone
df_dates['date_ny'] = df_dates['date_localized'].dt.tz_convert('America/New_York')

print(df_dates)
