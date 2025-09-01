import pandas as pd

# Sample data creation 
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': ['25', 'thirty', '35'],  # Note the issue here with 'thirty'
    'birthdate': ['1995-05-21', '1990-08-15', 'not_a_date'],  # Another issue
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Check current data types
print("Current data types:")
print(df.dtypes)
# Correcting the 'age' column to numeric
df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Converting to numeric, coercing errors.

# Fixing the 'birthdate' column to datetime
df['birthdate'] = pd.to_datetime(df['birthdate'], errors='coerce')  # Converting to datetime

print("Corrected data types:")
print(df.dtypes)
print(df)
