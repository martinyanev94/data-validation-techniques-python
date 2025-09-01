# Creating a dataset with ages for validation
age_data = {
    'age': [25, 150, -5, 30, 45],
}

age_df = pd.DataFrame(age_data)

# Define acceptable range
min_age = 0
max_age = 120

# Validate ages
age_df['age_valid'] = age_df['age'].apply(lambda x: min_age <= x <= max_age)
print("Age validation results:")
print(age_df)
