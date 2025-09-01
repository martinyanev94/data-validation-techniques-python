# Sample data for market share
labels = ['Company A', 'Company B', 'Company C', 'Company D']
sizes = [25, 35, 30, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.title('Market Share Distribution')
plt.show()
