height_mean = df['Height'].mean()
height_median = df['Height'].median()
height_std = df['Height'].std()

weight_mean = df['Weight'].mean()
weight_median = df['Weight'].median()
weight_std = df['Weight'].std()

print(f"Height - Mean: {height_mean}, Median: {height_median}, Std Dev: {height_std}")
print(f"Weight - Mean: {weight_mean}, Median: {weight_median}, Std Dev: {weight_std}")
import matplotlib.pyplot as plt

plt.scatter(df['Height'], df['Weight'], color='blue')
plt.title('Height vs Weight Scatter Plot')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.grid(True)
plt.show()
