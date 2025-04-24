import pandas as pd

INPUT_PATH = "data/cars.csv"
OUTPUT_PATH = "data/brand_counts.csv"

try:
    with open(OUTPUT_PATH, mode="w+", encoding="utf-8") as output_file:
        df = pd.read_csv(INPUT_PATH)

        for brand in df["brand"].unique():
            filtered_df = df[df["brand"] == brand]
            output_file.write(f"[{brand.capitalize()}] {len(filtered_df)} car(s)\n")
except Exception as err:
    print("[FATAL] Script stopped due to exception:\n")
    print(err)