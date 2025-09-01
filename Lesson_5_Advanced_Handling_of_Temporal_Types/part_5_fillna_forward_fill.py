# Introducing NaT values
df_dates.loc[2, 'date'] = pd.NaT

# Forward filling missing values
df_dates['date_filled'] = df_dates['date'].fillna(method='ffill')

print(df_dates)
