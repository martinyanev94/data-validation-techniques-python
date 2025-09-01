# Group by region in a distributed manner
result_df = partitioned_df.groupBy("region").agg({"order_id": "count"})
result_df.show()
