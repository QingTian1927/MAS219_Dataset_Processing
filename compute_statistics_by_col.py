import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv("data/new_automatic_toyota_samples.csv")

col = df['price']

mean_x = np.mean(col)
std_dev = np.std(col, ddof=1)  # Sample standard deviation
sample_var = np.var(col, ddof=1)  # Sample variance
se = std_dev / np.sqrt(len(col))  # Standard error
median = np.median(col)
mode = col.mode().values[0] if not col.mode().empty else None
q1 = np.percentile(col, 25)  # First quartile
q2 = median  # Second quartile (Median)
q3 = np.percentile(col, 75)  # Third quartile
minimum = np.min(col)
maximum = np.max(col)
range_val = maximum - minimum
count_n = len(col)
sum_val = np.sum(col)

# Compute t(α/2, df) for 95% confidence level
alpha = 0.05
t_critical = stats.t.ppf(1 - alpha / 2, df=count_n - 1)

stats_dict = {
    "Mean (X)": mean_x,
    "Standard Error (SE)": se,
    "Median": median,
    "Mode": mode,
    "Standard Deviation (s)": std_dev,
    "Sample Variance (s²)": sample_var,
    "Q1": q1,
    "Q2 (Median)": q2,
    "Q3": q3,
    "Minimum": minimum,
    "Maximum": maximum,
    "Range (Max - Min)": range_val,
    "Sum": sum_val,
    "Count (n)": count_n,
    "t(α/2) - 95%": t_critical
}

for key in stats_dict:
    print(f"{key} {stats_dict[key]}")