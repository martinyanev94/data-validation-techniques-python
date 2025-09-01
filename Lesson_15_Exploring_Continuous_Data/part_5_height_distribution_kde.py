import seaborn as sns

sns.histplot(df['Height'], kde=True)
plt.title('Height Distribution with KDE')
plt.xlabel('Height (cm)')
plt.ylabel('Density')
plt.grid(axis='y')
plt.show()
