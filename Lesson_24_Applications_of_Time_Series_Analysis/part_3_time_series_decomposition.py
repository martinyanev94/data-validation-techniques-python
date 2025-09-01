import statsmodels.api as sm

# Making sure daily crimes is a time series with a datetime index
daily_crimes.index = pd.to_datetime(daily_crimes.index)

# Decompose the time series
decomposition = sm.tsa.seasonal_decompose(daily_crimes, model='additive')

# Plotting the decomposition
decomposition.plot()
plt.show()
