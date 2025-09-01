zip_codes = ['80201', '90001', '10001', '60601', '80201']  # Repeated ZIP codes for test
df_zip = pd.DataFrame(zip_codes, columns=['ZIP_Code'])

# Store ZIP_Code as a categorical
df_zip['ZIP_Code'] = df_zip['ZIP_Code'].astype('category')

print(df_zip['ZIP_Code'].dtypes)
