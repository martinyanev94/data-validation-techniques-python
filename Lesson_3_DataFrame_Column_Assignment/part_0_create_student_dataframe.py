import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [23, 25, 22, 24],
    'Grade': ['A', 'B', 'A', 'C']
}

students_df = pd.DataFrame(data)
print(students_df)
