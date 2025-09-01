def merge_dataframes(df_a, df_b, on_column):
    return pd.merge(df_a, df_b, on=on_column)

# Sample DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': ['x', 'y']})
df2 = pd.DataFrame({'C': ['x', 'y'], 'D': [3, 4]})

# Test Function to expect an error
import pytest

def test_merge_dataframes():
    with pytest.raises(KeyError):
        merge_dataframes(df1, df2, 'A')  # Column 'A' should cause an error

test_merge_dataframes()
print("Test passed: KeyError raised as expected!")
