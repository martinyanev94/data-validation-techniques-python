import pandas as pd

# Sample continuous data
data = {
    'Height': [170.5, 165.0, 180.2, 155.3, 172.4, 168.8, 177.5, 160.0],
    'Weight': [65.0, 60.5, 80.0, 50.0, 70.2, 55.3, 75.0, 58.0]
}

df = pd.DataFrame(data)
print(df)
