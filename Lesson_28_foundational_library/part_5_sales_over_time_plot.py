import matplotlib.pyplot as plt

# Assuming 'date' and 'sales' are columns in the DataFrame
plt.plot(df['date'], df['sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time')
plt.show()
