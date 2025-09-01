import pandas as pd

# Creating a date range
date_range = pd.date_range(start='2024-01-01', periods=5, freq='D')

# Creating a DataFrame with datetime values
df_dates = pd.DataFrame({
    'date': date_range,
    'temperature': [30.5, 32.0, 29.5, 28.0, 31.0]
})

print(df_dates)
