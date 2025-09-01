# Fill missing age values with -1 to indicate unknown
df['Age'] = df['Age'].fillna(-1).astype('int8')  # explicitly use int8

# Or, if Age is not needed
# df = df.drop('Age', axis=1)

print(df.info())
