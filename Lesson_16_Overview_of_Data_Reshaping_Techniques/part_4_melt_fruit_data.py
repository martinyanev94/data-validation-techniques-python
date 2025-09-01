melted_df = pd.melt(fruit_df, id_vars=['state'], var_name='fruit', value_name='number_grown')
print(melted_df)
