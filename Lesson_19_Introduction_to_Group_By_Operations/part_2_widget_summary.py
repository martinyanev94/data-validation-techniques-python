result = df.groupby("widget").sum()
print(result)
widget                     
Widget A       32         7
Widget B       36        12
result = df.groupby("widget")[["sales", "returns"]].agg("sum")
print(result)
