# weather_modeling
#  Quadratic Weather Modeling System

This project demonstrates the development of a **Weather Prediction System** using **Quadratic Modeling** across three different Software Development Life Cycle (SDLC) methodologies:

 Waterfall Model
   Iterative Model
   Agile Model

The system fits a **quadratic equation** to historical temperature data and predicts future values.

 Problem Statement

Build a weather prediction application that models temperature trends using quadratic regression (`T = a·t² + b·t + c`) with historical data. The implementation explores three SDLC paradigms to show how development strategy influences design and features.

- Tools & Libraries Used

- Python 3.x
- NumPy
- Matplotlib
- scikit-learn (for Agile RMSE calculation)

 Waterfall Model

> A simple linear development cycle with hardcoded inputs and a one-time prediction.

 Features:
- Hardcoded data arrays
- Direct coefficient computation
- Predicts temperature for a fixed future day

`waterfall_model.py`

 Iterative Model

> Development is broken into repeated versions with incremental improvements.

Iteration 1:
- Takes temperature input from the user via keyboard

 `iterative_model_v1.py`

 Iteration 2:
- Reads historical data from a file (`data.txt`)
- Plots data and the quadratic fit

 `iterative_model_v2.py`



 Agile Model

> Sprint-based modular development with metrics and user-centric features.

 Sprint 1:
- Modular functions
- Keyboard input

 `agile_model_sprint1.py`

Sprint 3:
- Reads from file
- Predicts, graphs, and calculates RMSE
- Clean visualization and modular design

`agile_model_sprint3.py`

 Folder Structure
weather-modeling/
│
├── waterfall_model.py
├── iterative_model_v1.py
├── iterative_model_v2.py
├── agile_model_sprint1.py
├── agile_model_sprint3.py
├── data.txt
└── README.md

---

 Sample `data.txt` Format

1 22
2 24
3 27
4 33
5 40

Install required packages:
pip install numpy matplotlib scikit-learn

Run any model:
 waterfall_model.py
 iterative_model_v1.py
 iterative_model_v2.py
 agile_model_sprint1.py
 agile_model_sprint3.py
