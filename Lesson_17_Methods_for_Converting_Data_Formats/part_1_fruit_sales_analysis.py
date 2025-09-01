import pandas as pd

data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas'],
    '2019': [120, 200, 100],
    '2020': [150, 240, 130]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
stacked_df = df.set_index('Fruit').stack().reset_index()
stacked_df.columns = ['Fruit', 'Year', 'Sales']
print("\nStacked DataFrame:")
print(stacked_df)
