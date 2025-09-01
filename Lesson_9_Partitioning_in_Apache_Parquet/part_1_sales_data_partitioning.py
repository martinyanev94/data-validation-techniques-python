# Import necessary libraries
import pandas as pd
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("PartitioningExample").getOrCreate()

# Sample sales data
data = {
    "order_id": [1, 2, 3, 4],
    "customer_id": ["C1", "C2", "C1", "C3"],
    "region": ["North", "South", "North", "West"],
    "order_date": ["2023-01-01", "2023-01-02", "2023-01-01", "2023-01-03"],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the Pandas DataFrame to a Spark DataFrame
sdf = spark.createDataFrame(df)

# Write the DataFrame to Parquet format with partitioning by region
sdf.write.partitionBy("region").parquet("sales_data_partitioned.parquet")
