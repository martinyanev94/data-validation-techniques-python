import matplotlib.pyplot as plt

# Create a simple time series plot
plt.figure(figsize=(10, 6))
plt.plot(hourly_data.index, hourly_data.values)
plt.title('Hourly Data Trends')
plt.xlabel('Date')
plt.ylabel('Values')
plt.grid()
plt.show()
