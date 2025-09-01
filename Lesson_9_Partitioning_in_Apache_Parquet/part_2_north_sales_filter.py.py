# Read the partitioned Parquet file
partitioned_df = spark.read.parquet("sales_data_partitioned.parquet")

# Filter sales data for the North region
north_sales = partitioned_df.filter(partitioned_df.region == "North")

# Show results
north_sales.show()
