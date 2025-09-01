import pandas as pd

# Creating a sample DataFrame
data = {
    'Age': [25, 30, 35, 40, 45], 
    'Salary': [50000, 60000, 65000, 70000, 80000],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Check data types and memory usage
print(df.dtypes)
print(df.memory_usage(deep=True))
