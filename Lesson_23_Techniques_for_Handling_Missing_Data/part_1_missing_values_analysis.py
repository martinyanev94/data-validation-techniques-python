import pandas as pd

# Sample data
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Temperature': [22, 21, None, 25, None, 24, 23]
}

df = pd.DataFrame(data)

# Identifying missing values
missing_values = df.isnull().sum()
print("Missing values count:\n", missing_values)
