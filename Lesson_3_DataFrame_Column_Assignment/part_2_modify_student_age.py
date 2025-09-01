# Modifying an existing column
students_df.loc[students_df['Name'] == 'Bob', 'Age'] = 26
print(students_df)
