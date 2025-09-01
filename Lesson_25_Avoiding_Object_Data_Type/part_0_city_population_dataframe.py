import pandas as pd

data = {
    'City': ['Denver', 'Los Angeles', 'New York', 'Chicago'],
    'Population': [715522, 3971883, 8419600, 2695598]
}

df = pd.DataFrame(data)

# Check the data types
print(df.dtypes)
