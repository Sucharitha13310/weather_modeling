# Iteration 2 - File input + Graph

import numpy as np
import matplotlib.pyplot as plt

# Read data from file
days, temps = [], []
with open("data.txt", "r") as file:
    for line in file:
        d, t = line.strip().split()
        days.append(int(d))
        temps.append(float(t))

# Fit quadratic model
coeffs = np.polyfit(days, temps, 2)
a, b, c = coeffs

# Predict for a future day
future_day = 6
predicted_temp = a * future_day**2 + b * future_day + c
print(f"[Iterative 2] Predicted temperature on day {future_day}: {predicted_temp:.2f}°C")

# Plot data and model
x_vals = np.linspace(min(days), future_day, 100)
y_vals = a * x_vals**2 + b * x_vals + c

plt.scatter(days, temps, color='blue', label='Data')
plt.plot(x_vals, y_vals, color='red', label='Quadratic Fit')
plt.scatter([future_day], [predicted_temp], color='green', label='Prediction')
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.title("Quadratic Weather Prediction")
plt.grid(True)
plt.show()
