# Write the DataFrame to Parquet format with partitioning by order_date
sdf.write.partitionBy("order_date").parquet("sales_data_by_date.parquet")
