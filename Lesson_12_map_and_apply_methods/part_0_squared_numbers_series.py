import pandas as pd

numbers = pd.Series([1, 2, 3, 4, 5])
squared_numbers = numbers.map(lambda x: x**2)
print(squared_numbers)
1     4
2     9
3    16
4    25
dtype: int64
