# Mean imputation
mean_temp = df['Temperature'].mean()
df['Temperature'].fillna(mean_temp, inplace=True)
print("Data after mean imputation:\n", df)
