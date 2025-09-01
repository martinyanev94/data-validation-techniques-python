import pandas as pd

data = {
    'car_brand': ['Toyota', 'Honda', 'Ford', 'Toyota', 'Ford', 'Honda', 'Chevrolet'],
    'sales': [1500, 1200, 900, 1700, 1100, 950, 1300]
}

df = pd.DataFrame(data)

print(df)
df['car_brand'] = df['car_brand'].astype('category')
