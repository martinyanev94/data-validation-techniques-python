# Selecting specific rows and columns
first_two_names_ages = students_df.iloc[0:2, [0, 1]]  # Rows: 0-1, Columns: 0 and 1
print(first_two_names_ages)
0    Alice   23
1      Bob   25
