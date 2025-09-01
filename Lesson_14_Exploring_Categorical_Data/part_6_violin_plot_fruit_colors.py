import seaborn as sns

# Create a violin plot for fruit and their color
sns.violinplot(x='Fruit', y='Color', data=df_nan, inner='quartile')
plt.title('Violin Plot of Fruit Colors')
plt.show()
