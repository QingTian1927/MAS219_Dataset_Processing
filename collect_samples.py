import pandas as pd

INPUT_PATH = "data/cars.csv"
OUTPUT_PATH = "data/new_automatic_toyota_samples.csv"

df = pd.read_csv(INPUT_PATH)
filtered_df = df[(df["condition"] == "New car") & (df["transmission"] == "Automatic") & (df["brand"] == "Toyota")]

sample_size = min(600, len(filtered_df))  # Ensure sample size doesn't exceed available data
# Randomly sample without replacement
sampled_df = filtered_df.sample(n=sample_size, random_state=42)

sampled_df.to_csv(OUTPUT_PATH, index=False)
print(f"Randomly sampled {sample_size} cars saved to {OUTPUT_PATH}.")
