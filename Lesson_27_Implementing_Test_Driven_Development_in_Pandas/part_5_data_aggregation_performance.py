import numpy as np
import time

def aggregate_data(df):
    return df.groupby('Category').sum()

# Create a large sample DataFrame
np.random.seed(0)
large_df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=1000000),
    'Value': np.random.rand(1000000)
})

def test_aggregate_performance():
    start_time = time.time()
    result = aggregate_data(large_df)
    end_time = time.time()
    
    print(f"Aggregation time: {end_time - start_time} seconds")
    assert not result.empty  # Ensure we produce a result

test_aggregate_performance()
