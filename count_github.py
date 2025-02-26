import pandas as pd

# List of actual CSV files
files = ["question_tags.csv", "questions.csv"]  # Use correct filenames
count = 0
chunk_size = 10000  # Process 10,000 rows at a time

for file in files:
    print(f"Processing {file}...")  # Progress indicator
    
    # Read the CSV file in chunks
    for chunk in pd.read_csv(file, encoding="utf-8", on_bad_lines="skip", chunksize=chunk_size):
        contains_github = chunk.astype(str).apply(lambda col: col.str.contains("GitHub", case=False, na=False))
        count += contains_github.any(axis=1).sum()

print(f"Total lines containing 'GitHub': {count}")
