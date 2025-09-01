# Median imputation
median_temp = df['Temperature'].median()
df['Temperature'].fillna(median_temp, inplace=True)
print("Data after median imputation:\n", df)
