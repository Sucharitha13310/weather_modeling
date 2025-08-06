# Iteration 1 - Quadratic Model from keyboard input

import numpy as np

n = int(input("Enter number of data points: "))
days = []
temps = []

for i in range(n):
    d = int(input(f"Day {i+1}: "))
    t = float(input(f"Temp on day {d}: "))
    days.append(d)
    temps.append(t)

coeffs = np.polyfit(days, temps, 2)
a, b, c = coeffs

future_day = int(input("Enter future day to predict temp: "))
predicted_temp = a * future_day**2 + b * future_day + c
print(f"[Iterative 1] Predicted temperature: {predicted_temp:.2f}°C")
