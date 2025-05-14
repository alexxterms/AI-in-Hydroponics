import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 10000

# Generate features with realistic means and standard deviations
pH = np.random.normal(loc=6.0, scale=0.3, size=num_samples)  # Typical range: 5.5 - 6.5
EC = np.random.normal(loc=1.6, scale=0.2, size=num_samples)  # Electrical Conductivity
temperature = np.random.normal(loc=20, scale=2.5, size=num_samples)  # Air temp
humidity = np.random.normal(loc=70, scale=5, size=num_samples)  # Humidity %
light = np.random.normal(loc=16000, scale=1200, size=num_samples)  # Light intensity
water_temperature = np.random.normal(loc=18, scale=2, size=num_samples)  # Water temp

# Generate correlated growth rate
growth_rate = (
    0.2 * (pH - 5.5) + 
    0.5 * (EC - 1.2) + 
    0.1 * (temperature - 18) +
    0.2 * (humidity - 65) +
    0.3 * ((light - 15000) / 2000) + 
    0.2 * ((water_temperature - 17) / 2) +
    np.random.normal(scale=0.05, size=num_samples)  # Add some noise
)

# Ensure growth rate is non-negative
growth_rate = np.clip(growth_rate, 0, None)

# Create DataFrame
df = pd.DataFrame({
    'pH': pH,
    'EC': EC,
    'temperature': temperature,
    'humidity': humidity,
    'light': light,
    'water_temperature': water_temperature,
    'growth_rate': growth_rate
})

# Save to CSV
df.to_csv("synthetic_hydroponics_data.csv", index=False)

print("✅ Synthetic dataset created: 10,000+ samples saved as 'synthetic_hydroponics_data.csv'")
print(df.head())
