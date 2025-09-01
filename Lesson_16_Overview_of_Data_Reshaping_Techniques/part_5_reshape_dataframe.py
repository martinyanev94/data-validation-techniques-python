df = pd.DataFrame({
    'widget': ['Widget 1', 'Widget 2'],
    'quarter_1': [1, 16],
    'quarter_2': [2, 32],
    'quarter_3': [4, 64],
    'quarter_4': [8, 128]
})

long_df = pd.wide_to_long(df, stubnames='quarter_', i='widget', j='quarter')
print(long_df.reset_index())
