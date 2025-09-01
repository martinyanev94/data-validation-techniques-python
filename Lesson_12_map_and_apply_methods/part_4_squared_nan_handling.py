data_with_nan = pd.Series([1, 2, None, 4])
squared_with_nan = data_with_nan.map(lambda x: x**2)
print(squared_with_nan)
1     4.0
2     NaN
3    16.0
dtype: float64
