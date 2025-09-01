# Sample aggregation function to balance partitions
aggregated_df = partitioned_df.groupBy("region").agg({"order_id": "count", "customer_id": "count"})

# Save aggregated data with partitioning
aggregated_df.write.partitionBy("region").parquet("aggregated_sales_by_region.parquet")
