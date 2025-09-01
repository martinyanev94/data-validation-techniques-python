# Create a date range with missing data
complete_dates = pd.date_range(start='2023-01-01', end='2023-01-05')
data_with_gaps = pd.Series([1, 2, None, 4, None], index=complete_dates)

# Fill missing values with forward fill method
filled_data = data_with_gaps.ffill()
print(filled_data)
