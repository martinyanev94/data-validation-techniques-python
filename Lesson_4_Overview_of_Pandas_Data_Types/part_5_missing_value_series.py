# Series with a missing value
mixed_series = pd.Series([1, pd.NA, 3], dtype=pd.Int64Dtype())
print(mixed_series)
1    <NA>
2       3
dtype: Int64
