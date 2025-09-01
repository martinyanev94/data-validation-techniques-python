# Creating a Series for favorite subjects
favorite_subjects = pd.Series(['Math', 'Science', 'History', 'Art'], index=students_df.index)

# Assigning the Series to a new column
students_df['Favorite Subject'] = favorite_subjects
print(students_df)
