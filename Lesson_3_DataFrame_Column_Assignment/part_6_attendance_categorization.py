# Categorizing students based on attendance
students_df['Attendance Category'] = students_df['Attendance'].apply(lambda x: 'Low' if x < 90 else 'High')
print(students_df)
