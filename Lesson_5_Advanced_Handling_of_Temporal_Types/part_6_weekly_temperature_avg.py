# Resampling to weekly temperature averages
weekly_avg = df_dates.resample('W', on='date').mean()

print(weekly_avg)
