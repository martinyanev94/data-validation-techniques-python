from sklearn.impute import KNNImputer

# Instantiate KNN imputer
imputer = KNNImputer(n_neighbors=2)

# Modify the DataFrame for KNN imputation
df[['Temperature']] = imputer.fit_transform(df[['Temperature']])
print("Data after KNN imputation:\n", df)
