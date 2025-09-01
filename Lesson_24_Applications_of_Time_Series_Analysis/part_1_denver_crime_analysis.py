import pandas as pd

# Load the dataset
df = pd.read_csv('denver_crime_data.csv', parse_dates=['datetime'])

# Display the initial rows of the dataset
print(df.head())
