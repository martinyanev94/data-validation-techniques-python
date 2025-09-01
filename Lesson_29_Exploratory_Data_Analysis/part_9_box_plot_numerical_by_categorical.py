# Box plot of numerical column across categories
sns.boxplot(x='categorical_column', y='numerical_column', data=df)
plt.title('Box Plot of Numerical Column by Categorical Column')
plt.xlabel('Categorical Column')
plt.ylabel('Numerical Column')
plt.show()
