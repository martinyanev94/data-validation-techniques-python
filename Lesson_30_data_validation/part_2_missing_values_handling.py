# Identify missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Dropping rows with missing values
df_clean = df.dropna()
print("Data after dropping missing values:")
print(df_clean)

# Alternatively, filling missing values
df_filled = df.fillna({'age': df['age'].mean(), 'birthdate': pd.Timestamp('2000-01-01')})
print("Data after filling missing values:")
print(df_filled)
