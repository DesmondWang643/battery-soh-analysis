import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulated battery cycling data
np.random.seed(42)

cycles = np.arange(0, 501, 10)
initial_capacity = 100.0

# Simulate gradual capacity degradation
capacity = (
    initial_capacity
    - 0.035 * cycles
    + np.random.normal(0, 0.4, len(cycles))
)

# Calculate State of Health
soh = (capacity / initial_capacity) * 100

# Build dataset
data = pd.DataFrame({
    "Cycle": cycles,
    "Capacity_Percent": capacity,
    "SOH_Percent": soh
})

# Display summary
print(data.head())
print()
print(f"Initial SOH: {soh[0]:.2f}%")
print(f"Final SOH: {soh[-1]:.2f}%")
print(f"Capacity loss: {100 - soh[-1]:.2f}%")

# Save simulated data
data.to_csv("battery_soh_data.csv", index=False)

# Plot SOH trend
plt.figure(figsize=(10, 6))
plt.plot(data["Cycle"], data["SOH_Percent"], marker="o")

plt.axhline(
    y=80,
    linestyle="--",
    label="80% SOH reference"
)

plt.xlabel("Cycle Count")
plt.ylabel("State of Health (%)")
plt.title("Battery State of Health vs Cycle Count")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("battery_soh_plot.png", dpi=300)
plt.show()
