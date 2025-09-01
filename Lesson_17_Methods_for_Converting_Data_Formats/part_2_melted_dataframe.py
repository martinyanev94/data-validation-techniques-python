df_melt = pd.melt(df, id_vars='Fruit', var_name='Year', value_name='Sales')
print("\nMelted DataFrame:")
print(df_melt)
