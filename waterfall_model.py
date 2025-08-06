# Waterfall Model - Quadratic Weather Prediction

import numpy as np

# Step 1: Requirements — Hardcoded historical data
days = np.array([1, 2, 3, 4, 5])  # Day numbers
temps = np.array([22, 24, 27, 33, 40])  # Temperatures

# Step 2: Design — Quadratic Model (ax^2 + bx + c)
coeffs = np.polyfit(days, temps, 2)
a, b, c = coeffs

# Step 3: Implementation — Predict temperature for day 6
future_day = 6
predicted_temp = a * future_day**2 + b * future_day + c

# Step 4: Output
print(f"[Waterfall] Predicted temperature on day {future_day}: {predicted_temp:.2f}°C")
