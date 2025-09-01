# Selecting a row by label
charlie_info = students_df.loc[2]  # Assuming Charlie is in the 2nd position
print(charlie_info)
Age             22
Grade           A
Name: 2, dtype: object
# Selecting specific row and columns by label
charlie_name_and_grade = students_df.loc[2, ['Name', 'Grade']]
print(charlie_name_and_grade)
Grade           A
Name: 2, dtype: object
