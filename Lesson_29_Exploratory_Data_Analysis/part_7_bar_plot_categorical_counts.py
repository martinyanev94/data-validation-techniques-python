# Creating a bar plot to represent counts of categorical data
category_counts = df['categorical_column'].value_counts()
category_counts.plot(kind='bar', color='orange', alpha=0.7)
plt.title('Counts of Categorical Column')
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.show()
