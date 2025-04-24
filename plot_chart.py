import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/new_automatic_samples.csv")
df = df[["price"]].dropna()
df["price"] = df["price"] / 1_000_000_009

# Plot the line chart using index as x-axis
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["price"], linestyle="-", marker="", color="b")

# Add labels and title
plt.xlabel("Index (Order of Entries)")
plt.ylabel("Mức giá (Tỷ VND)")
plt.title("Biểu đồ biến động giá")

# Show the plot
plt.grid(True)
plt.show()
