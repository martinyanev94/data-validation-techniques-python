import pandas as pd

df_q1 = pd.DataFrame({
    'ticker': ['AAPL', 'MSFT', 'AMZN'],
    'shares': [100, 80, 60],
    'low': [50, 42, 40],
    'high': [75, 62, 120]
})

df_q2 = pd.DataFrame({
    'ticker': ['AAPL', 'MSFT', 'IBM'],
    'shares': [90, 100, 75],
    'low': [70, 60, 59],
    'high': [80, 70, 64]
})

# Concatenating DataFrames
combined_df = pd.concat([df_q1, df_q2], ignore_index=True)
print(combined_df)
