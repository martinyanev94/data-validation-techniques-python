pip install pandas
import pandas as pd
from pandas.testing import assert_frame_equal

def add_dataframes(df_a, df_b):
    return df_a + df_b

# Sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8])
expected_result = pd.DataFrame({'A': [6, 8], 'B': [10, 12]})

# Test
result = add_dataframes(df1, df2)
assert_frame_equal(result, expected_result)

print("Test passed: DataFrames are equal!")
