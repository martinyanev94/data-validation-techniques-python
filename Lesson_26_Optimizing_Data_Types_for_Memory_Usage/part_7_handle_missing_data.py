# Example of handling missing data
data_with_nan = {
    'Age': [25, None, 35, 40, None],  # Contains NaN values
}

df_with_nan = pd.DataFrame(data_with_nan)

# Convert Age to float for NaN compatibility
df_with_nan['Age'] = df_with_nan['Age'].astype(np.float32)
print(df_with_nan.dtypes)
