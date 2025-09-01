def filter_after_date(df, date_column, date):
    df[date_column] = pd.to_datetime(df[date_column])  # Ensure it's datetime
    return df[df[date_column] >= date]

# Sample DataFrame with date
df_dates = pd.DataFrame({
    'Date': ['2021-01-01', '2021-06-15', '2021-03-07'],
    'Value': [100, 200, 150]
})
expected_result = pd.DataFrame({
    'Date': ['2021-06-15'],
    'Value': [200]
})

def test_filter_after_date():
    result = filter_after_date(df_dates, 'Date', '2021-03-01')
    result['Date'] = result['Date'].dt.strftime('%Y-%m-%d')  # for comparison
    assert_frame_equal(result, expected_result)

test_filter_after_date()
print("Test passed: Filtered DataFrame matches the expected result!")
