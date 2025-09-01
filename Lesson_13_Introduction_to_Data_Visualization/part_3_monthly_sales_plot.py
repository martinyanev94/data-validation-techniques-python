import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1500, 2000, 3000, 2500, 4000, 3500, 4500, 3000, 5000, 6000, 7000, 8000]

plt.plot(months, sales, marker='o')
plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales in USD')
plt.grid(True)
plt.show()
