import pandas as pd
import numpy as np
import scipy.stats as stats

def hypothesis_decision(z_score, alpha=0.05):
    # Compute the critical value for a two-tailed test
    z_critical = stats.norm.ppf(1 - alpha/2)  # For 95% confidence, this is ~1.96

    # Print decision
    print(f"Z-score: {z_score:.4f}")
    print(f"Critical value: ±{z_critical:.4f}")

    if abs(z_score) > z_critical:
        print("Reject the null hypothesis (H₀): There is a significant difference in proportions.")
    else:
        print("Fail to reject the null hypothesis (H₀): No significant difference in proportions.")

INPUT_PATH = "data/cars.csv"
df = pd.read_csv(INPUT_PATH)

old_cars = df[(df["condition"] == "Used car") & (df["transmission"] == "Automatic") & (df["brand"] == "Toyota")]
old_cars_over_onebil = df[(df["condition"] == "Used car") & (df["transmission"] == "Automatic") & (df["brand"] == "Toyota") & (df['price'] > 1_000_000_000)]

new_cars = df[(df["condition"] == "New car") & (df["transmission"] == "Automatic") & (df["brand"] == "Toyota")]
new_cars_over_onebil = df[(df["condition"] == "New car") & (df["transmission"] == "Automatic") & (df["brand"] == "Toyota") & (df['price'] > 1_000_000_000)]

n1 = len(old_cars["price"])
n2 = len(new_cars["price"])

print(f"n1: {n1}")
print(f"n2: {n2}")

x1 = len(old_cars_over_onebil["price"])
x2 = len(new_cars_over_onebil["price"])

print(f"x1: {x1}")
print(f"x2: {x2}")

p1 = x1 / n1
p2 = x2 / n2

print(f"Sample proportion p1: {p1}")
print(f"Sample proportion p2: {p2}")

p_hat = (x1 + x2) / (n1 + n2)
se = np.sqrt(p_hat * (1 - p_hat) * ((1 / n1) + (1 / n2)))

print(f"p_hat: {p_hat}")
print(f"SE: {se}")

z_score = (p1 - p2) / se
hypothesis_decision(z_score)
