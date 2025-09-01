fruits = pd.Series(['apple', 'banana', 'cherry', 'date'])
uppercase_fruits = fruits.map(lambda x: x.upper())
print(uppercase_fruits)
1     BANANA
2     CHERRY
3       DATE
dtype: object
