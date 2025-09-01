# Create a DataFrame
beatles_df = pd.DataFrame({
    "first": ["Paul", "John"],
    "last": ["McCartney", "Lennon"],
    "birth": [1942, 1940]
})

# Write DataFrame to JSON
json_output = beatles_df.to_json(orient='records')
print(json_output)
[{"first":"Paul","last":"McCartney","birth":1942},{"first":"John","last":"Lennon","birth":1940}]
