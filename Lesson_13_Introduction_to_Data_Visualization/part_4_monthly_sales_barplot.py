import seaborn as sns
import pandas as pd

# Creating a DataFrame from the data
data = pd.DataFrame({
    'Months': months,
    'Sales': sales
})

# Create a bar plot
sns.barplot(x='Months', y='Sales', data=data, palette='viridis')
plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales in USD')
plt.xticks(rotation=45)
plt.show()
