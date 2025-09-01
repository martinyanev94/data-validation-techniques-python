ser3 = pd.Series([2, 4], dtype=pd.Int64Dtype())
result_non_align = ser + ser3
print(result_non_align)
1       5
2    <NA>
dtype: Int64
