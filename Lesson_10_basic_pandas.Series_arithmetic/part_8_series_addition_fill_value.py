ser1 = pd.Series([1., 2., 3.], dtype=pd.Float64Dtype())
ser2 = pd.Series([4., pd.NA, 6.], dtype=pd.Float64Dtype())

result_fill = ser1.add(ser2, fill_value=0.)
print(result_fill)
1    2.0
2    9.0
dtype: Float64
