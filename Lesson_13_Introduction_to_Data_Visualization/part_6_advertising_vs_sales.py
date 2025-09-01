advertising_spend = [200, 300, 400, 500, 600, 700]
sales_revenue = [1500, 2200, 3200, 4000, 4500, 5900]

plt.scatter(advertising_spend, sales_revenue, color='blue', s=100)
plt.title('Advertising Spend vs Sales Revenue')
plt.xlabel('Advertising Spend (in USD)')
plt.ylabel('Sales Revenue (in USD)')
plt.grid(True)
plt.show()
