# Sample quarterly data over two years
quarters = ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022']
quarterly_sales = [1500, 2500, 3500, 5000, 6500, 7000, 8000, 9500]

plt.plot(quarters, quarterly_sales, marker='s', color='green')
plt.title('Quarterly Sales Data')
plt.xlabel('Quarters')
plt.ylabel('Sales in USD')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
