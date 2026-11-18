EnergyAI Predictor

A machine-learning web application that predicts monthly household electricity consumption based on household characteristics.

Project Overview

EnergyAI Predictor uses a Random Forest regression model to estimate electricity consumption in kilowatt-hours (kWh).

The application allows users to enter:

- Number of occupants
- Average temperature (°C)
- House size (m²)

The model processes these inputs and returns an estimated monthly electricity consumption.

Technologies Used

- Python
- Pandas
- Scikit-learn
- FastAPI
- HTML, CSS and JavaScript
- Git and GitHub
- Render (cloud deployment)

Model Performance

The Random Forest model achieved the following results on the test dataset:

Metric| Result
MAE| 32.01 kWh
RMSE| 41.13 kWh
R²| 0.9419

These metrics describe performance on the project's test dataset and do not establish accuracy for real-world households.

Live Application

"Try EnergyAI Predictor" (https://energyai-predictor.onrender.com)
EnergyAI Predictor

## Project Architecture

1. The user enters household information in the HTML interface.
2. JavaScript sends the input data to the FastAPI `/predict` endpoint using an HTTP POST request.
3. FastAPI validates the inputs using Pydantic.
4. The saved Random Forest model processes the input features and generates a prediction.
5. FastAPI returns the predicted electricity consumption as JSON.
6. JavaScript displays the prediction on the webpage.

**Architecture:** HTML/CSS/JavaScript → FastAPI → Random Forest Model → JSON Response → Webpage
