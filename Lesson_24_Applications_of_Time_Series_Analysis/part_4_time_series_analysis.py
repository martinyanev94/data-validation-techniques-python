from statsmodels.tsa.stattools import adfuller

# Perform the Augmented Dickey-Fuller test
result = adfuller(daily_crimes)

# Extracting the p-value
p_value = result[1]
print(f'p-value: {p_value}')
from statsmodels.tsa.arima.model import ARIMA

# Fit ARIMA model - parameters p, d, q need to be defined based on analysis
model = ARIMA(daily_crimes, order=(1, 1, 1))
model_fit = model.fit()

# Make predictions
forecast = model_fit.forecast(steps=30)
print(forecast)
