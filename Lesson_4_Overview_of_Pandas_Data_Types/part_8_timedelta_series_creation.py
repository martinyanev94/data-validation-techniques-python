# Creating a timedelta Series
timedelta_series = pd.Series([pd.Timedelta(days=x) for x in range(3)])
print(timedelta_series)
1   1 days
2   2 days
dtype: timedelta64[ns]
