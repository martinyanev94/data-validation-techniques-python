def validate_data(df):
    # Validate data types
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['birthdate'] = pd.to_datetime(df['birthdate'], errors='coerce')
    
    # Check for missing values
    missing_values = df.isnull().sum()
    
    # Validate ranges
    age_valid = df['age'].between(0, 120)
    
    # Validate categories
    valid_genders = ['Male', 'Female']
    gender_valid = df['gender'].apply(lambda x: x in valid_genders)
    
    # Compile results
    return missing_values, age_valid, gender_valid

# Validate using the function
miss_vals, ages_valid, genders_valid = validate_data(df)
print("Missing values:", miss_vals)
print("Age valid:", ages_valid)
print("Gender valid:", genders_valid)
