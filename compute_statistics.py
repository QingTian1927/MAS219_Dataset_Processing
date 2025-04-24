import pandas as pd
import numpy as np
from scipy.stats import t

df = pd.read_csv("data/auto-manual_toyota_samples.csv")

column_name = "price"
data = df[column_name].dropna()  # Drop missing values

# Compute statistics
mean_x = data.mean()
std_dev = data.std(ddof=1)  # Sample standard deviation (n-1)
count_n = len(data)
sum_x = data.sum()
se = std_dev / np.sqrt(count_n)  # Standard Error
t_value = t.ppf(0.975, df=count_n - 1)  # t(α/2, df) for 95% confidence interval

print(f"Mean (X): {mean_x}")
print(f"Standard Error (SE): {se}")
print(f"Standard Deviation (s): {std_dev}")
print(f"Count (n): {count_n}")
print(f"Sum: {sum_x}")
print(f"t(α/2, df): {t_value}")
#print(f"Decision: {'Reject' if abs(t_stat) > t_critical else 'Fail to reject'} the null hypothesis")
