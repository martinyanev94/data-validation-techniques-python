# Calculating temperature change
df_dates['temp_change'] = df_dates['temperature'].diff()
# Calculating timedelta (number of days between dates)
df_dates['days_since_start'] = (df_dates['date'] - df_dates['date'].min()).dt.days

print(df_dates)
