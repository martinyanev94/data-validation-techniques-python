# Create an hourly date range
hourly_dates = pd.date_range(start='2023-01-01', periods=24, freq='H')
print(hourly_dates)
# Assume we have hourly data
data = pd.Series(range(24), index=hourly_dates)

# Resample to daily averages
daily_avg = data.resample('D').mean()
print(daily_avg)
