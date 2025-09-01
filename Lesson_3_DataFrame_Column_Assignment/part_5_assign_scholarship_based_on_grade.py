# Assigning values based on conditions
students_df['Scholarship'] = ['Yes' if grade == 'A' else 'No' for grade in students_df['Grade']]
print(students_df)
