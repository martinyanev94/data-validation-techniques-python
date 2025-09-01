# Concatenate the sales DataFrames side by side
side_by_side_sales = pd.concat([sales_2020, sales_2021], axis=1)
print(side_by_side_sales)
