# Reading in JSON data with specific orientation
df_from_json = pd.read_json(io.StringIO(json_split), orient='split')
print(df_from_json)
