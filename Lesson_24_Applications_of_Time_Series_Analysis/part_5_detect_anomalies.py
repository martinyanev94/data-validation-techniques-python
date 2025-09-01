# Calculating IQR
Q1 = daily_crimes.quantile(0.25)
Q3 = daily_crimes.quantile(0.75)
IQR = Q3 - Q1

# Define bounds for normality
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Detecting anomalies
anomalies = daily_crimes[(daily_crimes < lower_bound) | (daily_crimes > upper_bound)]
print("Anomalous crime counts:\n", anomalies)
