fruit_counts = df['Fruit'].value_counts()
print(fruit_counts)
import matplotlib.pyplot as plt

fruit_counts.plot(kind='bar', color='skyblue')
plt.title('Fruit Count')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()
