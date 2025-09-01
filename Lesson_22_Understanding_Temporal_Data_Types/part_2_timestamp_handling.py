# Create a timestamp
timestamp = pd.Timestamp('2023-01-10 14:30:00')

# Extracting date and time
date_part = timestamp.date()
time_part = timestamp.time()

print(f"Date part: {date_part}")
print(f"Time part: {time_part}")
# Create a naive timestamp
naive_timestamp = pd.Timestamp('2023-01-10 14:30:00')

# Localize to a timezone
aware_timestamp = naive_timestamp.tz_localize('America/New_York')

print(f"Naive Timestamp: {naive_timestamp}")
print(f"Timezone-Aware Timestamp: {aware_timestamp}")
