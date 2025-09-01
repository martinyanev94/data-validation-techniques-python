sales_data = {
    'Product': ['Widget A', 'Widget B'],
    'Q1_Sales': [100, 150],
    'Q2_Sales': [200, 250],
    'Q3_Sales': [300, 350],
    'Q4_Sales': [400, 450]
}

df_sales = pd.DataFrame(sales_data)
print("\nOriginal Sales DataFrame:")
print(df_sales)
long_sales_df = pd.wide_to_long(df_sales, stubnames='Q', i='Product', j='Quarter', sep='_')
long_sales_df = long_sales_df.reset_index()
print("\nLong Sales DataFrame:")
print(long_sales_df)
