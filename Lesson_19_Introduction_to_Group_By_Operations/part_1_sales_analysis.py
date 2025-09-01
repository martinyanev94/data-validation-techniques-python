import pandas as pd

df = pd.DataFrame([
    ["North", "Widget A", "Jan", 10, 2],
    ["North", "Widget B", "Jan", 4, 0],
    ["South", "Widget A", "Jan", 8, 3],
    ["South", "Widget B", "Jan", 12, 8],
    ["North", "Widget A", "Feb", 3, 0],
    ["North", "Widget B", "Feb", 7, 0],
    ["South", "Widget A", "Feb", 11, 2],
    ["South", "Widget B", "Feb", 13, 4],
], columns=["region", "widget", "month", "sales", "returns"])
