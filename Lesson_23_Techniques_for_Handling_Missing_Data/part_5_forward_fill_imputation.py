# Forward fill imputation
df['Temperature'].fillna(method='ffill', inplace=True)
print("Data after forward fill:\n", df)
