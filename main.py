import pandas as pd
from cleaning import clean_record
from similarity import calculate_total_similarity
from merger import merge_records

SIMILARITY_THRESHOLD = 0.75

def main():
    df = pd.read_csv('sample_dataset.csv')

    records = [clean_record(row) for _, row in df.iterrows()]

    visited = set()
    merged_records = []

    for i in range(len(records)):
        if i in visited:
            continue

        record1 = records[i]
        merged = record1

        for j in range(i + 1, len(records)):
            if j in visited:
                continue

            record2 = records[j]

            score = calculate_total_similarity(record1, record2)

            if score >= SIMILARITY_THRESHOLD:
                merged = merge_records(record1, record2)
                visited.add(j)

        merged_records.append(merged)

    output_df = pd.DataFrame(merged_records)
    output_df.to_csv("merged_output.csv", index=False)

    print("Duplicate detection completed.")
    print("Merged output saved.")

if __name__ == "__main__":
    main()
