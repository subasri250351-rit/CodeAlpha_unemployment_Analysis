import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Unemployment in India.csv")

# Display first 5 rows
print(data.head())

# Display dataset information
print("\nDataset Info:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Remove missing values
data = data.dropna()

# Plot unemployment rate by region
plt.figure(figsize=(12,6))
plt.bar(data['Region'], data[' Estimated Unemployment Rate (%)'])
plt.xticks(rotation=90)
plt.xlabel("Region")
plt.ylabel("Estimated Unemployment Rate (%)")
plt.title("Unemployment Rate by Region")
plt.tight_layout()
plt.show()