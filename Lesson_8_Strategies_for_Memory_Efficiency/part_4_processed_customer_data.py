# Save the DataFrame to a compressed CSV
final_df.to_csv('processed_customer_data.csv', compression='gzip', index=False)
