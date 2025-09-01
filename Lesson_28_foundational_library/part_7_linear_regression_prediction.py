from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[1], [2], [3], [4]])
y = np.array([1, 3, 2, 3])

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predicting new values
predictions = model.predict(np.array([[5], [6]]))
print(predictions)
