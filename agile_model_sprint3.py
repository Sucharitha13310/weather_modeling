# Sprint 3 - Agile: Add graph and RMSE

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def get_data():
    days, temps = [], []
    with open("data.txt", "r") as f:
        for line in f:
            d, t = map(float, line.strip().split())
            days.append(d)
            temps.append(t)
    return np.array(days), np.array(temps)

def train_model(days, temps):
    return np.polyfit(days, temps, 2)

def predict(coeffs, x_vals):
    a, b, c = coeffs
    return a * x_vals**2 + b * x_vals + c

def main():
    print("=== Agile Weather Model - Sprint 3 ===")
    days, temps = get_data()
    coeffs = train_model(days, temps)

    y_pred = predict(coeffs, days)
    rmse = np.sqrt(mean_squared_error(temps, y_pred))
    print(f"RMSE of Model: {rmse:.2f}")

    # Future prediction
    future_day = 6
    future_temp = predict(coeffs, future_day)
    print(f"Predicted Temp on day {future_day}: {future_temp:.2f}°C")

    # Plot
    x_vals = np.linspace(min(days), future_day, 100)
    y_vals = predict(coeffs, x_vals)
    plt.scatter(days, temps, label="Data", color='blue')
    plt.plot(x_vals, y_vals, label="Quadratic Fit", color='red')
    plt.scatter([future_day], [future_temp], color='green', label="Prediction")
    plt.legend()
    plt.xlabel("Day")
    plt.ylabel("Temperature")
    plt.title("Agile Weather Prediction Model")
    plt.grid(True)
    plt.show()

main()
