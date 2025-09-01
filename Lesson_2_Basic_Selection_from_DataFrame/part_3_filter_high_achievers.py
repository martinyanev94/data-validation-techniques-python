# Filtering the DataFrame for students with an 'A' grade
high_achievers = students_df[students_df['Grade'] == 'A']
print(high_achievers)
0    Alice   23     A
2  Charlie   22     A
