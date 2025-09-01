import matplotlib.pyplot as plt

df.groupby('car_brand')['sales'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Car Sales by Brand')
plt.xlabel('Car Brand')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()
