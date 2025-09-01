# Filtering based on multiple conditions
filtered_students = students_df[(students_df['Age'] > 23) & (students_df['Grade'] == 'A')]
print(filtered_students)
