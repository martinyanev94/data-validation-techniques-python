encoded_data = pd.get_dummies(df, columns=['car_brand'], drop_first=True)
print(encoded_data)
