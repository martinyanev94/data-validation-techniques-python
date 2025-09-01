# Plotting a pie chart
plt.pie(fruit_counts, labels=fruit_counts.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.title('Fruit Distribution')
plt.show()
