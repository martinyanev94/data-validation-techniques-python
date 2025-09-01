import matplotlib.pyplot as plt

# Convert 'datetime' to just date for daily aggregation
df['date'] = df['datetime'].dt.date

# Count the number of crimes per day
daily_crimes = df.groupby('date').size()

# Plotting the daily crime counts
plt.figure(figsize=(12, 6))
plt.plot(daily_crimes.index, daily_crimes.values)
plt.title('Daily Crime Count in Denver')
plt.xlabel('Date')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.show()
