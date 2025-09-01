# New DataFrame with floating-point values
data_floats = {
    'Temperature': [20.5, 21.8, 19.7, 20.9, 22.1],  # Normal temperatures
    'Humidity': [30.2, 60.1, 45.8, 40.4, 35.2]  # Humidity levels
}

df_floats = pd.DataFrame(data_floats)

# Change to float32 to save memory
df_floats['Temperature'] = df_floats['Temperature'].astype(np.float32)
df_floats['Humidity'] = df_floats['Humidity'].astype(np.float32)

# Check the memory usage
print(df_floats.memory_usage(deep=True))
