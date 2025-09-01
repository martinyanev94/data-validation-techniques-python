import pandas as pd

# Create a date range
date_range = pd.date_range(start='2023-01-01', end='2023-01-10')
print(date_range)
start_date = pd.Timestamp('2023-01-01')
end_date = pd.Timestamp('2023-01-10')

# Calculate the difference
difference = end_date - start_date
print(f"The difference in days is: {difference.days}")
