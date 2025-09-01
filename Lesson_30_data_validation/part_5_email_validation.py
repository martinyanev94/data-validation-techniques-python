import re

# Create a sample DataFrame for email validation
email_data = {
    'email': ['test@gmail.com', 'invalid-email', 'another.test@domain.com', 'invalid@.com'],
}

email_df = pd.DataFrame(email_data)

# Define a simple regex for basic email validation
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validate email formats
email_df['email_valid'] = email_df['email'].apply(lambda x: bool(re.match(email_pattern, x)))
print("Email validation results:")
print(email_df)
