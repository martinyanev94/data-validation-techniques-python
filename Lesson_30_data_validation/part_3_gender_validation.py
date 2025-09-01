# Create a DataFrame for demonstration
category_data = {
    'gender': ['Male', 'Female', 'unknown', 'Female', 'Not Specified'],
}

cat_df = pd.DataFrame(category_data)

# Define valid categories
valid_genders = ['Male', 'Female']

# Check for inconsistencies
cat_df['gender_valid'] = cat_df['gender'].apply(lambda x: x in valid_genders)
print("Gender validation results:")
print(cat_df)
