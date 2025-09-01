df['Sales'].iloc[3] = None  # Introduce a missing value
result_fillna = df['Sales'].fillna(0).agg(['sum', 'mean'])
print(result_fillna)
