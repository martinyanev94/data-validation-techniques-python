import pandas as pd

# Creating a pandas Series with 64-bit integers
int_series = pd.Series(range(3), dtype=pd.Int64Dtype())
print(int_series)
1    1
2    2
dtype: Int64
