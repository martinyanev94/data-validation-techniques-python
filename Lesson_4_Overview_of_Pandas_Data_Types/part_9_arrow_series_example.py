import pyarrow as pa

# Creating a Series with Arrow types
arrow_series = pd.Series(["2024-01-01", "2024-01-02"], dtype=pd.ArrowDtype(pa.date32()))
print(arrow_series)
1    2024-01-02
dtype: date32[day][pyarrow]
