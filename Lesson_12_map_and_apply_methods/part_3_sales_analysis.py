sales_df['Total_Sales'] = sales_df.apply(lambda row: row['Quantity'] * row['Price_per_Unit'], axis=1)
def categorize_sales(sales):
    if sales > 300:
        return "High"
    else:
        return "Low"

sales_df['Sales_Category'] = sales_df['Total_Sales'].apply(categorize_sales)
print(sales_df)
0       A        10               20           200            Low
1       B        15               30           450           High
2       C         5               40           200            Low
