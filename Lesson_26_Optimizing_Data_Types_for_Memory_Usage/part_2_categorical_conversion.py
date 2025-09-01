df['City'] = df['City'].astype('category')

# Check data types and memory usage again
print(df.dtypes)
print(df.memory_usage(deep=True))
