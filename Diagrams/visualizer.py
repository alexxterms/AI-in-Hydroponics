import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (Ensure lettuce_hydroponics_data.csv is in the same directory)
df = pd.read_csv("synthetic_hydroponics_data.csv")

# Set Seaborn style for better visuals
sns.set_theme(style="darkgrid")

# Create subplots (2x2 layout)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1️⃣ Light Intensity vs Temperature
sns.scatterplot(ax=axes[0, 0], x=df["light"], y=df["temperature"], color="orange")
axes[0, 0].set_title("Light Intensity vs. Temperature")
axes[0, 0].set_xlabel("Light Intensity (lux)")
axes[0, 0].set_ylabel("Temperature (°C)")

# 2️⃣ Temperature vs Humidity
sns.scatterplot(ax=axes[0, 1], x=df["temperature"], y=df["humidity"], color="blue")
axes[0, 1].set_title("Temperature vs. Humidity")
axes[0, 1].set_xlabel("Temperature (°C)")
axes[0, 1].set_ylabel("Humidity (%)")

# 3️⃣ pH vs Growth Rate
sns.lineplot(ax=axes[1, 0], x=df["pH"], y=df["growth_rate"], color="green", marker="o")
axes[1, 0].set_title("pH vs. Growth Rate")
axes[1, 0].set_xlabel("pH Level")
axes[1, 0].set_ylabel("Growth Rate (cm/day)")

# 4️⃣ EC vs Growth Rate
sns.lineplot(ax=axes[1, 1], x=df["EC"], y=df["growth_rate"], color="red", marker="o")
axes[1, 1].set_title("EC vs. Growth Rate")
axes[1, 1].set_xlabel("EC (Nutrient Concentration)")
axes[1, 1].set_ylabel("Growth Rate (cm/day)")

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plots
plt.show()
