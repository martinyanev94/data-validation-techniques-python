result_diff_agg = df.groupby(['Category', 'Region']).agg({
    'Sales': ['sum', 'mean'],
    'Category': 'count'
})
print(result_diff_agg)
sum        mean           
Category    Region      
Clothing    North  300.0  300.000000           1
            South  400.0  400.000000           1
Electronics North  250.0  250.000000           1
            South  150.0  150.000000           1
Home        North  350.0  350.000000           1
            South  450.0  450.000000           1
