import pandas as pd

# Sample categorical data
data = {
    'Fruit': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Cherry', 'Banana', 'Apple'],
    'Color': ['Red', 'Yellow', 'Orange', 'Red', 'Yellow', 'Red', 'Yellow', 'Red']
}

df = pd.DataFrame(data)
print(df)
