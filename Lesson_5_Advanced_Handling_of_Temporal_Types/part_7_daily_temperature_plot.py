import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(df_dates['date'], df_dates['temperature'], marker='o', label='Daily Temperature')
plt.title('Daily Temperatures Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
