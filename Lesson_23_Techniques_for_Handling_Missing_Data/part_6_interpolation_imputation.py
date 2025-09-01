# Interpolation imputation
df['Temperature'] = df['Temperature'].interpolate()
print("Data after interpolation:\n", df)
