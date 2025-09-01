plt.boxplot(df['Weight'], vert=True, patch_artist=True)
plt.title('Weight Box Plot')
plt.ylabel('Weight (kg)')
plt.grid(axis='y')
plt.show()
import numpy as np

df['Weight_Log'] = np.log(df['Weight'])
plt.hist(df['Weight_Log'], bins=5, color='green', edgecolor='black')
plt.title('Log-Transformed Weight Distribution Histogram')
plt.xlabel('Log of Weight (kg)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()
