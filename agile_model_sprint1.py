# Sprint 1 - Agile Quadratic Model with functions

import numpy as np

def get_data():
    n = int(input("Enter number of data points: "))
    days, temps = [], []
    for i in range(n):
        d = int(input(f"Day {i+1}: "))
        t = float(input(f"Temp on day {d}: "))
        days.append(d)
        temps.append(t)
    return np.array(days), np.array(temps)

def train_model(days, temps):
    return np.polyfit(days, temps, 2)

def predict_temp(coeffs, future_day):
    a, b, c = coeffs
    return a * future_day**2 + b * future_day + c

def main():
    print("=== Weather Predictor (Agile Sprint 1) ===")
    days, temps = get_data()
    coeffs = train_model(days, temps)
    future_day = int(input("Enter future day to predict: "))
    pred = predict_temp(coeffs, future_day)
    print(f"Predicted Temp on day {future_day}: {pred:.2f}°C")

main()
