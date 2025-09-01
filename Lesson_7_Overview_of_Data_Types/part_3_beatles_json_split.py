# Write DataFrame to JSON using 'split' orientation
json_split = beatles_df.to_json(orient='split')
print(json_split)
{"index":[0,1],"columns":["first","last","birth"],"data":[["Paul","McCartney",1942],["John","Lennon",1940]]}
