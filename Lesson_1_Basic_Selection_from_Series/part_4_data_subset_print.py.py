subset_labels = data[["b", "c", "d"]]
print(subset_labels)
c    30
d    40
dtype: int64
subset_indices = data.iloc[[1, 2, 3]]  # Accessing second to fourth elements
print(subset_indices)
c    30
d    40
dtype: int64
