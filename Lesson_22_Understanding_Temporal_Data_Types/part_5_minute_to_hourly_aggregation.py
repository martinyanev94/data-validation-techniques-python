# Create a minute-level date range
minute_dates = pd.date_range(start='2023-01-01', periods=120, freq='T')
minute_data = pd.Series(range(120), index=minute_dates)

# Group by hour and sum the values
hourly_data = minute_data.resample('H').sum()
print(hourly_data)
