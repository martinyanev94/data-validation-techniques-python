chunk_size = 10000  # Define how many rows we want to read at a time
chunks = []

# Read the CSV in chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Process the chunk (e.g., filter, aggregate, etc.)
    processed_chunk = chunk[chunk['PurchaseAmount'] > 100]  # Keep only significant purchases
    chunks.append(processed_chunk)

# Concatenate processed chunks into a final DataFrame
final_df = pd.concat(chunks, ignore_index=True)

print(final_df.shape)
