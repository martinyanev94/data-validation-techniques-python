import matplotlib.pyplot as plt

# Plot a histogram for a specific column
plt.hist(df['numerical_column'], bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
