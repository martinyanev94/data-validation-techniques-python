fruit_df = pd.DataFrame({
    'state': ['Texas', 'Arizona', 'Florida'],
    'Apple': [12, 9, 0],
    'Orange': [10, 7, 14],
    'Banana': [40, 12, 190]
})

# Stacking to create a long format
long_fruit_df = fruit_df.set_index('state').stack().reset_index(name='number_grown')
long_fruit_df.columns = ['state', 'fruit', 'number_grown']
print(long_fruit_df)
