def sort_dataframe(df, column):
    return df.sort_values(by=column)

# Sample DataFrame to test sorting
df = pd.DataFrame({'A': [2, 1, 3], 'B': [4, 5, 6]})
expected_sorted = pd.DataFrame({'A': [1, 2, 3], 'B': [5, 4, 6]}).sort_values(by='A')

def test_sort_dataframe():
    sorted_df = sort_dataframe(df, 'A')
    assert_frame_equal(sorted_df, expected_sorted)

test_sort_dataframe()
print("Test passed: DataFrame sorted as expected!")
