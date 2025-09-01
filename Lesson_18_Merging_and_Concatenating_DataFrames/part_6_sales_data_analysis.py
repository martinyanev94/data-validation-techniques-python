sales_2020 = pd.DataFrame({
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Sales': [1500, 1800, 1600, 2000]
})

sales_2021 = pd.DataFrame({
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Sales': [1700, 2200, 1900, 2500]
})

# Concatenate the two DataFrames vertically
concatenated_sales = pd.concat([sales_2020, sales_2021], ignore_index=True)
print(concatenated_sales)
