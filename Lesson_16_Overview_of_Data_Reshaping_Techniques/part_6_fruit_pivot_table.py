pivot_df = pd.pivot_table(long_fruit_df, index='state', columns='fruit', values='number_grown', aggfunc='sum')
print(pivot_df)
